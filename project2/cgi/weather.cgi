#!/bin/bash

ENDPOINT="35.238.226.140:3001/AMZN"
#QUERY_STRING="city=cleveland&state=ohio"

function weather_data {
    query="${ENDPOINT}"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
weather_data