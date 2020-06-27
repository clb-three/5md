const CopyWebpackPlugin = require("copy-webpack-plugin");

module.exports = {
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
