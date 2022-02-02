#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const options = { encoded: 'utf-8' };
request(process.argv[2], (err, res, body) => {
  if (!err) {
    fs.writeFile(process.argv[3], body, options);
  }
});
