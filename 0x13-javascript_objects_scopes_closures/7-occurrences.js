#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  list.forEach(el => {
    if (el === searchElement) occurence++;
  });
  return occurence;
};
