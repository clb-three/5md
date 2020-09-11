// debug
import {Model} from "./Model";
import {initializeSocket, socket} from "./socket";

// display

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

