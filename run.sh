#!/bin/bash


for date in `seq 09 26`;
do
    python3 elk_parser.py -f ~/log/202107$date.json
done
