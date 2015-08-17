#!/bin/bash
awk  -F'" "|"$' '
BEGIN{
}{
    if($5!="NULL"){
        if($5==1){
            boy[$6]++
        }else{
            girl[$6]++
        }
        taxo[$6]=$7
    }
}END{
    # print "男比例|男|女|故事"
    # print "---|---|---|---"
    for(i in boy){
        if(boy[i]<20&&girl[i]<20)
            continue;
        boymark = boy[i] / (boy[i] + girl[i])
        if(girl[i]==""||boy[i]/girl[i]>1.4||boy[i]==""||girl[i]/boy[i]>1.4){
            # print  boymark " | " boy[i]" | "girl[i]" | "  i | "sort -r -n -k1";
            split(taxo[i], ts, ",")
            if(boymark > 0.5){
                for(t in ts){
                    taxoboy[ts[t]]++
                }
            }else{
                for(t in ts){
                    taxogirl[ts[t]]++
                }
            }
        }
    }
}END{
    print "taxo | taxogirl"
    print "---|---"
    for(t in taxogirl){
        if(taxogirl[t] > 8)
            print taxogirl[t] " | " t | "sort -rnk1"
    }
    # print "taxo | taxoboy"
    # print "---|---"
    # for(t in taxoboy){
    #     if(taxoboy[t] > 8)
    #         print taxoboy[t] " | " t | "sort -rnk1"
    # }
}' event_3.index >> report-boygirl.md
