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

function sprite(resource, x, y, w, h) {
  const texture = PIXI.Texture.from(resource);
  const sprite = new PIXI.Sprite(texture);
  sprite.anchor.set(0.5);
  sprite.position.set(x, y);
  sprite.width = w;
  sprite.height = h;
  app.stage.addChild(sprite);
  return sprite;
}

export function load_target(type, symbols, x, y) {
  const target = sprite(`images/badguy.png`, x, y, 100, 160);
  const targetType = text(type, x, y);
  const targetSymbols = text(symbols, x, y + 50);
  return {
    target,
    targetType,
    targetSymbols,
  };
}

export function deleteThisNephew(child) {
  app.stage.removeChild(child);
}

export function load_card(name, x, y) {
  // load the texture we need
  const card = sprite(`images/${name}.png`, x, y, 100, 160);

  card.interactive = true;
  function onDown(cardName) {
    socket.emit("command", `benji play ${cardName}`);
  }
  card.on("mousedown", () => onDown(name));
  card.on("touchstart", () => onDown(name));
  return card;
}

function text(text, x, y) {
  const numCards = new PIXI.Text(text, {
    font: "35px Snippet",
    fill: "white",
    align: "left",
  });
  numCards.anchor.set(0.5);
  numCards.position.set(x, y);
  app.stage.addChild(numCards);
  return numCards;
}

export function load_deck(num_cards, x, y) {
  const deck = sprite(`images/back.png`, x, y, 100, 160);

  deck.interactive = true;
  function onDown() {
    socket.emit("command", `benji draw`);
  }
  deck.on("mousedown", () => onDown(name));
  deck.on("touchstart", () => onDown(name));
  app.stage.addChild(deck);

  const numCards = text(num_cards, x, y);

  return {
    deck,
    numCards,
  };
}
