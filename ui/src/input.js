let socket;

export function initialize(sock) {
  socket = sock;
  const input = document.getElementById("command");
  const submit = document.getElementById("submit-command");
  submit.addEventListener("click", function () {
    socket.emit("command", input.value);
    input.value = "";
  });
}
