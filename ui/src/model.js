import * as display from "./display";

let name = "benji";
let cardDisplay = {};
let deckDisplay;
let x = 100;

function wireUpDisplay(state) {
  const hero = state.heroes[name];

  cardDisplay = {};
  for (const card of hero.hand) {
    loadCard(card);
  }

  deck(hero.deck.length);
}

export function loadCard(card) {
  cardDisplay[card.uuid] = display.load_card(card.symbol, x, 100);
  x += 60;
}

export function discardCard(card) {
  display.deleteThisNephew(cardDisplay[card.uuid]);
  delete cardDisplay[card.uuid];
}

export function deck(numCards) {
  if (!deckDisplay) {
    deckDisplay = display.load_deck(numCards, 100, 300);
  }
  deckDisplay.numCards.text = numCards;
}

export function init(state) {
  console.log("initialize state", state);

  wireUpDisplay(state);
}
