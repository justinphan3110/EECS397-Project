#!/bin/bash

ENDPOINT="http://35.238.226.140:3001/FB"

function stock_data {
    query = "${ENDPOINT}"
    echo $(curl $query)
}

echo
stock_data