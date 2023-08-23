import numpy as np
import pandas as pd
import argparse
import redis

from utils.formats import DATA_FORMATS
from utils.storage_utils import make_redis_client

def main():
    parser = argparse.ArgumentParser(description="Input variables")
    parser.add_argument("--dir_name", required=True, type=str, help="Path to directory")
    parser.add_argument("--freq", required=True, type=float, choices=[0.5, 1.0, 1.5, 2.0], help="How often to commit")
    parser.add_argument("--num_days", required=True, type=int, help="How many days to spend committing")

    args = parser.parse_args()

    dir_name = args.dir_name
    freq = args.freq
    num_days = args.num_days

    print(dir_name, freq, num_days)

    redis_client = make_redis_client()

    # Data to store
    key = 'my_key'
    value = 'Hello, Redis!'

    # Store data in Redis
    redis_client.set(key, value)

    # Retrieve and print the stored data
    stored_value = redis_client.get(key)
    print(f"Key: {key}\nStored Value: {stored_value.decode('utf-8')}")

if __name__ == '__main__':
    main()
