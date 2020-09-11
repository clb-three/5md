import {Display} from "./Display";
import {socket} from "./socket";

export class Model {
    doEvent(event) {
        console.log("event", event);
        switch (event.code) {
            case "state":
                this.initialize(event.obj);
                break;
            case "cardsleft":
                this.setNumCards(event.obj);
                break;
            case "drawcard":
                this.loadCard(event.obj[1]);
                break;
            case "playcard":
                this.deleteCard(event.obj[1]);
                break;
            case "enemy":
                this.setTarget(event.obj);
                break;
            case "hurt":
                this.setSymbols(event.obj);
                break;
            default:
                console.log("unhandled");
                break;
        }
    }

    initialize(state) {
        const name = "benji"; // TODO: Auth story: get a real name

        this.display = new Display();

        const hero = state.heroes[name];
        this.setHand(hero);
        this.setDeck(hero);
        this.setTarget(state.target);
    }

    setTarget(enemy) {
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
            targetSymbols
        };
    }

    setSymbols(symbols) {
        this.targetDisplay.targetSymbols.text = symbols;
    }

    setDeck(hero) {
        const x = 100;
        const y = 300;

        const deck = this.display.sprite(`images/back.png`, x, y, 100, 160);

        deck.interactive = true;

        const onDown = () => socket.emit("command", `benji draw`);
        deck.on("mousedown", () => onDown());
        deck.on("touchstart", () => onDown());

        const numCardsDisplay = this.display.text(hero.deck.length, x, y);

        this.deckDisplay = {
            deck,
            numCards: numCardsDisplay,
        };

        this.setNumCards(hero.deck.length);
    }

    setNumCards(numCards) {
        this.deckDisplay.numCards.text = numCards;
    }


    setHand(hero) {
        this.cardDisplay = {};

        this.x = 100;
        for (const card of hero.hand) {
            this.loadCard(card);
        }
    }

    loadCard(card) {
        const name = card.symbol;
        const y = 100;

        // load the texture we need
        const cardDisplay = this.display.sprite(`images/${name}.png`, this.x, y, 100, 160);

        cardDisplay.interactive = true;

        const onDown = () => socket.emit("command", `benji play ${name}`);
        cardDisplay.on("mousedown", () => onDown(name));
        cardDisplay.on("touchstart", () => onDown(name));
        this.cardDisplay[card.uuid] = cardDisplay;
        this.x += 60;
    }

    deleteCard(card) {
        display.deleteThisNephew(this.cardDisplay[card.uuid]);
        delete this.cardDisplay[card.uuid];
    }
}