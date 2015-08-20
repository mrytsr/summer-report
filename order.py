#!/usr/bin/env python2
#coding:utf-8

addr_dict = { }
age_dict = { }
gender_dict = { }
addrs = {}
ages = {}
genders = {}

for line in open("member_year_gender.index"):
    arr = line.split('" "')
    age = arr[1]
    gender = arr[2].rstrip('"\n')
    if not age in ages:
        ages[age] = 0
    ages[age] += 1
    if not gender in genders:
        genders[gender] = 0
    genders[gender] += 1


for line in open("device_addr.index"):
    arr = line.split('" "')
    addr = arr[1].rstrip('"\n')
    if not addr in addrs:
        addrs[addr] = 0
    addrs[addr] += 1

for line in open("order.index"):
    # "499" "2015-05-28 20:58:05" "甘肃省" "NULL" "NULL"
    arr = line.split('" "')
    cost = int(arr[0].lstrip('"'))
    addr = arr[2]
    age = arr[3]
    gender = arr[4].rstrip('"\n')

    if gender != 'NULL':
        if not gender in gender_dict:
            gender_dict[gender] = {
                        'total' : 0,
                        'count' : 0
                    }
        gender_dict[gender]['total'] += cost
        gender_dict[gender]['count'] += 1
    if age != 'NULL':
        if not age in age_dict:
            age_dict[age] = {
                        'total' : 0,
                        'count' : 0
                    }
        age_dict[age]['total'] += cost
        age_dict[age]['count'] += 1
    if addr != 'NULL' and addr != '0':
        if not addr in addr_dict:
            addr_dict[addr] = {
                        'total' : 0,
                        'count' : 0
                    }
        addr_dict[addr]['total'] += cost
        addr_dict[addr]['count'] += 1

print '\n### addr\ntotal|count|total/count|total/占比\n---|---|---|---'
for addr in addr_dict:
    print addr, "|",\
	 addr_dict[addr]['total'], "|",\
	 addr_dict[addr]['count'], "|",\
	 1.0 * addr_dict[addr]['total'] / addr_dict[addr]['count'], "|",\
     addr_dict[addr]['total'] / addrs[addr]

print '\n### age\ntotal|count|total/count|total/占比\n---|---|---|---'
for age in age_dict:
    print age, "|",\
	 age_dict[age]['total'], "|",\
	 age_dict[age]['count'], "|",\
	 1.0 * age_dict[age]['total'] / age_dict[age]['count'], "|",\
     age_dict[age]['total'] / ages[age]

print '\n### gender\ntotal|count|total/count|total/占比\n---|---|---|---'
for gender in gender_dict:
    print gender, "|",\
	 gender_dict[gender]['total'], "|",\
	 gender_dict[gender]['count'], "|",\
	 1.0 * gender_dict[gender]['total'] / gender_dict[gender]['count'], "|",\
     gender_dict[gender]['total'] / genders[gender]
