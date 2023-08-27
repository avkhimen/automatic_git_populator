import numpy as np
import pandas as pd
import argparse
import redis
import os
from datetime import datetime

from utils.formats import EXCLUDED_DATA_FORMATS
from utils.storage_utils import make_redis_client
import subprocess
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s [%(levelname)s] - %(message)s',
                    filename='/Users/vadimavkhimenia/Documents/projects/automatic_git_populator/log_files/logs.log')
'''
# Using the logger
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
'''

'''
Workflow:

1. read input args
2. get project name
3. init redis client
4. check if project is present in redis, exit if it does
5. setup loop to make commits
    5.1. 
'''

def git_actions(file_name, commit_message):
    try:
        # Git add
        subprocess.check_call(['git', 'add', file_name])
        
        # Git commit
        subprocess.check_call(['git', 'commit', '-m', commit_message])
        
        # Git push
        subprocess.check_call(['git', 'push', 'origin', 'main'])
        
        print("Git actions completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error executing git command: {e}")

def create_project_name(path):
    project_base = os.path.basename(os.path.normpath(path))
    current_date = datetime.now()
    current_date_string = current_date.strftime('%Y%m%d')
    project_name = project_base + '_' + current_date_string
    return project_name

# List to store file names
# Function to list non-hidden files in a directory
def list_non_hidden_files(directory, absolute_path):
    non_hidden_files = []
    non_hidden_files_code_line_nums = []
    for root, dirs, files in os.walk(directory):
        # Filter out hidden subdirectories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d[0].isalpha()]
        for file in files:
            if (not file.startswith('.')) and (file.split('.')[-1] not in EXCLUDED_DATA_FORMATS):  # Check if file is not hidden
                non_hidden_files.append(os.path.join(absolute_path, os.path.join(root, file)[2:]))
                with open(os.path.join(absolute_path, os.path.join(root, file)[2:]), 'r') as f:
                    line_count = sum(1 for line in f)
                non_hidden_files_code_line_nums.append(line_count)
    return non_hidden_files, non_hidden_files_code_line_nums

def setup_temp_repo():
    pass

def copy_lines_over(filename):
    pass

def main():
    parser = argparse.ArgumentParser(description="Input variables")
    parser.add_argument("--dir_name", required=True, type=str, help="Path to directory")
    parser.add_argument("--freq", required=True, type=float, choices=[0.5, 1.0, 1.5, 2.0], help="How often to commit")
    parser.add_argument("--num_days", required=True, type=int, help="How many days to spend committing")
    parser.add_argument("--start_date", required=True, type=str, help="Start date in format YYYYMMDD")

    args = parser.parse_args()

    dir_name = args.dir_name
    absolute_path = os.path.abspath(dir_name)

    start_date = args.start_date
    start_date = datetime.strptime(start_date, '%Y%m%d')

    print('absolute path', absolute_path)

    freq = args.freq
    num_days = args.num_days

    print(dir_name, freq, num_days)

    project_name = create_project_name(absolute_path)

    print(project_name)

    redis_client = make_redis_client()

    project_to_check = project_name[:-8]
    if redis_client.exists(project_to_check):
        print(f"The key '{project_to_check}' exists in the Redis database.")
        return
    else:
        print(f"The key '{project_to_check}' does not exist in the Redis database.")

    # Get a list of non-hidden files
    non_hidden_files, non_hidden_files_code_line_nums = list_non_hidden_files(dir_name, absolute_path)

    total_num_of_lines_of_code = np.array(non_hidden_files_code_line_nums).sum()
    print('Total number of lines of code', total_num_of_lines_of_code)

    # Print the list of non-hidden files
    for file_path in non_hidden_files:
        print(file_path)
        x = 2
        y = 3

        with open(file_path, 'r') as f:
            for current_line_number, line in enumerate(f, 1):  # Start counting from 1
                if x <= current_line_number <= y:
                    print(line, end='')  # Print the line

    current_project = {'completion_status' : False, 'files' : [], 'file_numbers' : []}
    #Commit loop
    while not current_project['completion_status']:
        print('Running')
        # for every file name pick a random number of lines to copy
        # copy lines and paste them
        # update the dictionary's completion status and the last file lines
        for ii, file_path in enumerate(non_hidden_files):
            # use non_hidden_files_code_line_nums
            # use current_project['file_numbers'][ii]
            number_of_code_lines_remaining = non_hidden_files_code_line_nums[ii] - current_project['file_numbers'][ii]
            print('The number of lines in a file is')
            print('pick a random number for number of lines of code to commit')
        print('Commit here')
        current_project['completion_status'] = True
        #commit changes

    # Data to store
    key = project_name
    value = 'file_names'

    # Store data in Redis
    redis_client.mset({key: value})

    # Retrieve and print the stored data
    stored_value = redis_client.get(key)
    print(f"Key: {key}\nStored Value: {stored_value.decode('utf-8')}")

    print(non_hidden_files_code_line_nums)

if __name__ == '__main__':
    main()
