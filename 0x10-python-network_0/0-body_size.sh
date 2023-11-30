#!/bin/bash
# displays size of body of response
curl -s "$1" | wc -c
