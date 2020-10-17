import * as PIXI from "pixi.js";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::Display");

export class Display {
    constructor() {
        const w = 800, h = 600;
        this.app = new PIXI.Application({
            width: w,
            height: h,
        });

        document.body.appendChild(this.app.view);
        log.debug("w", w, "h", h);
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