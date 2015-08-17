#!/bin/bash
join -a1 -e\"NULL\" -o1.3 1.4 1.2 1.1 2.2 2.3 1.5 1.6  <(join -e\"NULL\" -a1 -o1.2 2.2 1.3 1.4 1.5 1.6 <(sort -k1 event_audio_name_class.index) device_addr.index|sort -k1) member_year_gender.index > event_addr_year_gender.index
