import * as PIXI from "pixi.js";
import log from "./log";
import * as socket from "./socket";

var app;

// Initialize the display
export function initialize() {
  if (app !== undefined) return;
  app = new PIXI.Application({
    width: 800,
    height: 600,
  });
  log.initialized("display");

  document.body.appendChild(app.view);
}
initialize();

function onDown(cardName) {
  socket.emit("command", `benji play ${cardName}`);
}

export function load_cards() {
  // load the texture we need
  app.loader
    .add("scroll", `images/scroll.png`)
    .add("jump", `images/jump.png`)
    .add("arrow", `images/arrow.png`)
    .add("shield", `images/shield.png`)
    .add("sword", `images/sword.png`)
    .load((_, resources) => {
      let x = 20;
      for (const n of ["scroll", "jump", "arrow", "shield", "sword"]) {
        const card = new PIXI.Sprite(resources[n].texture);
        card.x = x;
        x += 110;
        card.y = 200;
        card.width = 100;
        card.height = 160;
        app.stage.addChild(card);

        card.interactive = true;
        card.on("mousedown", () => onDown(n));
        card.on("touchstart", () => onDown(n));
      }
    });
}
