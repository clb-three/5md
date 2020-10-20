import {socket} from "./socket";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Hand");

function onDragStart(ev, cardDisplay) {
    log.info("onDragStart");
    cardDisplay.data = ev.data;
    cardDisplay.dragging = true;
}

function onDragEnd(ev, cardDisplay, name, deck) {
    log.info("onDragEnd");
    cardDisplay.dragging = false;
    cardDisplay.data = null;

    const inGarbage = false;
    const shouldPlay = deck.containsPoint(ev.data.global);
    if (inGarbage) {
        socket.emit("command", `hero benji discard ${name}`);
    } else if (shouldPlay) {
        socket.emit("command", `hero benji play ${name}`);
    }
}

function onDragMove(cardDisplay) {
    if (cardDisplay.dragging) {
        log.debug("onDragMove");
        const newPosition = cardDisplay.data.getLocalPosition(cardDisplay.parent);
        cardDisplay.position.x = newPosition.x;
        cardDisplay.position.y = newPosition.y;
    }
}

export class Hand {
    constructor(display, deck) {
        this.handX = 100;
        this.cardDisplay = {};
        this.display = display;
        this.dragging = false;
        this.deck = deck;

        log.debug("hand x", this.handX);
    }

    drawCard(card) {
        log.debug("draw", card);

        const name = card.symbol;
        const y = 100;

        // load the texture we need
        const cardDisplay = this.display.sprite(`images/${name}.png`, this.handX, y, 100, 160);

        cardDisplay.interactive = true;
        cardDisplay.buttonMode = true;
        cardDisplay
            // events for drag start
            .on('mousedown', ev => onDragStart(ev, cardDisplay))
            .on('touchstart', ev => onDragStart(ev, cardDisplay))
            // events for drag end
            .on('mouseup', ev => onDragEnd(ev, cardDisplay, name, this.deck))
            .on('mouseupoutside', ev => onDragEnd(ev, cardDisplay, name, this.deck))
            .on('touchend', ev => onDragEnd(ev, cardDisplay, name, this.deck))
            .on('touchendoutside', ev => onDragEnd(ev, cardDisplay, name, this.deck))
            // events for drag move
            .on('mousemove', ev => onDragMove(cardDisplay))
            .on('touchmove', ev => onDragMove(cardDisplay));

        this.cardDisplay[card.uuid] = cardDisplay;
        this.handX += 60;
    }

    discardCard(card) {
        log.debug("discard", card);

        if (card) {
            this.display.deleteThisNephew(this.cardDisplay[card.uuid]);
            delete this.cardDisplay[card.uuid];
        }
    }
}