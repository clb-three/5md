import {socket} from "./socket";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Deck");

export class Deck {
    constructor(display) {
        this.display = display;
        const x = 100;
        const y = 300;

        const deck = this.display.sprite(`images/back.png`, x, y, 100, 160);

        deck.interactive = true;

        const onDown = () => socket.emit("command", `hero benji draw`);
        deck.on("mousedown", () => onDown());
        deck.on("touchstart", () => onDown());

        const numCardsDisplay = this.display.text("", x, y);

        this.deckDisplay = {
            deck,
            numCards: numCardsDisplay,
        };

        log.debug("deck display", this.deckDisplay);
    }

    setNumCards(numCards) {
        log.debug("set number of cards", numCards);
        this.deckDisplay.numCards.text = numCards;
    }
}