const path = require("path");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  devtool: "inline-source-map",
  mode: "development",
  output: {
    filename: "[name].[contenthash].js",
    path: path.resolve(__dirname, "dist"),
  },
  performance: {
    hints: false,
    maxEntrypointSize: 512000,
    maxAssetSize: 512000,
  },
  plugins: [
    new CopyWebpackPlugin({
      patterns: [
        {
          from: "./images/*",
        },
      ],
    }),
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: "Output Management",
    }),
  ],
};
