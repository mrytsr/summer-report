#!/bin/bash
awk -F'","' '{arr[$3]=0}END{for(i in arr){print "\""i"\""}}' dataset/0813/appshare_log.aps_data_eventlog.csv.esc |sort > devices.index
