import numpy as np
import pandas as pd
import argparse
import redis
import os
from datetime import datetime

from utils.formats import DATA_FORMATS
from utils.storage_utils import make_redis_client

def create_project_name(path):
    project_base = os.path.basename(os.path.normpath(path))
    current_date = datetime.now()
    current_date_string = current_date.strftime('%Y%m%d')
    project_name = project_base + '_' + current_date_string
    return project_name

def main():
    parser = argparse.ArgumentParser(description="Input variables")
    parser.add_argument("--dir_name", required=True, type=str, help="Path to directory")
    parser.add_argument("--freq", required=True, type=float, choices=[0.5, 1.0, 1.5, 2.0], help="How often to commit")
    parser.add_argument("--num_days", required=True, type=int, help="How many days to spend committing")

    args = parser.parse_args()

    dir_name = args.dir_name
    absolute_path = os.path.abspath(dir_name)

    freq = args.freq
    num_days = args.num_days

    print(dir_name, freq, num_days)

    project_name = create_project_name(absolute_path)

    print(project_name)

    redis_client = make_redis_client()

    # List to store file names
    file_names = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(absolute_path):
        for file in files:
            file_names.append(file)

    # Print the list of file names
    for file_name in file_names:
        print(file_name)

    # Data to store
    key = project_name
    value = file_names

    # Store data in Redis
    redis_client.mset({key: value})

    # Retrieve and print the stored data
    stored_value = redis_client.get(key)
    print(f"Key: {key}\nStored Value: {stored_value.decode('utf-8')}")

if __name__ == '__main__':
    main()
