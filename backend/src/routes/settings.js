var express = require("express");

var settings = express.Router();

settings.get('/', function(_, res) {
  res.send('Hello from settings root route.');
});

settings.get('/users', function(_, res) {
  res.send('List of settings users.');
});

// this is where we're renaming the router to something noticeable and exporting it
let SettingsRouter = settings;
module.exports = SettingsRouter