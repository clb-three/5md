import io from "socket.io-client";
import log from "./log";
import * as model from "./model";

export function emit(name, message) {
  socket.emit(name, message);
}

var socket;

// Initialize the socket
export function initialize() {
  if (socket !== undefined) return;
  socket = io.connect();
  log.initialized("socket");

  wire_up_events(socket);
  wire_up_errors(socket);
  socket.emit("command", "getstate");
}
initialize();

function handleErrors(err) {
  console.error("do something about this!", err);
}

function doEvent(event) {
  console.log("event", event);
  switch (event.code) {
    case "state":
      model.init(event.obj);
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

function wire_up_events(socket) {
  socket.on("connect", function () {
    console.log("connected");
    socket.emit("hello", "I'm connected!");
  });
  socket.on("message", function (msg) {
    console.log("got a message:", msg);
  });
  socket.on("hello", function (msg) {
    console.log("hello!", msg);
  });
  socket.on("gameevent", function (msg) {
    // console.log("got game event:", event);
    const events = JSON.parse(msg);
    for (const event of events) {
      doEvent(event);
    }
  });
}

function wire_up_errors(socket) {
  socket.on("connect_error", handleErrors);
  socket.on("connect_failed", handleErrors);
  socket.on("disconnect", handleErrors);
}
