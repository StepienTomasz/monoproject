#!/bin/bash

# This script manages daily notes. It creates a new note for the current day,
# copies the content from the most recent note, and moves that previous note to the archive.

# Get the current date in YYYYMMDD format
TODAY=$(date +%Y%m%d)
NEW_NOTE_PATH="/Users/tomasz/monoproject/notes/${TODAY}.txt"

# Check if a note for today already exists
if [ -f "$NEW_NOTE_PATH" ]; then
    echo "Note for today ($NEW_NOTE_PATH) already exists."
    exit 0
fi

# Find the most recent note file
LATEST_NOTE=$(ls -1 /Users/tomasz/monoproject/notes/[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].txt 2>/dev/null | sort -r | head -n 1)

if [ -z "$LATEST_NOTE" ]; then
    echo "No previous note found to copy."
    # If no previous note, create a new one from scratch
    echo -e "todo:\n\ndone:\n" > "$NEW_NOTE_PATH"
    echo "Created a new note: $NEW_NOTE_PATH"
else
    # Copy the latest note to the new note file
    cp "$LATEST_NOTE" "$NEW_NOTE_PATH"
    echo "Copied $LATEST_NOTE to $NEW_NOTE_PATH"

    # Archive the latest note
    LATEST_NOTE_FILENAME=$(basename "$LATEST_NOTE")
    YEAR=$(echo "$LATEST_NOTE_FILENAME" | cut -c 1-4)
    ARCHIVE_DIR="/Users/tomasz/projects/notes/04_archive/${YEAR}"

    # Create the archive directory if it doesn't exist
    mkdir -p "$ARCHIVE_DIR"

    # Move the latest note to the archive
    mv "$LATEST_NOTE" "$ARCHIVE_DIR/"
    echo "Archived $LATEST_NOTE to $ARCHIVE_DIR/"
fi