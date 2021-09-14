#!/usr/bin/node

/* Write a script that computes the number of
tasks completed by user id. */

const url = process.argv[2];
const request = require('request');
const completedTask = Object();

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        if (!completedTask[task.userId]) {
          completedTask[task.userId] = 1;
        } else {
          completedTask[task.userId] = completedTask[task.userId] + 1;
        }
      }
    }
  }
  console.log(completedTask);
});
