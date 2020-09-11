import {socket} from "./socket";

export class Deck {
    constructor(display) {
        this.display = display;
        const x = 100;
        const y = 300;

        const deck = this.display.sprite(`images/back.png`, x, y, 100, 160);

        deck.interactive = true;

        const onDown = () => socket.emit("command", `benji draw`);
        deck.on("mousedown", () => onDown());
        deck.on("touchstart", () => onDown());

        const numCardsDisplay = this.display.text("", x, y);

        this.deckDisplay = {
            deck,
            numCards: numCardsDisplay,
        };
    }

    setNumCards(numCards) {
        this.deckDisplay.numCards.text = numCards;
    }
}