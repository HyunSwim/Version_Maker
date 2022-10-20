import argparse
import json
import csv
from collections import OrderedDict
import pandas as pd

file_data = OrderedDict()
data = ["bsm", "gps", "map", "pvd", "rtcm", "spat"]
total_data = []
stri = " "

def make_json(Path):
    json_data = {}
    data_list = []

    with open(Path + ".csv", encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for index, rows in enumerate(csvReader):
            key = rows[list(rows.keys())[0]]
            json_data[index] = rows
            # data_list.append(rows)
            # print(rows)
            # exit()
        
    with open(Path + ".json", 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(json_data, indent=4))

def make_csv_without_gps():
    global stri
    writeFileCsv = open(pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data_without_gps.csv", "w")
    writeFileCsv.write(stri)
    print("Convert complete! : " + pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data_without_gps.csv")
    writeFileCsv.close()

def make_sentense(stl):
    global stri
    stri = stri + stl + '\n'
    
def make_csv_with_gps(g, pwd, i):
    global stri
    plus_msg = ""
    if i == 0:
        plus_msg = "_with_gps"
    g_stri = ""
    j = 0
    writeFileCsv = open(pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data" + plus_msg + ".csv", "w")
    while True:
        g_str = g.readline()

        if not g_str:
            print("Convert complete! : " + pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data" + plus_msg + ".csv")
            break

        g_str = g_str.replace(":", "")

        if j == 0:
            g_str = g_str.replace("'", "")
            g_str = g_str.replace("/", "")

        g_list = g_str.split()
        g_str = g_str.replace(" ", ",")
        writeFileCsv.write(g_str)

        if i == 0:
            g_stri = ""
            g_list.pop(3)
            g_list.pop(3)
            for k in range(len(g_list)-1):
                g_stri = g_stri + g_list[k] + ","
            g_stri = g_stri + g_list[len(g_list)-1]
            make_sentense(g_stri)

        j += 1

    if i == 0:
        make_csv_without_gps()
    
    writeFileCsv.close()
    make_json(pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data" + plus_msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File pwd..')
    parser.add_argument('--pwd')
    args = parser.parse_args()

    with open(args.pwd + "/directory.txt", "r") as f:
        while True:
            pwd = f.readline()
            pwd = pwd.replace("\n", "")
            if not pwd:
                break
            for i in range(len(data)):
                new_pwd = pwd + "/obu/" + data[i] + "/obu_" + data[i] + "_data.txt"
                try:
                    print(data[i])

                    with open(new_pwd, "r") as g:
                        make_csv_with_gps(g, pwd, i)
                except:
                    print("no file : " + new_pwd)