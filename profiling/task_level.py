import re
import pandas as pd
import numpy as np
def parse_input(trace_root_path, trace_name):
    data_file = open(trace_root_path + '/' + trace_name, 'r')
    lines = data_file.readlines()

    data_dict = {"trackig-period": [], 
                "tracking-time" : [],
                "mapping-period" : [],
                "mapping-time" : [],
                "loop-closing-period": [],
                "loop-closing-time":[]}

    for line in lines:
        if line.startswith("[Profiling]"):
            decomposed = line.split(" ")
            # print(decomposed)
            if (decomposed[1] == '[Task'):
                if (decomposed[3] == 'Tracking'):
                    data_dict['trackig-period'].append(float(decomposed[5].replace(',', '')))
                    data_dict['tracking-time'].append(float(decomposed[7].replace('\n', '')))
                elif (decomposed[3] == 'Local'):
                    data_dict['mapping-period'].append(float(decomposed[6].replace(',', '')))
                    data_dict['mapping-time'].append(float(decomposed[8].replace('\n', '').replace(',', '')))
                elif (decomposed[3] == 'Loop'):
                    print(decomposed)
                    if (decomposed[6] != "LM:"):
                        data_dict['loop-closing-period'].append(float(decomposed[6].replace(',', '')))
                        data_dict['loop-closing-time'].append(float(decomposed[8].replace('\n', '')))
    return data_dict


def get_mean_and_sd(dict):
    for metric in dict:
        print("For {}: Mean {} Std {}".format(metric, np.mean(dict[metric][1:]), np.std(dict[metric][1:])))
    return 

trace_root_path='/nscratch/simon/ba-profile/mount/traces'
trace_name='task-MH_01_easy.out'
data_dict = parse_input(trace_root_path, trace_name)
get_mean_and_sd(data_dict)
# print(data_dict['trackig-period'])
