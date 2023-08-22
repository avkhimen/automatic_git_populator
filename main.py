import numpy as np
import pandas as pd
import argparse

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

if __name__ == '__main__':
    main()
