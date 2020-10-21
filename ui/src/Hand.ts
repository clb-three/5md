import {socket} from "./socket";
import * as loglevel from "loglevel";
import {BaseViewModelObject} from "./BaseViewModelObject";


const log = loglevel.getLogger("display::Hand");

class Card extends BaseViewModelObject {
    uuid: string;
    sprite: PIXI.Sprite;
    dragging: boolean;
    eventData: PIXI.InteractionData;

    constructor(vm, uuid, sprite) {
        super(vm);
        this.uuid = uuid;
        this.dragging = false;
        this.eventData = null;

        this.sprite = sprite;
        this.sprite.interactive = true;
        this.sprite.buttonMode = true;
        this.sprite
            // events for drag start
            .on('mousedown', ev => this.onDragStart(ev))
            .on('touchstart', ev => this.onDragStart(ev))
            // events for drag end
            .on('mouseup', ev => this.onDragEnd(ev))
            .on('mouseupoutside', ev => this.onDragEnd(ev))
            .on('touchend', ev => this.onDragEnd(ev))
            .on('touchendoutside', ev => this.onDragEnd(ev))
            // events for drag move
            .on('mousemove', _ => this.onDragMove())
            .on('touchmove', _ => this.onDragMove());
    }

    onDragStart(ev: PIXI.InteractionEvent) {
        log.info("onDragStart");
        this.eventData = ev.data;
        this.dragging = true;
    }

    onDragEnd(ev: PIXI.InteractionEvent) {
        log.info("onDragEnd");
        this.dragging = false;
        this.eventData = null;

        const inGarbage = false;
        const shouldPlay = this.vm.target.containsPoint(ev.data.global);
        if (inGarbage) {
            socket.emit("command", `hero benji discard ${this.uuid}`);
        } else if (shouldPlay) {
            socket.emit("command", `hero benji play ${this.uuid}`);
        }
    }

    onDragMove() {
        if (this.dragging) {
            log.debug("onDragMove");
            const newPosition = this.eventData.getLocalPosition(this.sprite.parent);
            this.sprite.position.x = newPosition.x;
            this.sprite.position.y = newPosition.y;
        }
    }
}

export class Hand extends BaseViewModelObject {
    cards: Map<string, Card>;
    handX: number;
    handY: number;

    constructor(vm) {
        super(vm);

        this.cards = new Map<string, Card>();

        this.handX = 100;
        this.handY = 100;
        log.debug("hand x", this.handX);
    }

    drawCard(card) {
        log.debug("draw", card);

        const sprite = this.view.sprite(`images/${card.name}.png`, this.handX, this.handY, 100, 160);
        this.cards[card.uuid] = new Card(this.vm, card.uuid, sprite);
        this.handX += 60;
    }

    discardCard(card) {
        log.debug("discard", card);

        if (card) {
            this.view.deleteThisNephew(this.cards[card.uuid].sprite);
            delete this.cards[card.uuid];
        }
    }
}