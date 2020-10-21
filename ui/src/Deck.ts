import {socket} from "./socket";
import * as loglevel from "loglevel";
import {BaseViewModelObject} from "./BaseViewModelObject";

const log = loglevel.getLogger("display::Deck");

export class Deck extends BaseViewModelObject {
    sprite: PIXI.Sprite;
    numCards: PIXI.Text;

    constructor(vm) {
        super(vm);
        const x = 100;
        const y = 300;

        this.sprite = this.view.sprite(`images/back.png`, x, y, 100, 160);
        this.sprite.interactive = true;
        this.sprite.buttonMode = true;
        const onDown = () => socket.emit("command", `hero benji draw`);
        this.sprite
            .on("mousedown", () => onDown())
            .on("touchstart", () => onDown());

        this.numCards = this.view.text("", x, y);
    }

    setNumCards(numCards) {
        log.debug("set number of cards", numCards);
        this.numCards.text = numCards;
    }
}