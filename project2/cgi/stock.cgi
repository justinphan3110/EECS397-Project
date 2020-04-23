#!/bin/bash

ENDPOINT="35.238.226.140:3001/"

function stock_data {
    q=($QUERY_STRING)
    query="${ENDPOINT}$q"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
echo "Access-Control-Allow-Origin: *"
echo
stock_data