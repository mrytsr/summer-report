#!/bin/bash
join -o1.1 1.2 1.4 1.5 2.2 2.3 --nocheck-order -13 <(cat ./shm/aps_data_eventlog_members.csv|sort -k3) audio_name_class.index > event_audio_name_class.index
