#!/bin/bash

ENDPOINT="35.238.226.140:3001/AMZN"

function stock_data {
    # company = ($QUERY_STRING)
    query="${ENDPOINT}"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
echo
stock_data