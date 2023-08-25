# automatic_git_populator
Script that will take a repository and using a language model will create commits that will be regularly posted to github. The script works by specifying the directory name, the frequency of commits, and the number of days over which the commits will take place.

## Considerations

To make sure commits are displayed properly on your github page make sure to specify your name and email:

1. `$ git config --global user.name "FIRST_NAME LAST_NAME"`
2. `$ git config --global user.email "EMAIL"`

## Installing dependencies

1. Install redis on MacOS with `$ brew install redis`
2. Install python dependencies with `$ pip install -r requirements.txt`

Tested with Python 3.11.0.

## Running the script

1. Run redis server in a separate terminal with `$ redis-server`
2. Run the script `$ python main.py --dir_name <dir_name> --freq <freq> --num_days <num_days> --start_date <YYYYMMDD>`.
