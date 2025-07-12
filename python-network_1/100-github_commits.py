#!/usr/bin/python3
"""
This script fetches and prints the 10 most recent commits of a repository
using the GitHub API.

Usage:
    ./100-github_commits.py <repository_name> <owner_name>
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    except Exception:
        pass
