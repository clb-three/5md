import * as io from "socket.io-client";

export let socket;

export function initializeSocket(eventHandler) {
    if (socket !== undefined) return;
    socket = io.connect('localhost:8080');

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
        const event = JSON.parse(msg);
        eventHandler(event);
    });

    // Handle various errors in the same way
    socket.on("connect_error", handleErrors);
    socket.on("connect_failed", handleErrors);
    socket.on("disconnect", handleErrors);

    // Request the current state from the server
    socket.emit("getstate");
}

function handleErrors(err) {
    console.error("do something about this!", err);
}