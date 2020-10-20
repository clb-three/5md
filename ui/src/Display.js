import * as PIXI from "pixi.js";
import * as loglevel from "loglevel";
import {Deck} from "./Deck";
import {Target} from "./Target";
import {Hand} from "./Hand";

const log = loglevel.getLogger("display::Display");

export class Display {
    constructor() {
        const w = 800, h = 600;
        log.debug("w", w, "h", h);
        this.app = new PIXI.Application({
            width: w,
            height: h,
        });
        document.body.appendChild(this.app.view);

        this.deck = new Deck(this);
        this.target = new Target(this);
        this.hand = new Hand(this);
    }

    doEvent(event) {
        switch (event.code) {
            case "state":
                const state = event.obj;
                const name = "benji"; // TODO: Auth story: get a real name
                const hero = state.heroes.find(h => h.name == name);
                this.deck.setNumCards(hero.deck.length);
                for (const card of hero.hand) {
                    this.hand.drawCard(card);
                }
                this.target.drawEnemy(state.door_deck.top);
                break;
            case "cardsleft":
                this.deck.setNumCards(event.obj);
                break;
            case "draw":
                this.hand.drawCard(event.obj[1]);
                break;
            case "discard":
                this.hand.discardCard(event.obj[1]);
                break;
            case "enemy":
                this.target.drawEnemy(event.obj);
                break;
            case "hurt":
                this.target.setSymbols(event.obj);
                break;
            default:
                log.warn("unhandled event", event);
                break;
        }
    }

    texture(name) {
        log.debug("get texture", name);
        return PIXI.Texture.from(name);
    }

    sprite(name, x, y, w, h) {
        log.debug("get sprite", name, x, y, w, h);

        const texture = this.texture(name);
        const sprite = new PIXI.Sprite(texture);
        sprite.anchor.set(0.5);
        sprite.position.set(x, y);
        sprite.width = w;
        sprite.height = h;
        this.app.stage.addChild(sprite);
        return sprite;
    }

    deleteThisNephew(chile) {
        log.debug("delete", chile);
        this.app.stage.removeChild(chile);
    }

    text(text, x, y) {
        log.debug("create text", text, x, y);
        const numCards = new PIXI.Text(text, {
            font: "35px Snippet",
            fill: "white",
            align: "left",
        });
        numCards.anchor.set(0.5);
        numCards.position.set(x, y);
        this.app.stage.addChild(numCards);
        return numCards;
    }
}