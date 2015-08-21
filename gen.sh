#!/bin/bash

# 1. gen device_addr
cat ./dataset/0813/appshare.aps_device_location.csv.esc |awk -F'","' '{month=substr($6,1,7);if("2015-05"==month||"2015-06"==month||"2015-07"==month||"2015-08"==month){printf "%s %.1f_%.1f\n",$1,$3,$4}}' |sed 's/^"//' |awk '{arr[$1]="\""$2"\""}END{for(i in arr){print "\""i"\"",arr[i]}}'|sort > device_loc.index
join -o 1.1 2.2 -1 2 <(sort -k2 device_loc.index) dataset/loc_addr.index |sort > device_addr.index

# 1. gen member_year_gender 
awk -F'","' '{if($5>1999&&$5<2015&&$4!="宝贝"&&$4!=""&&$4~/^[^(0-9a-zA-Z.!¥]+$/){if($9==1||$9==2){printf "\"%s\" \"%s\" \"%s\"\n",$2,$5,$9}}}' ./dataset/0813/appshare.aps_kids.csv.esc|sort -k1> member_year_gender.index

# 1. gen play

# 1. gen download
cat ./dataset/0813/appshare_log.aps_data_eventlog.csv.esc |awk -F',' '{if($6=="\"click_download\""){print $3,$4,$9,$13}}' |sort> ./shm/download.csv

# 1. gen order
cat ./dataset/appshare.aps_biz_order.csv.esc |awk -F',' '{if($4!="\"12个月VIP会员\""&&$4!="\"充值\"")print $30,$27,$5,$33}' > ./shm/order.csv

# 1. gen audio_name_taxo
awk -F'","' '{gsub(/ /,"-",$3); printf "%s\" \"%s\" \"%s\"\n",$1,$3,$37}' dataset/appshare.aps_audio.csv.esc |sort> audio_name_taxo.index

# 1. gen device_model.index
cat dataset/appshare.aps_device.csv.esc |awk -F'","' '{gsub(/ /,"-",$3); gsub(/ /,"-",$4); printf "\"%s\" \"%s,%s,%s,%s\"\n",$6,$3,$4,$8,$9}' |sort -k1 > device_model.index

# 2. gen event_audio
join -o1.1 1.2 1.4 1.5 2.2 2.3 --nocheck-order -13 <(cat ./shm/download.csv|sort -k3) audio_name_taxo.index |sort -k1 > event_audio.index

# 3 gen order.index
join --nocheck-order -a1 -e\"NULL\" -o1.2 1.3 1.4 1.5 2.2 2.3 <(join --nocheck-order -a1 -e\"NULL\" -o 1.2 1.3 1.4 1.5 2.2 <(cat ./shm/order.csv|sort -k1) device_addr.index|sort -k1) member_year_gender.index > order.index

# 3. gen download.index
join -a1 -e\"NULL\" -o1.3 1.4 1.2 1.1 2.2 2.3 1.5 1.6 1.7 <(join -e\"NULL\" -a1 -o1.2 1.3 1.4 1.5 1.6 1.7 2.2 <(join -e\"NULL\" -a1 -o1.1 1.2 2.2 1.3 1.4 1.5 1.6 event_audio.index device_addr.index) device_model.index|sort -k1) member_year_gender.index > download.index
