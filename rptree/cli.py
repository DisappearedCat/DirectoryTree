import argparse
import pathlib
import sys

from . import  __version__
from .rptree import DirectoryTree

def main():
    args = parse_cmd_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exits")
        sys.exit()
    tree = DirectoryTree(root_dir)
    tree.generate()

def parse_cmd_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="A directory three generator",
        epilog="Thanks for using!"
    )
    parser.version = f"{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument("root_dir", metavar="ROOT_DIR", nargs="?", default=".", help="Generate a full directory"
                                                                                     "starting at ROOT_DIR")
    return parser.parse_args()