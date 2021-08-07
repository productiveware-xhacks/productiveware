const express = require("express");
const app = express();

// port the server will be listening on
const port = 3000;

// importing the routers into the file
const TodoRouter = require("./src/routes/todo");
const SettingsRouter = require("./src/routes/settings");

// this is the base of the route of the api
const apiBaseRoute = "/api"

app.use(apiBaseRoute + "/todo", TodoRouter);
app.use(apiBaseRoute + "/settings", SettingsRouter);

app.get("/", (_, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
    console.log(`App running and listening on port ${port}`);
    console.log("Valid routes: ")
});
