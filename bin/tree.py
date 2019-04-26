#! python3
from pathlib import Path

cwd  = Path.cwd()

def tree(path,depth=0):
    for child in path.iterdir():
        if child.is_dir():
            tree(child,depth+1)
        else:
            print("    "*depth+str(child.name))

if __name__ == "__main__":
    tree(cwd)