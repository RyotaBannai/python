# coding= utf-8

from pathlib import Path
if __name__ == "__main__":
  # Path.glob()
  # Path('.').glob('**/*.py') ->  “this directory and all subdirectories of cur dir, recursively”
  # Path('.').glob('*/*.py') -> any python file can match that exists under any dir under cur dir.
  print(list(Path('.').glob('*/*.py'))) 