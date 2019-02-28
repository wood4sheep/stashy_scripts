#!/usr/bin/python
import sys
import os
import stashy

# clone all repos from stash
  
stash = stashy.connect("GIT_URL", "GIT_USER", "GIT_PASS")

for repo in stash.projects[sys.argv[1]].repos.list():
    for url in repo["links"]["clone"]:
        if (url["name"] == "ssh"):
            os.system("git clone %s" % url["href"])
            break
