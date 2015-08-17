#!/bin/bash
join -o 1.1 2.2 -1 2 <(sort -k2 device_loc.index) loc_addr.index |sort > device_addr.index

