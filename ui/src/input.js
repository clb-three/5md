import log from "./log";
import * as socket from "./socket";

var initialized;

export function initialize() {
  if (initialized !== undefined) return;
  initialized = true;
  log.initialized("input");

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
initialize();
