#!/bin/bash

# This script commits and pushes changes with an AI-generated commit message.

# 1. Get the diff of the changes.
DIFF=$(git diff HEAD)

# 2. Generate a commit message.
COMMIT_MESSAGE=$(gemini -p "generate commit message based on $DIFF")

# 3. Commit the changes.
git add .
git commit -m "$COMMIT_MESSAGE"

# 4. Push the changes.
git push