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
let model;

function doEvent(event) {
    console.log("event", event);
    switch (event.code) {
        case "state":
            model = new Model(event.obj);
            break;
        case "cardsleft":
            model.deck(event.obj);
            break;
        case "drawcard":
            model.loadCard(event.obj[1]);
            break;
        case "playcard":
            model.discardCard(event.obj[1]);
            break;
        case "enemy":
            model.target(event.obj);
            break;
        case "hurt":
            model.targetSymbols(event.obj);
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

function deleteThisNephew(child) {
    app.stage.removeChild(child);
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


// model
class Model {
    constructor(state) {
        this.name = "benji"; // TODO: Auth story: get a real name
        this.x = 100;

        const hero = state.heroes[name];

        for (const card of hero.hand) {
            this.discardCard(card);
        }
        this.cardDisplay = {};
        for (const card of hero.hand) {
            this.loadCard(card);
        }

        this.deck(hero.deck.length);

        this.target(state.target);
    }

    target(enemy) {
        if (this.targetDisplay) {
            deleteThisNephew(this.targetDisplay.target);
            deleteThisNephew(this.targetDisplay.targetType);
            deleteThisNephew(this.targetDisplay.targetSymbols);
        }

        const x = 300;
        const y = 300;
        const target = sprite(`images/badguy.png`, x, y, 100, 160);
        const targetType = text(enemy.type, x, y);
        const targetSymbols = text(enemy.symbols, x, y + 50);
        this.targetDisplay = {
            target,
            targetType,
            targetSymbols,
        };
    }

    targetSymbols(symbols) {
        this.targetDisplay.targetSymbols.text = symbols;
    }

    loadCard(card) {
        const name = card.symbol;
        const x = this.x;
        const y = 100;

        // load the texture we need
        const cardDisplay = sprite(`images/${name}.png`, x, y, 100, 160);

        cardDisplay.interactive = true;

        function onDown(cardName) {
            socket.emit("command", `benji play ${cardName}`);
        }

        cardDisplay.on("mousedown", () => onDown(name));
        cardDisplay.on("touchstart", () => onDown(name));
        this.cardDisplay[card.uuid] = cardDisplay;
        this.x += 60;
    }

    discardCard(card) {
        deleteThisNephew(this.cardDisplay[card.uuid]);
        delete this.cardDisplay[card.uuid];
    }

    deck(numCards) {
        if (!this.deckDisplay) {
            const x = 100;
            const y = 300;

            const deck = sprite(`images/back.png`, x, y, 100, 160);

            deck.interactive = true;

            function onDown() {
                emit("command", `benji draw`);
            }

            deck.on("mousedown", () => onDown(name));
            deck.on("touchstart", () => onDown(name));
            app.stage.addChild(deck);

            const numCardsDisplay = text(numCards, x, y);
            numCardsDisplay.text = numCards;

            this.deckDisplay = {
                deck,
                numCards: numCardsDisplay,
            };
        }
    }
}

initializeDisplay();
initializeSocket();
