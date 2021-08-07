const webpack = require('webpack');
const path              = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const resolve = dir => path.join(__dirname, '../../', dir);

const env = process.env.NODE_ENV || 'development';
const isDev = env === 'development';

const WebpackDefinePluginConfig = new webpack.DefinePlugin({
  'process.env': {
    NODE_ENV: JSON.stringify(env),
  },
});

const HtmlWebpackPluginConfig = new HtmlWebpackPlugin({
  template: resolve('website/index.html'),
  favicon: resolve('website/assets/icons/favicon.ico'),
  filename: 'index.html',
  inject: 'body',
});

const CleanWebpackPluginConfig = new CleanWebpackPlugin({
  verbose: true,
  cleanStaleWebpackAssets: false,
});

module.exports = {
  devtool: 'source-map',
  entry: [
    resolve('website/styles/index.scss'),
    resolve('website/assets/index.js'),
    resolve('website/index.js'),
  ],
  output: {
    filename: isDev ? '[name].js' : '[name].[hash].js',
    path: resolve('dist'),
    publicPath: '/',
  },
  resolve: {
    alias: {
      _client: resolve('website'),
      _assets: resolve('website/assets/'),
      _styles: resolve('website/styles/'),
      _utils: resolve('website/utils/'),
      _api: resolve('website/api/'),
      _hooks: resolve('website/hooks/'),
      _atoms: resolve('website/components/atoms/'),
      _molecules: resolve('website/components/molecules/'),
      _organisms: resolve('website/components/organisms/'),
      _templates: resolve('website/components/templates/'),
      _pages: resolve('website/components/pages/'),
      _environment: resolve('website/components/environment/'),
      _store: resolve('website/store/'),
      _actions: resolve('website/store/actions/'),
      _reducers: resolve('website/store/reducers/'),
      _thunks: resolve('website/store/thunks/'),
    },
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        include: [resolve('website')],
      },
      {
        test: /\.css$/,
        use: [isDev ? 'style-loader' : MiniCssExtractPlugin.loader, 'css-loader'],
      },
      {
        test: /\.scss$/,
        use: [isDev ? 'style-loader' : MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
      },
      {
        test: /\.less$/,
        use: [isDev ? 'style-loader' : MiniCssExtractPlugin.loader, 'css-loader', 'less-loader'],
      },
      {
        test: /\.(jpe?g|png|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'images/[name].[ext]',
            },
          },
        ],
      },
      {
        test: /\.svg(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'file-loader',
        options: { name: 'icons/[name].[ext]' },
      },
      {
        test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader',
        options: {
          name: 'fonts/[name].[ext]',
          limit: 8192,
          mimetype: 'application/font-woff',
        },
      },
      {
        test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'file-loader',
        options: { name: 'fonts/[name].[ext]' },
      },
    ],
  },
  plugins: [
    HtmlWebpackPluginConfig,
    WebpackDefinePluginConfig,
    CleanWebpackPluginConfig,
  ],
  performance: {
    hints: false,
  },
};
