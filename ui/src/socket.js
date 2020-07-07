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

function doEvent(event) {
  switch (event.code) {
    default:
      console.log("unhandled event", event);
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
