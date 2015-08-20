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
                        'key' : gender,
                        'total' : 0,
                        'count' : 0
                    }
        gender_dict[gender]['total'] += cost
        gender_dict[gender]['count'] += 1
    if age != 'NULL':
        if not age in age_dict:
            age_dict[age] = {
                        'key' : age,
                        'total' : 0,
                        'count' : 0
                    }
        age_dict[age]['total'] += cost
        age_dict[age]['count'] += 1
    if addr != 'NULL' and addr != '0':
        if not addr in addr_dict:
            addr_dict[addr] = {
                        'key' : addr,
                        'total' : 0,
                        'count' : 0
                    }
        addr_dict[addr]['total'] += cost
        addr_dict[addr]['count'] += 1

print '\n### addr\ntotal|count|total/count|total/占比\n---|---|---|---'

def cmp_total_addr(val1, val2):
    return cmp(val1['total'] / addrs[val1['key']], val2['total'] / addrs[val2['key']])

addr_list = sorted(addr_dict.iteritems(), cmp_total_addr, key=lambda d:d[1], reverse = True)

for addr,detail in addr_list:
    print addr, "|",\
	 detail['total'], "|",\
	 detail['count'], "|",\
	 1.0 * detail['total'] / detail['count'], "|",\
     detail['total'] / addrs[addr]

print '\n### age\ntotal|count|total/count|total/占比\n---|---|---|---'
def cmp_age(val1, val2):
    return cmp(val1,val2)
age_list = sorted(age_dict.iteritems(), cmp_age, key=lambda d:d[0], reverse = True)
for age,detail in age_list:
    print 2015 - int(age), "|",\
	 detail['total'], "|",\
	 detail['count'], "|",\
	 1.0 * detail['total'] / detail['count'], "|",\
     detail['total'] / ages[age]

print '\n### gender\ntotal|count|total/count|total/占比\n---|---|---|---'
def cmp_total_gender(val1, val2):
    return cmp(val1['total'] / genders[val1['key']],
            val2['total'] / genders[val2['key']]
            )
gender_list = sorted(gender_dict.iteritems(), cmp_total_gender, key=lambda d:d[1], reverse = True)
for gender,detail in gender_list:
    print gender, "|",\
	 detail['total'], "|",\
	 detail['count'], "|",\
	 1.0 * detail['total'] / detail['count'], "|",\
     detail['total'] / genders[gender]
