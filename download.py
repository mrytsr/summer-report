#!/usr/bin/env pypy
#coding:utf-8
import sys
import time

n = 10000000000
title_dict = {}
global_dict = {}
global_dict = {
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
        }

addr_dict = { }

def cmp_weight(val1, val2):
    return cmp(val1['weight'], val2['weight'])

for line in open("event_3.index"):
    arr = line.split('" "')
    title = arr[5].rstrip('\n').rstrip('"').replace('\'', '')
    addr = arr[1]
    age = arr[3]
    gender = arr[4]
    daytime = time.strptime(arr[0][12:22], '%H:%M:%S')[3] #* 3600 #+  time.strptime(arr[0][12:22], '%H:%M:%S')[4] * 60

    if addr != 'NULL':
        if not addr in addr_dict:
            addr_dict[addr] = {
                    'total' : 0
                    }
        if not daytime in addr_dict[addr]:
            addr_dict[addr][daytime] = 0
        addr_dict[addr][daytime] += 1
        addr_dict[addr]['total'] += 1

    if title != 'NULL':
        if not title in title_dict:
            title_dict[title] = {'count': 0, 
                    'age' : {}, 
                    'age_count' : 0,
                    'gender': {}, 
                    'gender_count' : 0,
                    'addr': {},
                    'addr_count': 0
                    }
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

print '## ' + str(daytime)
for addr in addr_dict:
    print '\n### ' + addr + '\naddr|count|count*\n---|---|---'
    for daytime in addr_dict[addr]:
        if not daytime == 'total':
            print daytime, '|', addr_dict[addr][daytime], '|', 'I' * int(1.0 * addr_dict[addr][daytime] / addr_dict[addr]['total'] * 500)


# print "## titles"
for title in title_dict:
    if title_dict[title]['age_count'] < 30:
        continue

    # print "### title: " + title 
    age_dict = sorted(title_dict[title]['age'].iteritems(), key=lambda d:d[1], reverse = True)
    addr_dict = sorted(title_dict[title]['addr'].iteritems(), key=lambda d:d[1], reverse = True)
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
