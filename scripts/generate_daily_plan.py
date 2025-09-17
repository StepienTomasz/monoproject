
import os
import subprocess
import glob
from datetime import date, timedelta
import pathlib
import shutil

def main():
    monorepo_root = pathlib.Path("/Users/tomasz/monoproject")
    notes_dir = monorepo_root / "notes"
    archive_dir = notes_dir / "_archive"
    scripts_dir = monorepo_root / "scripts"

    # 1. Find the most recent daily tasks file
    today = date.today()
    today_str = today.strftime("%Y%m%d")
    output_file = notes_dir / f"daily_tasks_{today_str}.txt"

    if output_file.exists():
        print(f"Daily plan for today ({output_file.name}) already exists.")
        return

    task_files = sorted(notes_dir.glob("daily_tasks_*.txt"), reverse=True)
    latest_task_file = task_files[0] if task_files else None

    previous_day_content = ""
    if latest_task_file:
        print(f"Found previous task file: {latest_task_file.name}")
        with open(latest_task_file, "r") as f:
            previous_day_content = f.read()

    # 2. Read all README.md files from the entire monorepo
    readme_files = glob.glob(os.path.join(monorepo_root, "**/README.md"), recursive=True)
    all_readmes_content = []
    for readme_file in readme_files:
        # Exclude READMEs from virtual environments or other irrelevant dirs
        if ".venv" in readme_file or ".git" in readme_file:
            continue
        with open(readme_file, "r") as f:
            all_readmes_content.append(f"--- {os.path.basename(os.path.dirname(readme_file))} README ---{f.read()}")

    if not all_readmes_content:
        print("No README.md files found in the monorepo.")
        # Still proceed to allow carrying over sections from previous day

    readmes_agg = "\n\n".join(all_readmes_content)

    # 3. Construct the prompt
    prompt = f"""Today is {today.strftime('%A, %B %d, %Y')}.

I need you to act as an AI Project Manager and generate a daily plan by intelligently combining information from multiple sources.

**Source 1: Previous Day's Plan**
This is the content from yesterday's task file. It may contain recurring sections like 'Meetings', 'Admin', or sections for completed tasks like 'Done'.

--- PREVIOUS DAY'S PLAN ---
{previous_day_content}
--- END PREVIOUS DAY'S PLAN ---


**Source 2: Project READMEs**
This is a collection of all README.md files from the monorepo, providing context on each project's goals.

--- PROJECT READMES ---
{readmes_agg}
--- END PROJECT READMES ---


**Your Task:**

Create a new daily plan for today with the following two-part structure:

1.  **Project-Specific Tasks (Generated):**
    -   Analyze the **PROJECT READMES** exclusively.
    -   Create a prioritized, project-focused to-do list for today.
    -   Group the tasks by project name. This section should be generated from scratch based on the project goals.

2.  **Recurring & Copied Sections:**
    -   Analyze the **PREVIOUS DAY'S PLAN**.
    -   Identify all sections that are **not** project-specific to-do lists (e.g., 'Meetings', 'Admin', 'Done', 'Follow-up').
    -   Copy these sections and their entire content verbatim into the new plan.

Combine these two parts into a single, coherent daily plan for today.
"""

    # 4. Run Gemini CLI
    try:
        print("Generating new daily plan with Gemini...")
        result = subprocess.run(
            ["/opt/homebrew/bin/gemini", "-p", prompt],
            capture_output=True,
            text=True,
            check=True,
            cwd=monorepo_root
        )
        new_task_list = result.stdout
        print("Successfully received response from Gemini.")
    except FileNotFoundError:
        print("Error: 'gemini' command not found. Make sure it's in your PATH.")
        return
    except subprocess.CalledProcessError as e:
        print(f"Error running gemini command: {e}")
        print(f"Stderr: {e.stderr}")
        return

    # 5. Write the new tasks file
    with open(output_file, "w") as f:
        f.write(new_task_list)
    print(f"Successfully generated daily plan and saved to {output_file.name}")

    # 6. Archive the previous tasks file
    if latest_task_file:
        archive_year_dir = archive_dir / str(latest_task_file.name[12:16])
        archive_year_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(latest_task_file, archive_year_dir / latest_task_file.name)
        print(f"Successfully archived {latest_task_file.name} to {archive_year_dir}")

if __name__ == "__main__":
    main()
