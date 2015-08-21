#!/usr/bin/env pypy
#coding:utf-8
import sys
import time

n = 10000000000
title_dict = {}
global_dict = {}
global_dict = {
        'devicetype' : {}, 
        'devicetype_count' : 0,
        'devicemodel' : {}, 
        'devicemodel_count' : 0,
        'deviceheight' : {}, 
        'deviceheight_count' : 0,
        'deviceversion' : {}, 
        'deviceversion_count' : 0,
        'age' : {}, 
        'age_count' : 0,
        'gender': {}, 
        'gender_count' : 0,
        'addr': {},
        'addr_count': 0
        }

prefer_dict = {
        'age' : {},
        'gender' : {},
        'addr' : {},
        'devicetype' : {}, 
        'devicemodel' : {}, 
        'deviceheight' : {}, 
        'deviceversion' : {}, 
        }

addr_dict = { }

age_dict = { }

def cmp_weight(val1, val2):
    return cmp(val1['weight'], val2['weight'])

for line in open("download.index"):
    arr = line.split('" "')
    daytime = time.strptime(arr[0][12:22], '%H:%M:%S')[3]
    addr = arr[1]
    age = arr[3]
    gender = arr[4]
    title = arr[5].replace('\'', '-')
    taxo = arr[6]

    devicetype = 'NULL'
    devicemodel = 'NULL'
    deviceheight = 'NULL'
    deviceversion = 'NULL'
    try:
        devicearr = arr[7].rstrip('"\n').split(',')
    except Exception as ex:
        print arr
    if len(devicearr) == 4:
        devicetype = devicearr[0]
        devicemodel = devicearr[1]
        deviceheight = devicearr[2]
        deviceversion = devicearr[3]

    if addr != 'NULL':
        if not addr in addr_dict:
            addr_dict[addr] = { 'total' : 0, 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0 }
        addr_dict[addr][daytime] += 1
        addr_dict[addr]['total'] += 1

    if age != 'NULL':
        if not age in age_dict:
            age_dict[age] = { 'total' : 0, 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0 }
        if not daytime in age_dict[age]:
            age_dict[age][daytime] = 0
        age_dict[age][daytime] += 1
        age_dict[age]['total'] += 1

    if title != 'NULL':
        if not title in title_dict:
            title_dict[title] = {
                    'count': 0, 
                    'devicetype' : {}, 
                    'devicetype_count' : 0,
                    'devicemodel' : {}, 
                    'devicemodel_count' : 0,
                    'deviceheight' : {}, 
                    'deviceheight_count' : 0,
                    'deviceversion' : {}, 
                    'deviceversion_count' : 0,
                    'age' : {}, 
                    'age_count' : 0,
                    'gender': {}, 
                    'gender_count' : 0,
                    'addr': {},
                    'addr_count': 0
                    }
        if deviceversion != 'NULL':
            if not deviceversion in title_dict[title]['deviceversion']:
                title_dict[title]['deviceversion'][deviceversion] = 0
            title_dict[title]['deviceversion'][deviceversion] += 1
            title_dict[title]['deviceversion_count'] += 1
            if not deviceversion in global_dict['deviceversion']:
                global_dict['deviceversion'][deviceversion] = 0
            global_dict['deviceversion'][deviceversion] += 1
            global_dict['deviceversion_count'] += 1
        if deviceheight != 'NULL':
            if not deviceheight in title_dict[title]['deviceheight']:
                title_dict[title]['deviceheight'][deviceheight] = 0
            title_dict[title]['deviceheight'][deviceheight] += 1
            title_dict[title]['deviceheight_count'] += 1
            if not deviceheight in global_dict['deviceheight']:
                global_dict['deviceheight'][deviceheight] = 0
            global_dict['deviceheight'][deviceheight] += 1
            global_dict['deviceheight_count'] += 1
        if devicemodel != 'NULL':
            if not devicemodel in title_dict[title]['devicemodel']:
                title_dict[title]['devicemodel'][devicemodel] = 0
            title_dict[title]['devicemodel'][devicemodel] += 1
            title_dict[title]['devicemodel_count'] += 1
            if not devicemodel in global_dict['devicemodel']:
                global_dict['devicemodel'][devicemodel] = 0
            global_dict['devicemodel'][devicemodel] += 1
            global_dict['devicemodel_count'] += 1
        if devicetype != 'NULL':
            if not devicetype in title_dict[title]['devicetype']:
                title_dict[title]['devicetype'][devicetype] = 0
            title_dict[title]['devicetype'][devicetype] += 1
            title_dict[title]['devicetype_count'] += 1
            if not devicetype in global_dict['devicetype']:
                global_dict['devicetype'][devicetype] = 0
            global_dict['devicetype'][devicetype] += 1
            global_dict['devicetype_count'] += 1
        if age != 'NULL':
            if not age in title_dict[title]['age']:
                title_dict[title]['age'][age] = 0
            title_dict[title]['age'][age] += 1
            title_dict[title]['age_count'] += 1
            if not age in global_dict['age']:
                global_dict['age'][age] = 0
            global_dict['age'][age] += 1
            global_dict['age_count'] += 1
        if gender != 'NULL':
            if not gender in title_dict[title]['gender']:
                title_dict[title]['gender'][gender] = 0
            title_dict[title]['gender'][gender] += 1
            title_dict[title]['gender_count'] += 1
            if not gender in global_dict['gender']:
                global_dict['gender'][gender] = 0
            global_dict['gender'][gender] += 1
            global_dict['gender_count'] += 1
        if addr != 'NULL':
            if not addr in title_dict[title]['addr']:
                title_dict[title]['addr'][addr] = 0
            title_dict[title]['addr'][addr] += 1
            title_dict[title]['addr_count'] += 1
            if not addr in global_dict['addr']:
                global_dict['addr'][addr] = 0
            global_dict['addr'][addr] += 1
            global_dict['addr_count'] += 1

    n -= 1
    if(n == 0):
        break

