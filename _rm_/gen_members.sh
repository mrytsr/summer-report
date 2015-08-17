cat ./dataset/aps_data_eventlog.csv.esc |awk -F',' '{if($4 != "\"0\"" && $6=="\"click_download\""){print $3,$4,$9,$13}}' |sort> ./shm/aps_data_eventlog_members.csv
