import os
import re
import csv
import datetime
import gzip

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
    path="../result/"
    result = {}
    files = file_name(path)
    for item in files:
        if item[-8:] == "stats.gz":
            name, res = extract_res(path, item)
            result[int(name)] = round(float(res),3) 
    print(result)
    with open(str(datetime.datetime.now())+".csv", "w") as f:
        writer = csv.writer(f)
        for item in result:
            writer.writerow([item, result[item]])