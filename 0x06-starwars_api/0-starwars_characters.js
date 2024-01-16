#!/usr/local/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieEndPoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function makeRequest(characterList, index) {
    if (characterList.length === index) {
        return;
    }

    request(characterList[index], (error, response, body) => {
        if (error) {
            console.log(error);
        } else {
            console.log(JSON.parse(body).name);
            makeRequest(characterList, index + 1);
        }
    });
}

request(movieEndPoint, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const characterList = JSON.parse(body).characters;
        makeRequest(characterList, 0);
    }
});