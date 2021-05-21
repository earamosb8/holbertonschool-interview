#!/usr/bin/node

let request = require('request');

async function sw (id) {
  let url = `https://swapi-api.hbtn.io/api/films/${id}`;

  request(url, async function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      for (let ch of JSON.parse(body).characters) {
        let ret = () => {
          return new Promise((resolve, reject) => {
            request(ch, function (err, response, body) {
              if (err) {
                console.log(err);
              } else {
                resolve(JSON.parse(body).name);
              }
            });
          });
        };
        console.log(await ret());
      }
    }
  });
}

if (process.argv.length === 3) {
  sw(process.argv[2]);
}
