#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error('error:', err);
  }

  const characters = JSON.parse(body).characters;
  let names = [];
  for (const i of [...characters]) {
    request(i, (err, res, bod) => {
      if (err) {
        console.error('error:', err);
      }
      names.push(JSON.parse(bod));
      if (names.length === characters.length) {
        names = names.sort((a, b) => {
          a = +a.url.split('/').slice(5)[0];
          b = +b.url.split('/').slice(5)[0];
          if (a > b) {
            return 1;
          }
          if (a < b) {
            return -1;
          }
          return 0;
        });
        for (const i of [...names]) {
          console.log(i.name);
        }
      }
    });
  }
});