print '## ' + 'addr和时间的相关性'
for addr in addr_dict:
    print '\n### ' + addr + '\naddr|count|count*\n---|---|---'
    for daytime in addr_dict[addr]:
        if not daytime == 'total':
            print daytime, '|', addr_dict[addr][daytime], '|', 'I' * int(1.0 * addr_dict[addr][daytime] / addr_dict[addr]['total'] * 500)

print '## ' + 'age和时间的相关性'
for age in age_dict:
    print '\n### ' + age + '\nage|count|count*\n---|---|---'
    for daytime in age_dict[age]:
        if not daytime == 'total':
            print daytime, '|', age_dict[age][daytime], '|', 'I' * int(1.0 * age_dict[age][daytime] / age_dict[age]['total'] * 400)


# print "## titles"
for title in title_dict:
    if title_dict[title]['age_count'] < 30:
        continue

    devicetype_dict = sorted(title_dict[title]['devicetype'].iteritems(), key=lambda d:d[1], reverse = True)
    for devicetype,count in devicetype_dict:
        if count < 40:
            continue
        weight = 1.0 * count / title_dict[title]['devicetype_count'] / global_dict['devicetype'][devicetype] * global_dict['devicetype_count']
        if weight > 1.4:
            # print devicetype, count, weight 
            if not devicetype in prefer_dict['devicetype']:
                prefer_dict['devicetype'][devicetype] = {}
            prefer_dict['devicetype'][devicetype][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    devicemodel_dict = sorted(title_dict[title]['devicemodel'].iteritems(), key=lambda d:d[1], reverse = True)
    for devicemodel,count in devicemodel_dict:
        if count < 40:
            continue
        weight = 1.0 * count / title_dict[title]['devicemodel_count'] / global_dict['devicemodel'][devicemodel] * global_dict['devicemodel_count']
        if weight > 1.4:
            # print devicemodel, count, weight 
            if not devicemodel in prefer_dict['devicemodel']:
                prefer_dict['devicemodel'][devicemodel] = {}
            prefer_dict['devicemodel'][devicemodel][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    deviceheight_dict = sorted(title_dict[title]['deviceheight'].iteritems(), key=lambda d:d[1], reverse = True)
    for deviceheight,count in deviceheight_dict:
        if count < 40:
            continue
        weight = 1.0 * count / title_dict[title]['deviceheight_count'] / global_dict['deviceheight'][deviceheight] * global_dict['deviceheight_count']
        if weight > 1.4:
            # print deviceheight, count, weight 
            if not deviceheight in prefer_dict['deviceheight']:
                prefer_dict['deviceheight'][deviceheight] = {}
            prefer_dict['deviceheight'][deviceheight][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    deviceversion_dict = sorted(title_dict[title]['deviceversion'].iteritems(), key=lambda d:d[1], reverse = True)
    for deviceversion,count in deviceversion_dict:
        if count < 40:
            continue
        weight = 1.0 * count / title_dict[title]['deviceversion_count'] / global_dict['deviceversion'][deviceversion] * global_dict['deviceversion_count']
        if weight > 1.4:
            # print deviceversion, count, weight 
            if not deviceversion in prefer_dict['deviceversion']:
                prefer_dict['deviceversion'][deviceversion] = {}
            prefer_dict['deviceversion'][deviceversion][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    gender_dict = sorted(title_dict[title]['gender'].iteritems(), key=lambda d:d[1], reverse = True)
    for gender,count in gender_dict:
        if count < 40:
            continue
        weight = 1.0 * count / title_dict[title]['gender_count'] / global_dict['gender'][gender] * global_dict['gender_count']
        if weight > 1.4:
            # print gender, count, weight 
            if not gender in prefer_dict['gender']:
                prefer_dict['gender'][gender] = {}
            prefer_dict['gender'][gender][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    age_dict = sorted(title_dict[title]['age'].iteritems(), key=lambda d:d[1], reverse = True)
    for age,count in age_dict:
        if count < 20:
            continue
        weight = 1.0 * count / title_dict[title]['age_count'] / global_dict['age'][age] * global_dict['age_count']
        if weight > 1.3:
            # print age, count, weight
            if not age in prefer_dict['age']:
                prefer_dict['age'][age] = {}
            prefer_dict['age'][age][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

    addr_dict = sorted(title_dict[title]['addr'].iteritems(), key=lambda d:d[1], reverse = True)
    for addr,count in addr_dict:
        if count < 10:
            continue
        weight = 1.0 * count / title_dict[title]['addr_count'] / global_dict['addr'][addr] * global_dict['addr_count']
        if weight > 1.2:
            # print addr,count, weight
            if not addr in prefer_dict['addr']:
                prefer_dict['addr'][addr] = {}
            prefer_dict['addr'][addr][title] = {
                    'count' : count,
                    'weight' : weight,
                    }

for prefer in prefer_dict:
    print "\n## " + prefer
    for reason in prefer_dict[prefer].keys():
        print "\n### " + prefer + ": " + reason
        print "\n" + reason + "|weight|count|weight*"
        print "---|---|---|---"
        title_dict = sorted(prefer_dict[prefer][reason].iteritems(), cmp_weight, key=lambda d:d[1], reverse = True)
        for title,detail in title_dict:
            print title, '|', detail['weight'], '|', detail['count'], '|', 'I' * int(detail['weight'] / 2 * 50)


# age_dict = sorted(global_dict['age'].iteritems(), key=lambda d:d[1], reverse = True)
# addr_dict = sorted(global_dict['addr'].iteritems(), key=lambda d:d[1], reverse = True)
# gender_dict = global_dict['gender']

# print ''
# print '[global]'
# print '[count]', global_dict['gender_count']
# for gender in gender_dict.keys():
#     print gender, gender_dict[gender]
# print '[count]', global_dict['age_count']
# for age,count in age_dict:
#     print age,count
# print '[count]', global_dict['addr_count']
# for addr,count in addr_dict:
#     print addr,count

# dic= sorted(age_dict.iteritems(), key=lambda d:d[0])
# for item in dic:
#     age = item[0]
#     print age
#     titles = sorted(item[1].iteritems(), key=lambda d:d[1], reverse = True)
#     for title,count in titles:
#         print title, count
#         if count < 10:
#             break
