import os
import shutil
import re
import subprocess

# Paths for the Obsidian notes and Quartz notes repositories
OBSIDIAN_NOTES_PATH = "/home/olai/notes/obsidian"
QUARTZ_NOTES_PATH = "/home/olai/devel/quartz_notes/content"
EXCLUDED_FOLDERS = {"Daily", ".obsidian", ".stfolder", ".trash"}
EXCLUDED_TAGS = {"#oppgave", "#innlevering", "#private"}
EXCLUDED_EXTENSIONS = {".excalidraw.md"}

def ignore_files(dir, files):
    """
    Ignore files and folders based on exclusion rules.
    """
    ignored = []

    # Ignore entire folders
    for folder in EXCLUDED_FOLDERS:
        if folder in dir:
            return files  # Ignore everything in this folder

    # Ignore files based on tags and extensions
    for file in files:
        full_path = os.path.join(dir, file)
        if os.path.isfile(full_path):
            # Exclude based on extension
            if any(file.endswith(ext) for ext in EXCLUDED_EXTENSIONS):
                ignored.append(file)
                continue

            # Exclude based on tags
            if file.endswith(".md"):
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if any(tag in content for tag in EXCLUDED_TAGS):
                        ignored.append(file)
    return ignored

def sync_quartz():
    """Runs the Quartz sync command."""
    try:
        subprocess.run(["npx", "quartz", "sync"], cwd=os.path.dirname(QUARTZ_NOTES_PATH), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during Quartz sync: {e}")

def main():
    # Clear the Quartz content folder
    if os.path.exists(QUARTZ_NOTES_PATH):
        shutil.rmtree(QUARTZ_NOTES_PATH)

    # Copy notes with filtering
    shutil.copytree(
        OBSIDIAN_NOTES_PATH,
        QUARTZ_NOTES_PATH,
        ignore=ignore_files
    )

    # Sync Quartz
    sync_quartz()

if __name__ == "__main__":
    main()
