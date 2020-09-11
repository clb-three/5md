import io from "socket.io-client";

export let socket;

export function initializeSocket(eventHandler) {
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