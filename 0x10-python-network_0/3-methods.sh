#!/bin/bash
# displays the methods accepted
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
