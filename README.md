# automatic_git_populator
Script that will take a repository and using a language model will create commits that will be regularly posted to github.

## Installing dependencies

1. Install redis on MacOS with `$ brew install redis`
2. Install python dependencies with `$ pip install -r requirements.txt`

Tested with Python 3.11.0.

## Running the script

1. Run redis server in a separate terminal with `$ redis-server`
2. Run the script `$ python main.py --dir_name <dir_name> --freq <freq> --num_days <num_days>`.
