var express = require("express");

var todo = express.Router();

todo.get('/', function(_, res) {
  res.send('Hello from todo root route.');
});

todo.get('/users', function(_, res) {
  res.send('List of todo users.');
});

// this is where we're renaming the router to something noticeable and exporting it
let TodoRouter = todo;
module.exports = TodoRouter;