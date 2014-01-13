#!/usr/bin/env python
import os
import sys
import glob
import subprocess
from colorama import Fore, Back, Style


def get_repos():
    ret = []
    items = glob.glob(os.path.join(".", "*"))
    for item in items:
        if os.path.isdir(item) and os.path.isdir(os.path.join(item, ".git")):
            ret.append(item)

    ret.sort()
    return ret


def get_git_status(folder):
    curdir = os.path.abspath(os.curdir)
    os.chdir(folder)
    output = subprocess.check_output(["git", "status"])
    output = output.split("\n")[1]
    os.chdir(curdir)

    if output in ("nothing to commit, working directory clean", "# Untracked files:"):
        return "OK"
    elif output in ("# Changes not staged for commit:",):
        return "Pending commit"

    return output


def main():
    previous_dir = os.curdir

    if len(sys.argv) > 1:
        folders = sys.argv[1:]

    for folder in folders:
        os.chdir(folder)
        repos = get_repos()

        print Fore.CYAN + folder, "-", len(repos), "repositories"

        for repo in repos:
            status = get_git_status(repo)
            if status == "OK":
                continue
            elif status == "Pending commit":
                colour = Fore.RED
            else:
                colour = Fore.YELLOW
            print colour + "-", repo[2:].ljust(40), status

    print Fore.RESET + Back.RESET + Style.RESET_ALL
    os.chdir(previous_dir)


if __name__ == "__main__":
    main()

