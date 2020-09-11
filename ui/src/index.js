// debug
function initializeDebugElements() {
    const input = document.createElement("input");
    input.placeholder = "Enter command here";
    document.body.appendChild(input);

    const submit = document.createElement("button");
    submit.innerHTML = "Send";
    submit.addEventListener("click", function () {
        socket.emit("command", input.value);
        input.value = "";
    });
    document.body.appendChild(submit);
}

initializeDebugElements();


// socket

let socket;

function initializeSocket(eventHandler) {
    if (socket !== undefined) return;
    socket = io.connect();

    // Initial connection
    socket.on("connect", function () {
        console.log("connected");
        socket.emit("hello", "I'm connected!");
    });
    // Initialization
    socket.on("hello", function (msg) {
        console.log("hello!", msg);
    });
    // Normal logging messages
    socket.on("message", function (msg) {
        console.log("got a message:", msg);
    });
    // Game event to apply to our model
    socket.on("gameevent", function (msg) {
        // console.log("got game event:", event);
        const events = JSON.parse(msg);
        for (const event of events) {
            eventHandler(event);
        }
    });

    // Handle various errors in the same way
    socket.on("connect_error", handleErrors);
    socket.on("connect_failed", handleErrors);
    socket.on("disconnect", handleErrors);

    // Request the current state from the server
    socket.emit("command", "getstate");
}

function handleErrors(err) {
    console.error("do something about this!", err);
}

// Apply gameevent to the model
function doEvent(event) {
    console.log("event", event);
    switch (event.code) {
        case "state":
            initializeModel(event.obj);
            break;
        case "cardsleft":
            deck(event.obj);
            break;
        case "drawcard":
            loadCard(event.obj[1]);
            break;
        case "playcard":
            discardCard(event.obj[1]);
            break;
        case "enemy":
            target(event.obj);
            break;
        case "hurt":
            targetSymbols(event.obj);
            break;
        default:
            console.log("unhandled");
            break;
    }
}

initializeSocket(doEvent);

// display
import * as PIXI from "pixi.js";
import io from "socket.io-client";

let app;

function initializeDisplay() {
    if (app !== undefined) return;
    app = new PIXI.Application({
        width: 800,
        height: 600,
    });

    document.body.appendChild(app.view);
}

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

function load_target(type, symbols, x, y) {
    const target = sprite(`images/badguy.png`, x, y, 100, 160);
    const targetType = text(type, x, y);
    const targetSymbols = text(symbols, x, y + 50);
    return {
        target,
        targetType,
        targetSymbols,
    };
}

function deleteThisNephew(child) {
    app.stage.removeChild(child);
}

function load_card(name, x, y) {
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

function load_deck(num_cards, x, y) {
    const deck = sprite(`images/back.png`, x, y, 100, 160);

    deck.interactive = true;

    function onDown() {
        emit("command", `benji draw`);
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


// model
let name = "benji";
let cardDisplay = {};
let deckDisplay;
let targetDisplay;
let x = 100;

function wireUpDisplay(state) {
    const hero = state.heroes[name];

    for (const card of hero.hand) {
        discardCard(card);
    }
    cardDisplay = {};
    for (const card of hero.hand) {
        loadCard(card);
    }

    deck(hero.deck.length);

    target(state.target);
}

function target(enemy) {
    if (targetDisplay) {
        deleteThisNephew(targetDisplay.target);
        deleteThisNephew(targetDisplay.targetType);
        deleteThisNephew(targetDisplay.targetSymbols);
    }

    targetDisplay = load_target(enemy.type, enemy.symbols, 300, 300);
}

function targetSymbols(symbols) {
    targetDisplay.targetSymbols.text = symbols;
}

function loadCard(card) {
    cardDisplay[card.uuid] = load_card(card.symbol, x, 100);
    x += 60;
}

function discardCard(card) {
    deleteThisNephew(cardDisplay[card.uuid]);
    delete cardDisplay[card.uuid];
}

function deck(numCards) {
    if (!deckDisplay) {
        deckDisplay = load_deck(numCards, 100, 300);
    }
    deckDisplay.numCards.text = numCards;
}

function initializeModel(state) {
    console.log("initialize state", state);

    wireUpDisplay(state);
}

initializeDisplay();
initializeSocket();
initializeModel();
