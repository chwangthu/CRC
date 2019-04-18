import os
import re
import gzip

def file_name(file_dir):
    for _, _, files in os.walk(file_dir):
            return files

def extract_res(file):
    f = gzip.open(file, 'rb')
    content = f.read()
    content = content.decode('utf-8')
    res_pattern = re.compile(u".*Thread:.*Lookups.*\n", re.IGNORECASE)
    res = re.findall(res_pattern, content)
    print(file, res)
    f.close()

if __name__ == "__main__":
    path="../result/"
    files = file_name(path)
    for item in files:
        if item[-8:] == "stats.gz":
            extract_res(path+item)
