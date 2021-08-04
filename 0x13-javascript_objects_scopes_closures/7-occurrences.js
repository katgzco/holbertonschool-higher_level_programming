#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let Ocurrence = 0;
  for (const x of list) {
    if (searchElement === x) {
      Ocurrence++;
    }
  }
  return (Ocurrence);
};
