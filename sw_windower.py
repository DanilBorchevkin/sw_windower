# -*- coding: utf-8 -*-
"""
Slice file by windows
@author: Danil Borchevkin
"""

import glob
import os

def read_file_data(filepath):
    '''
    Read data in list
    '''

    raw_data = list()
    encondings = ['utf-8', 'utf-16']
    for encoding in encondings:
        try:
            with open(filepath, 'r', encoding=encoding) as dest_f:
                raw_data = dest_f.readlines()
            is_read = True
            break
        except:
            continue

    # Get raw data
    if False == is_read:
        raise Exception(f"<{filepath}> has non-supported encoding")

    return raw_data

def process_file(data, out_filepath, window, step):
    line_cursor = 0

    while (line_cursor < (len(data) - window)):
        with open(out_filepath + '_c' + "{:08d}".format(line_cursor) + '_w' + str(window) + '_s' + str(step) + ".dat", 'w') as dest_f:
            for i in range(window):
                dest_f.write(data[line_cursor + i])
        line_cursor += step
                
def main():
    print("Script is started")

    files = glob.glob("./input/*.dat")
    WINDOW = 79920     # Change window value here
    STEP = 79920       # Change step value here

    for filepath in files:
        print("Process >> " + filepath)

        try:
            read_data = read_file_data(filepath)
            out_dat_filepath = "./output/" + os.path.basename(filepath)
            process_file(read_data, out_dat_filepath, WINDOW, STEP)
            print(f"<{filepath}> was processed by the script")
    
        except Exception as e:
            print("Cannot process >> ", filepath)
            print("Reason >> " + str(e))
            
        finally:
            print()

    print("Script is finished")

if __name__ == "__main__":
    main()