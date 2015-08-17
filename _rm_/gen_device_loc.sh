#!/bin/bash
# awk '{print "ag",$1,"../../dataset/aps_device_location.uniqdevice"}' devices.list|sed 's/ "/ "^/;s/" /$" /' |bash> ./device_loc.list

# awk -F'","' '{printf "%s %.1f_%.1f\n",$1,$3,$4}' aps_device_location.csv.esc|sed 's/^"//' > device_loc.index

cat ./dataset/0813/appshare.aps_device_location.csv.esc |awk -F'","' '{month=substr($6,1,7);if("2015-05"==month||"2015-06"==month||"2015-07"==month||"2015-08"==month){printf "%s %.1f_%.1f\n",$1,$3,$4}}' |sed 's/^"//' |awk '{arr[$1]="\""$2"\""}END{for(i in arr){print "\""i"\"",arr[i]}}'|sort > device_loc.index

