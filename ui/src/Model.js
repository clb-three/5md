import {Target} from "./Target";
import {Hand} from "./Hand";
import {Deck} from "./Deck";

export class Model {
    constructor(display) {
        this.deck = new Deck(display);
        this.hand = new Hand(display);
        this.target = new Target(display);
    }

    doEvent(event) {
        console.log("event", event);
        switch (event.code) {
            case "state":
                const state = event.obj;
                const name = "benji"; // TODO: Auth story: get a real name
                const hero = state.heroes[name];
                this.deck.setNumCards(hero.deck.length);
                for (const card of hero.hand) {
                    this.hand.drawCard(card);
                }
                this.target.drawEnemy(state.target);
                break;
            case "cardsleft":
                this.deck.setNumCards(event.obj);
                break;
            case "drawcard":
                this.hand.drawCard(event.obj[1]);
                break;
            case "playcard":
                this.hand.discardCard(event.obj[1]);
                break;
            case "enemy":
                this.target.drawEnemy(event.obj);
                break;
            case "hurt":
                this.target.setSymbols(event.obj);
                break;
            default:
                console.log("unhandled");
                break;
        }
    }
}