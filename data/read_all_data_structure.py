from pathlib import Path

current_dir = Path(".")

for file in current_dir.iterdir():
    if str(file).endswith(".tsv"):
        with open(file, "r") as fd:
            print(f"File '{file}' columns:")
            print("=" * 20)
            print(fd.readline(), end="")
            print(fd.readline(), end="")
            print()
