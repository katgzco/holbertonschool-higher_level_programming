#!/usr/bin/node
exports.converter = function (base) {
  return function (numberToConvert) {
    return parseInt(numberToConvert, 10).toString(base);
  };
};
