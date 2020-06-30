function handleErrors(err) {
  console.error("do something about this!", err);
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
    console.log("got game event:", event);
  });
}

function wire_up_errors(socket) {
  socket.on("connect_error", handleErrors);
  socket.on("connect_failed", handleErrors);
  socket.on("disconnect", handleErrors);
}

const socket = io.connect();

// Initialize the socket
export function initialize() {
  wire_up_events(socket);
  wire_up_errors(socket);
}

export function emit(name, message) {
  socket.emit(name, message);
}
