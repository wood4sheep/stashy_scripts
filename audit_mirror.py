#!/usr/bin/python3
import sys
import os
import stashy
import pprint
import inspect

# Updates commit hook accross all repos in all projects

pp = pprint.PrettyPrinter(indent = 4)
##for i in inspect.getmembers(stash.projects["RES"].repos["asterisk"].settings.hooks.list()):

stash = stashy.connect("GIT_URL", "GIT_USER", "GIT_PASS")

# need to check permissions

for proj in stash.projects.list():
   print(proj["key"])
   for repo in stash.projects[proj["key"]].repos.list():
      #print(str(repo["name"]).replace(' ','+'))
      #pp.pprint(stash.projects[proj["key"]].repos[str(repo["name"]).replace(' ','-')].settings.hooks.list());
      for hook in stash.projects[proj["key"]].repos[str(repo["name"]).replace(' ','-')].settings.hooks.list():
         if (str(hook["configured"]) == "False") and (str(hook["details"]["name"]) == "Push Mirror Repo"):
            print("\t" + str(repo["name"]).replace(' ','+'))




           # print(hook["details"]["name"])

#{   'configured': False,
#    'details': {   'configFormKey': 'com.ngs.stash.externalhooks.external-hooks:external-post-receive-hook-config-form',
#                   'description': 'The External Post Receive Hook Plugin',
#                   'key': 'com.ngs.stash.externalhooks.external-hooks:external-post-receive-hook',
#                   'name': 'External Post Receive Hook',
#                   'type': 'POST_RECEIVE',
#                   'version': '1.3-7'},
#    'enabled': False}

#         if (hook["configured"] == "False"):
#            print(hook["details"]["name"])
  #       if (hook["details"]["name"] == "Push Mirro Repo"):
  #          print(hook["configured"])
  #          print(hook["enabled"])
  #       print(hook["details"]["name"])
         #if (hook["configured"] == "False" and hook["enabled"] == "False" and hook["details"]["name"] == "Push Mirro Repo"):
  #          print("BOO")
           # print(proj["key"]+repo["name"])
         #if (hook.details["name"] == "Push Mirro Repo") and (:
         
  #    pp.pprint(stash.projects[proj["key"]].repos[repo["name"]].permitted);

  #    for i in inspect.getmembers(stash.projects[proj["key"]].repos[repo["name"]].settings.hooks.list()):
 #        if not i[0].startswith('_'):
#         # Ignores methods
#            if not inspect.ismethod(i[1]):
##               print(i)
