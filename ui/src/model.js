import * as display from "./display";

let name = "benji";
let cardDisplay;
let deckDisplay;
let x = 100;

function wireUpDisplay(state) {
  const hero = state.heroes[name];

  cardDisplay = [];
  for (const card of hero.hand) {
    loadCard(card);
  }

  deck(hero.deck.length);
}

export function loadCard(card) {
  cardDisplay.push(display.load_card(card.symbol, x, 100));
  x += 40;
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
