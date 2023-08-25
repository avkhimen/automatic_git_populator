#!/bin/bash

# Get user input for commit message
read -p "Enter commit message: " commit_message

# Define the branch name
branch_name="main"

# Perform Git operations
git add .
git commit -m "$commit_message"
git push origin "$branch_name"

echo "Git operations completed."

