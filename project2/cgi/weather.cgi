#!/bin/bash

ENDPOINT="35.238.226.140:3001/AMZN"

function weather_data {
    query="${ENDPOINT}"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
echo
weather_data