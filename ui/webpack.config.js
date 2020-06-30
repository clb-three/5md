const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
  devtool: "source-map",
  output: {
    filename: "main.js",
  },
  plugins: [
    new CopyWebpackPlugin({
      patterns: [
        {
          from: "./*.html",
        },
        {
          from: "./images/*",
        },
      ],
    }),
  ],
};
