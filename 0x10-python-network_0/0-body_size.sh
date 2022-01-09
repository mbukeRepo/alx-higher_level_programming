#!/usr/bin/env bash
# takes url as arg curl it and print the length of the res
curl $1 | wc -c
