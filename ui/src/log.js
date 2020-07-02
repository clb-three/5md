function now() {
  return new Date().toLocaleString("en-US");
}

function initialized(module) {
  console.log(`${now()} initialized ${module}`);
}

export default { initialized };
