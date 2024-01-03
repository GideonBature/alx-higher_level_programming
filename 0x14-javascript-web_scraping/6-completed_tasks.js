#!/usr/bin/node
// a script that computes the number of
// tasks completed by user id.
const process = require('process');
const request = require('request');

const url = process.argv[2];
const completedTasksByUserId = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    for (const task of data) {
      if (task.completed) {
        completedTasksByUserId[task.userId] = (completedTasksByUserId[task.userId] || 0) + 1;
      }
    }
    console.log(completedTasksByUserId);
  }
});
