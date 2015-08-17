#!/bin/bash
awk  -F'" "' '
{
    if($5!="NULL"){
        if($5==1){
            boy[$6" - "$7]++;
        }else{
            girl[$6" - "$7]++;
        }
    }
    print "男|女|故事"
    print "---|---|---"
}END{
    for(i in boy){
        if(boy[i]<10&&girl[i]<10)
            continue;
        if(girl[i]==""||boy[i]/girl[i]>1.2||boy[i]==""||girl[i]/boy[i]>1.2)
            print boy[i]" | "girl[i]" | "i;
    }
}' event_3.index > report-boygirl.md
