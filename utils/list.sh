#!/bin/bash
# find all traces in the directory and execute
files=$(ls ../traces/)
for filename in $files
do
    end=${filename:${#filename}-8}
    if [ "$end" = "trace.gz" ]; then
#    echo ${filename:0:${#filename}-9}.stats
    ../bin/CMPsim.usetrace.64 -threads 1 -t ../traces/$filename -o ../result/${filename:0:${#filename}-9}.stats -cache UL3:1024:64:16 -LLCrepl 1
    fi
done

python get_result.py
