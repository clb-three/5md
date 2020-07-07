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

export function load_card(name, x, y) {
  // load the texture we need
  const texture = PIXI.Texture.from(`images/${name}.png`);
  const card = new PIXI.Sprite(texture);
  card.anchor.set(0.5);
  card.position.set(x, y);
  card.width = 100;
  card.height = 160;
  app.stage.addChild(card);
  card.interactive = true;

  function onDown(cardName) {
    socket.emit("command", `benji play ${cardName}`);
  }
  card.on("mousedown", () => onDown(name));
  card.on("touchstart", () => onDown(name));
  return card;
}

export function load_deck(num_cards, x, y) {
  // load the texture we need
  const texture = PIXI.Texture.from(`images/back.png`);
  const deck = new PIXI.Sprite(texture);
  deck.anchor.set(0.5);
  deck.position.set(x, y);
  deck.width = 100;
  deck.height = 160;
  deck.interactive = true;

  function onDown() {
    socket.emit("command", `benji draw`);
  }
  deck.on("mousedown", () => onDown(name));
  deck.on("touchstart", () => onDown(name));
  app.stage.addChild(deck);

  const numCards = new PIXI.Text(num_cards, {
    font: "35px Snippet",
    fill: "white",
    align: "left",
  });
  numCards.anchor.set(0.5);
  numCards.position.set(x, y);
  app.stage.addChild(numCards);

  return {
    deck,
    numCards,
  };
}
