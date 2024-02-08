import subprocess
import shutil
from pathlib import Path
from datetime import datetime

def build_book() -> None:
    command= ["jupyter-book", "build", "notebooks/", "--all"]
    subprocess.run(command, check=True)

def make_book_archive() -> None:
    cwd = Path.cwd()
    base_name = str(cwd / "book" / "build") + f"_{datetime.now(): %Y-%m-%d}"
    base_dir = "notebooks"
    shutil.make_archive(
        base_name= base_name,
        format="gztar",
        base_dir= base_dir
    )

def main() -> int:
    build_book()
    make_book_archive()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())