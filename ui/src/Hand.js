import {socket} from "./socket";

export class Hand {
    constructor(display) {
        this.handX = 100;
        this.cardDisplay = {};
        this.display = display;
    }

    drawCard(card) {
        const name = card.symbol;
        const y = 100;

        // load the texture we need
        const cardDisplay = this.display.sprite(`images/${name}.png`, this.handX, y, 100, 160);

        cardDisplay.interactive = true;

        const onDown = () => socket.emit("command", `benji play ${name}`);
        cardDisplay.on("mousedown", () => onDown(name));
        cardDisplay.on("touchstart", () => onDown(name));
        this.cardDisplay[card.uuid] = cardDisplay;
        this.handX += 60;
    }

    discardCard(card) {
        if (card) {
            this.display.deleteThisNephew(this.cardDisplay[card.uuid]);
            delete this.cardDisplay[card.uuid];
        }
    }
}