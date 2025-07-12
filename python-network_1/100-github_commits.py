#!/usr/bin/python3
"""
This script uses the GitHub API to list 10 most recent commits
from a given repository and owner.
Usage: ./100-github_commits.py <repository> <owner>
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    except Exception:
        pass
