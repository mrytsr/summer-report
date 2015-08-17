cat ./dataset/0813/appshare_log.aps_data_eventlog.csv.esc |awk -F'","' '$6=="click_download"' > /dev/shm/aps_data_eventlog_download.csv
