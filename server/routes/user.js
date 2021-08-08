const express = require('express');
const bcrypt = require('bcryptjs');
const { requireAuth } = require('./middleware');
const { User } = require('../database/schemas');

const router = express.Router();

module.exports = router;

router.get('/', (req, res) => {
  const user = (req.user && req.user.hidePassword()) || {};

  res.send({ message: 'User info successfully retreived', user });
});

router.get('/encryptkey', (req, res) => {  
  User.find({ user: req.user.id }, { __v: 0, user: 0 }, (err, user) => {
    if (err) {
      res.status(400).send({ message: 'Get users failed', err });
    } else {
      res.send({ message: 'Retreived encryption key', encrypt_key: user.encrypt_key });
    }
  });
});

router.put('/encryptkey', requireAuth, (req, res) => {
  const { newKey } = req.body;

  User.findByIdAndUpdate({ _id: req.user._id }, { encrypt_key: newKey }, (err, user) => {
    if (err) {
      res.status(400).send({ err, message: 'Error updating encryption key' });
    }
    res.status(200).send({ message: 'Encryption key successfully updated', user: user.hidePassword() });
  });
});

router.put('/password', requireAuth, (req, res) => {
  const { oldPassword, newPassword } = req.body;

  if (req.user.validPassword(oldPassword)) {
    bcrypt.genSalt(10, (err, salt) => {
      if (err) {
        res.status(400).send({ err, message: 'Error updating password' });
      }
      bcrypt.hash(newPassword, salt, (err, hash) => {
        if (err) {
          res.status(400).send({ err, message: 'Error updating password' });
        }
        User.findByIdAndUpdate({ _id: req.user._id }, { password: hash }, err => {
          if (err) {
            res.status(400).send({ err, message: 'Error updating password' });
          }
          res.status(200).send({ message: 'Password successfully updated' });
        });
      });
    });
  } else {
    res.status(400).send({ message: 'Old password did not match' });
  }
});

router.put('/', requireAuth, (req, res) => {
  req.body.updated_at = Date.now();

  User.findByIdAndUpdate({ _id: req.user._id }, req.body, { new: true }, (err, user) => {
    if (err) {
      res.status(400).send({ err, message: 'Error updating user' });
    }
    res.status(200).send({ message: 'User successfully updated', user: user.hidePassword() });
  });
});
