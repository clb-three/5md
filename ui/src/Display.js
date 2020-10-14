import * as PIXI from "pixi.js";

export class Display {
    constructor() {
        this.app = new PIXI.Application({
            width: 800,
            height: 600,
        });

        document.body.appendChild(this.app.view);
    }

    texture(name) {
        return PIXI.Texture.from(name);
    }

    sprite(name, x, y, w, h) {
        const texture = this.texture(name);
        const sprite = new PIXI.Sprite(texture);
        sprite.anchor.set(0.5);
        sprite.position.set(x, y);
        sprite.width = w;
        sprite.height = h;
        this.app.stage.addChild(sprite);
        return sprite;
    }

    deleteThisNephew(child) {
        this.app.stage.removeChild(child);
    }

    text(text, x, y) {
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