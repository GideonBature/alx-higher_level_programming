#!/usr/bin/node

const dict = require('./101-data.js').dict;

const occurenceDict = {};

for (const [userID, occurenceCount] of Object.entries(dict)) {
  if (!occurenceDict[occurenceCount]) {
    occurenceDict[occurenceCount] = [];
  }
  occurenceDict[occurenceCount].push(userID);
}
console.log(occurenceDict);
