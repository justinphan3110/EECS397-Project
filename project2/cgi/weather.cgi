#!/bin/bash

ENDPOINT="35.238.226.140:3001/AMZN"
#QUERY_STRING="city=cleveland&state=ohio"


function query_map {
    saveIFS=$IFS
    IFS='=&'
    query=($QUERY_STRING)
    IFS=$saveIFS

    declare -A query_map
    for ((i=0; i<${#query[@]}; i+=2))
    do
        query_map[${query[i]}]=${query[i+1]}
    done
    echo ${query_map[@]}
}

function join_by { local IFS="$1"; shift; echo "$*"; }

function weather_data {
    query="${ENDPOINT}"
    echo $(curl -sS $query)
}

echo "Content-Type: application/json"
echo
weather_data