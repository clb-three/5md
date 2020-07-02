import io from "socket.io-client";
import log from "./log";

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
}
initialize();

function handleErrors(err) {
  console.error("do something about this!", err);
}

function doInf(text) {
  const split = text.split(/\s+/);
  switch (split[0]) {
    case "playcard":
      const player = split[1];
      const verb = split[2];
      const card = split[3];
      const effect = split.slice(4);
      console.log(player, verb, card, effect);
      break;
    default:
      console.log("didnt know that one", text);
      break;
  }
}

function doEvent(eventText) {
  const commandSplit = eventText.split(/([^ ]+)\s+(.+)/);
  const type = commandSplit[1];
  const rest = commandSplit[2];

  switch (type) {
    case "err":
      console.error("eroeororroror", rest);
      break;
    case "inf":
      doInf(rest);
      break;
    case "state":
      console.log("Getting state", rest);
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
  socket.on("gameevent", function (event) {
    // console.log("got game event:", event);
    doEvent(event);
  });
}

function wire_up_errors(socket) {
  socket.on("connect_error", handleErrors);
  socket.on("connect_failed", handleErrors);
  socket.on("disconnect", handleErrors);
}
