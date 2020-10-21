import * as io from "socket.io-client";
import * as loglevel from "loglevel";

const log = loglevel.getLogger("root::socket");

export let socket;
const SERVER_URI = 'localhost:8080';

export function initializeSocket(eventHandler): void {
    log.debug(`connecting to the server ${SERVER_URI}`);

    if (socket !== undefined) return;
    socket = io.connect(SERVER_URI);

    // Initial connection
    socket.on("connect", function () {
        log.info("connected to the server, sending handshake...");
        socket.emit("hello");
    });
    // Normal logging messages
    socket.on("message", function (msg) {
        log.info(`[MSG] ${msg}`);
    });
    // Game event to apply to our model
    socket.on("gameevent", function (msg) {
        log.debug(`event message "${msg}"`);
        const event = JSON.parse(msg);
        log.info("[EVT]", event);
        eventHandler(event);
    });

    // Handle various errors in the same way
    socket.on("connect_error", handleErrors);
    socket.on("connect_failed", handleErrors);
    socket.on("disconnect", handleErrors);

    log.debug("done wiring up events");
}

function handleErrors(err): void {
    console.error("do something about this!", err);
}