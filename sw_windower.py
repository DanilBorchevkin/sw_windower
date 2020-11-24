# -*- coding: utf-8 -*-
"""
Plot graph according to the DAT file 
@author: Danil Borchevkin
"""

import csv
import glob
import os

def read_file_data(filepath):
    '''
    Read data in list
    '''

    raw_data = list()

    # Get raw data
    with open(filepath, 'r') as dest_f:
        raw_data = dest_f.readlines()

    return raw_data

def process_file(data, out_filepath, window, step):
    line_cursor = 0

    while (line_cursor < (len(data) - window)):
        with open(out_filepath + '_c' + str(line_cursor) + '_w' + str(window) + '_s' + str(step) + ".dat", 'w') as dest_f:
            for i in range(window):
                dest_f.write(data[line_cursor + i])
        
        line_cursor += step
                

def main():
    print("Script is started")

    files = glob.glob("./input/*.dat")
    WINDOW = 50     # Change window value here
    STEP = 10       # Change step value here

    for filepath in files:
        print("Process >> " + filepath)

        try:
            read_data = read_file_data(filepath)
            out_dat_filepath = "./output/" + os.path.basename(filepath)
            process_file(read_data, out_dat_filepath, WINDOW, STEP)
            print(f"<{filepath}> succesful processed by the script")
    
        except Exception as e:
            print("Cannot process >> ", filepath)
            print("Reason >> " + str(e))
            
        finally:
            print()

    print("Script is finished")

if __name__ == "__main__":
    main()