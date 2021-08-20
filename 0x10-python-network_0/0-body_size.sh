#!/bin/bash
#displays the size of the body of the response
curl -Is "$1" | awk '/Content-Length:/ {print $2}'
