#!/bin/bash
awk  -F'" "|"$' '
BEGIN{
    print "男比例|男|女|故事"
    print "---|---|---|---"
}{
    if($5!="NULL"){
        split($7, ts, ",")
        if($5==1){
            boy[$6" - "$7]++
            for(t in ts){
                taxoboy[t]++
            }
        }else{
            girl[$6" - "$7]++
            for(t in ts){
                taxogirl[t]++
            }
        }
    }
}END{
    for(i in boy){
        if(boy[i]<20&&girl[i]<20)
            continue;
        if(girl[i]==""||boy[i]/girl[i]>1.4||boy[i]==""||girl[i]/boy[i]>1.4)
            print boy[i] / (boy[i] + girl[i])  " | " boy[i]" | "girl[i]" | "  i | "sort -r -n -k1";
    }
    print ""
    print "taxo | taxogirl"
    for(taxo in taxogirl){
        print taxo " | " taxogirl[taxo]
    }
}' event_3.index #> report-boygirl.md
