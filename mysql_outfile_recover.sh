#!/bin/bash
scp s3:mysql_outfile/appshare.aps_audio.esc.gz .
scp s3:mysql_outfile/appshare.aps_audio.struct .
gunzip appshare.aps_audio.esc.gz
mysql -uroot appshare -e "truncate aps_audio"
mysql -uroot appshare < appshare.aps_audio.struct
mysql -uroot appshare -e "load data local infile '/home/tjx/idaddy-summer-report/appshare.aps_audio.csv.esc' into table aps_audio character set utf8 FIELDS TERMINATED BY ',' ENCLOSED BY '\\\"'"

mysql -uroot appshare -e "select * from aps_audio limit 10\G "
