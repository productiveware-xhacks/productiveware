export NODE_ENV=production

webpack --mode=production --config ./website/config/webpack.prd.config.js

unset NODE_ENV
