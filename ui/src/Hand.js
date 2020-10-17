import {socket} from "./socket";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Hand");

export class Hand {
    constructor(display) {
        this.handX = 100;
        this.cardDisplay = {};
        this.display = display;

        log.debug("hand x", this.handX);
    }

    drawCard(card) {
        log.debug("draw", card);

        const name = card.symbol;
        const y = 100;

        // load the texture we need
        const cardDisplay = this.display.sprite(`images/${name}.png`, this.handX, y, 100, 160);

        cardDisplay.interactive = true;

        const onDown = () => socket.emit("command", `hero benji play ${name}`);
        cardDisplay.on("mousedown", () => onDown(name));
        cardDisplay.on("touchstart", () => onDown(name));
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