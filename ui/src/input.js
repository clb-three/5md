let socket;

export function initialize(sock) {
  socket = sock;

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
