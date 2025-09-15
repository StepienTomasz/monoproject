
import os
import subprocess
import glob
from datetime import date

def main():
    notes_dir = "/Users/tomasz/monoproject/notes/"
    readme_files = glob.glob(os.path.join(notes_dir, "**/README.md"), recursive=True)

    all_readmes_content = []
    for readme_file in readme_files:
        with open(readme_file, "r") as f:
            all_readmes_content.append(f.read())

    if not all_readmes_content:
        print("No README.md files found in the notes directory.")
        return

    prompt = f"""
Based on the following project descriptions, create a prioritized to-do list for today, {date.today().strftime('%Y-%m-%d')}.
Focus on tasks that will move each project forward. Group the tasks by project.

Here are the project descriptions:
---
{"---\n".join(all_readmes_content)}
---
"""

    try:
        result = subprocess.run(
            ["gemini", "-p", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        task_list = result.stdout
    except FileNotFoundError:
        print("Error: 'gemini' command not found. Make sure it's in your PATH.")
        return
    except subprocess.CalledProcessError as e:
        print(f"Error running gemini command: {e}")
        print(f"Stderr: {e.stderr}")
        return

    today_str = date.today().strftime("%Y%m%d")
    output_file = os.path.join(notes_dir, f"daily_tasks_{today_str}.txt")

    with open(output_file, "w") as f:
        f.write(task_list)

    print(f"Successfully generated daily tasks and saved to {output_file}")

if __name__ == "__main__":
    main()
