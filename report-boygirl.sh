#!/bin/bash
awk  -F'" "' '
BEGIN{
    print "男|女|比例|故事"
    print "---|---|---|---"
}{
    if($5!="NULL"){
        if($5==1){
            boy[$6" - "$7]++;
        }else{
            girl[$6" - "$7]++;
        }
    }
}END{
    for(i in boy){
        print i
        mark[i] = boy[i] / (boy[i] + girl[i])
    }
    for(i in mark){
        if(boy[i]<20&&girl[i]<20)
            continue;
        if(girl[i]==""||boy[i]/girl[i]>1.4||boy[i]==""||girl[i]/boy[i]>1.4)
            print boy[i]" | "girl[i]" | " mark[i]  " | " i;
    }
}' event_3.index > report-boygirl.md
