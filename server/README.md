# Setting up the backend

First you need to install MongoDB on your system, you can do that by following the instructions [here](https://docs.mongodb.com/manual/installation/)

## Database

1. Create a database named "productiveware"
1. Create a user named "server" with password "server" with roles:

```json
roles: [{
    role: "readWrite",
    db: "productiveware"
  }]
```

## Note

This mongodb URL is stored in `server/config/environment.js` under the variable `process.env.DATABASE_URL`
