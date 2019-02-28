#!/usr/bin/python3
import sys
import os
import stashy

# pulls all git repos from stash

stash = stashy.connect("GIT_URL", "GIT_USER", "GIT_PASS")

for repo in stash.projects[sys.argv[1]].repos.list():
   for url in repo["links"]["clone"]:
       if (url["name"] == "ssh"):
           print('pull\t' + repo["name"] + '\n');
           #cmd = "cd '/root/git/" + sys.argv[1] + "/" + repo["name"].lower() + "'; git branch --set-upstream origin/master; git pull " + url["href"] + " 2>&1"
           cmd = "cd '/root/git/" + sys.argv[1] + "/" + repo["name"].lower().replace(" ", "-")  + "'; git pull 2>&1"
           #os.system("cd %s ; git pull %s" % url["href"])
           os.system(cmd)
           break
