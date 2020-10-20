import {socket} from "./socket";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Hand");

class Card {
    constructor(display, uuid, target) {
        this.uuid = uuid;
        this.display = display;
        this.target = target;

        this.display.interactive = true;
        this.display.buttonMode = true;
        this.display
            // events for drag start
            .on('mousedown', ev => this.onDragStart(ev))
            .on('touchstart', ev => this.onDragStart(ev))
            // events for drag end
            .on('mouseup', ev => this.onDragEnd(ev, this.deck))
            .on('mouseupoutside', ev => this.onDragEnd(ev, this.deck))
            .on('touchend', ev => this.onDragEnd(ev, this.deck))
            .on('touchendoutside', ev => this.onDragEnd(ev, this.deck))
            // events for drag move
            .on('mousemove', ev => this.onDragMove())
            .on('touchmove', ev => this.onDragMove());
    }

    onDragStart(ev) {
        log.info("onDragStart");
        this.display.data = ev.data;
        this.display.dragging = true;
    }

    onDragEnd(ev, deck) {
        log.info("onDragEnd");
        this.display.dragging = false;
        this.display.data = null;

        const inGarbage = false;
        const shouldPlay = this.target.containsPoint(ev.data.global);
        if (inGarbage) {
            socket.emit("command", `hero benji discard ${this.uuid}`);
        } else if (shouldPlay) {
            socket.emit("command", `hero benji play ${this.uuid}`);
        }
    }

    onDragMove() {
        if (this.display.dragging) {
            log.debug("onDragMove");
            const newPosition = this.display.data.getLocalPosition(this.display.parent);
            this.display.position.x = newPosition.x;
            this.display.position.y = newPosition.y;
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
        this.cardDisplay[card.uuid] = new Card(sprite, card.uuid, this.target);
        this.handX += 60;
    }

    discardCard(card) {
        log.debug("discard", card);

        if (card) {
            this.display.deleteThisNephew(this.cardDisplay[card.uuid].display);
            delete this.cardDisplay[card.uuid];
        }
    }
}