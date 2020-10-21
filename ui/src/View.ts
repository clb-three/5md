import * as PIXI from "pixi.js";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("display::View");

export class View {
    app: PIXI.Application;

    constructor() {
        const w = 800, h = 600;
        log.debug("w", w, "h", h);

        this.app = new PIXI.Application({
            width: w,
            height: h,
        });
        document.body.appendChild(this.app.view);
    }

    texture(name): PIXI.Texture {
        log.debug("get texture", name);

        return PIXI.Texture.from(name);
    }

    sprite(name, x, y, w, h): PIXI.Sprite {
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

    deleteThisNephew(chile: any): void {
        log.debug("delete", chile);
        this.app.stage.removeChild(chile);
    }

    text(text: string, x: number, y: number): PIXI.Text {
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