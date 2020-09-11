import {Display} from "./Display";
import {socket} from "./socket";

export class Model {
    constructor(state) {
        const name = "benji"; // TODO: Auth story: get a real name
        this.x = 100;

        this.display = new Display();

        const hero = state.heroes[name];
        this.cardDisplay = {};
        for (const card of hero.hand) {
            this.discardCard(card);
        }
        for (const card of hero.hand) {
            this.loadCard(card);
        }

        this.deck(hero.deck.length);
        this.target(state.target);
    }

    target(enemy) {
        if (this.targetDisplay) {
            this.display.deleteThisNephew(this.targetDisplay.target);
            this.display.deleteThisNephew(this.targetDisplay.targetType);
            this.display.deleteThisNephew(this.targetDisplay.targetSymbols);
        }

        const x = 300;
        const y = 300;
        const target = this.display.sprite(`images/badguy.png`, x, y, 100, 160);
        const targetType = this.display.text(enemy.type, x, y);
        const targetSymbols = this.display.text(enemy.symbols, x, y + 50);
        this.targetDisplay = {
            target,
            targetType,
            targetSymbols,
        };
    }

    targetSymbols(symbols) {
        this.targetDisplay.targetSymbols.text = symbols;
    }

    loadCard(card) {
        const name = card.symbol;
        const x = this.x;
        const y = 100;

        // load the texture we need
        const cardDisplay = this.display.sprite(`images/${name}.png`, x, y, 100, 160);

        cardDisplay.interactive = true;

        const onDown = () => socket.emit("command", `benji play ${name}`);
        cardDisplay.on("mousedown", () => onDown(name));
        cardDisplay.on("touchstart", () => onDown(name));
        this.cardDisplay[card.uuid] = cardDisplay;
        this.x += 60;
    }

    discardCard(card) {
        this.display.deleteThisNephew(this.cardDisplay[card.uuid]);
        delete this.cardDisplay[card.uuid];
    }

    deck(numCards) {
        if (!this.deckDisplay) {
            const x = 100;
            const y = 300;

            const deck = this.display.sprite(`images/back.png`, x, y, 100, 160);

            deck.interactive = true;

            const onDown = () => socket.emit("command", `benji draw`);
            deck.on("mousedown", () => onDown());
            deck.on("touchstart", () => onDown());

            const numCardsDisplay = this.display.text(numCards, x, y);

            this.deckDisplay = {
                deck,
                numCards: numCardsDisplay,
            };
        }

        this.deckDisplay.numCards.text = numCards;
    }
}