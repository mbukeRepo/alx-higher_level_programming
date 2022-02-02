#!/usr/bin/node

const request = require('request');
let count = 0;
let results = null;
request(process.argv[2], (err, res, body) => {
  if (!err) {
    results = JSON.parse(body).results;
    count = results.reduce((c, movie) => {
      return movie.characters.find(c => c.endsWith('/18/'))
        ? c + 1
        : c;
    }, 0);
    console.log(count);
  }
});
