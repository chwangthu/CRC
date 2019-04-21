import os
import re
import csv
import datetime
import gzip
import time

def file_name(file_dir):
    for _, _, files in os.walk(file_dir):
            return files

def extract_res(path, file):
    f = gzip.open(path+file, 'rb')
    content = f.read()
    content = content.decode('utf-8')
    res_pattern = re.compile(u".*Thread:.*Lookups.*\n", re.IGNORECASE)
    res = re.findall(res_pattern, content)
    # print(file[0:3], res[0][:-1].split(" ")[-1])
    f.close()
    return file[0:3], res[0][:-1].split(" ")[-1]

if __name__ == "__main__":
    policy = input("Please input replacement policy: ")
    traces_path="../traces/"
    traces = file_name(traces_path)
    time_res = {}
    for item in traces:
        if item[-8:] == "trace.gz":
            start = time.time()
            command = "../bin/CMPsim.usetrace.64 -threads 1 -t ../traces/" + item + " -o ../result/" + item[0:-9] + ".stats -cache UL3:1024:64:16 -LLCrepl " + str(policy)
            os.system(command)
            end = time.time()
            time_res[int(item[0:3])] = float(end-start)

    path="../result/"
    result = {}
    files = file_name(path)
    for item in files:
        if item[-8:] == "stats.gz":
            name, res = extract_res(path, item)
            result[int(name)] = round(float(res),3) 
    print(time_res)
    print(result)
    with open(str(datetime.datetime.now())+".csv", "w") as f:
        writer = csv.writer(f)
        for item in result:
            writer.writerow([item, result[item], time_res[item]])