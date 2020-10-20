import {socket} from "./socket";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Hand");

class Card {
    constructor(display, sprite, uuid, target) {
        this.uuid = uuid;
        this.display = display;
        this.sprite = sprite;
        this.target = target;

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
            .on('mousemove', ev => this.onDragMove())
            .on('touchmove', ev => this.onDragMove());
    }

    onDragStart(ev) {
        log.info("onDragStart");
        this.sprite.data = ev.data;
        this.sprite.dragging = true;
    }

    onDragEnd(ev) {
        log.info("onDragEnd");
        this.sprite.dragging = false;
        this.sprite.data = null;

        const inGarbage = false;
        const shouldPlay = this.display.target.containsPoint(ev.data.global);
        if (inGarbage) {
            socket.emit("command", `hero benji discard ${this.uuid}`);
        } else if (shouldPlay) {
            socket.emit("command", `hero benji play ${this.uuid}`);
        }
    }

    onDragMove() {
        if (this.sprite.dragging) {
            log.debug("onDragMove");
            const newPosition = this.sprite.data.getLocalPosition(this.sprite.parent);
            this.sprite.position.x = newPosition.x;
            this.sprite.position.y = newPosition.y;
        }
    }
}

export class Hand {
    constructor(display, target) {
        this.handX = 100;
        this.cardDisplay = {};
        this.display = display;
        this.dragging = false;
        this.target = target;

        log.debug("hand x", this.handX);
    }

    drawCard(card) {
        log.debug("draw", card);

        const y = 100;
        const sprite = this.display.sprite(`images/${card.name}.png`, this.handX, y, 100, 160);
        this.cardDisplay[card.uuid] = new Card(this.display, sprite, card.uuid);
        this.handX += 60;
    }

    discardCard(card) {
        log.debug("discard", card);

        if (card) {
            this.display.deleteThisNephew(this.cardDisplay[card.uuid].sprite);
            delete this.cardDisplay[card.uuid];
        }
    }
}