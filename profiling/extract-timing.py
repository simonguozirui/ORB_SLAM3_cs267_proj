import re
import pandas as pd
def parse_input(data_file_path):
    data_file = open(data_file_path, 'r')
    lines = data_file.readlines()
    
    overall_timing = []
    global_stats = []

    for line in lines:
        if line.startswith("[DEBUG]"):
            decomposed = line.split(" ")
            if (decomposed[1] == "Overall"):                
                overall_timing.append(decomposed[3].strip().split(','))
            elif (decomposed[1] == "global"):
                # print(line)
                for index, value in zip(range(len(decomposed)), decomposed):
                    print (index, value)
                    # global_stats.append([decomposed[16][:-2], decomposed[18][:-2], decomposed[22][:-2], decomposed[34][:-2]])

                
            # print(line.strip(" "))  
    # print(overall_timing)
  
    print(global_stats)
    pd.DataFrame()

    return 

data_file_path='run_01.txt'
parse_input(data_file_path)
