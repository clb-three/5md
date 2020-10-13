const {FuseBox, WebIndexPlugin, Sparky} = require("fuse-box");
const {task, src, context} = require("fuse-box/sparky");

const fuse = FuseBox.init({
    homeDir: "src",
    target: "browser@es6",
    output: "dist/$name.js",
    plugins: [
        WebIndexPlugin(),
    ],
    debug: true,
});

const config = fuse
    .bundle("app")
    .sourceMaps(true)
    .instructions(" > index.js");

Sparky.task("copy-favicon", () => {
    return Sparky.src("favicon.ico", {base: "./resources"})
        .dest("dist")
        .exec();
});
Sparky.task("copy-images", () => {
    return Sparky.watch("**/*.+(svg|png|jpg|gif)", {base: "./resources/images"})
        .dest("dist/images")
        .exec();
});
Sparky.task("copy-assets", ["&copy-images", "&copy-favicon"]);
Sparky.task("run", ["copy-assets"], () => {
    return fuse.run();
});
Sparky.task("watch", () => {
    fuse.dev();
    config
        .watch('src/**')
        .hmr();
    return Sparky.exec("run");
});
Sparky.task("build", () => {
    return Sparky.exec("run");
});
Sparky.task("default", ["build"]);
