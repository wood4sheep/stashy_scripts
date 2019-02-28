#!/usr/bin/python3
import sys
import os
import stashy
import subprocess

# Clones all repos given a stash project

errorCount = 0
stash = stashy.connect("GIT_URL", "GIT_USER", "GIT_PASS")

for repo in stash.projects[sys.argv[1]].repos.list():
   for url in repo["links"]["clone"]:

# Choose ssh over http
       if (url["name"] == "ssh"):
#           os.system("git clone %s 2>&1 |grep -v 'is not an empty directory' " % url["href"].lower() )
# Adding checks
#           cmd = "/usr/bin/git clone " + url["href"].lower() + ' 1>&2'
           cmd = "/usr/bin/git clone " + url["href"].lower() 

           out = ""
           err = ""
           rtn = "failure"

           print('clone\t' + repo["name"] )
       
           try:
# Google says use pipe instead of check_output, esp with shell.
               output = subprocess.check_output(
                   cmd, stderr=subprocess.STDOUT, shell=True, timeout=30,
                   universal_newlines=True)
           except subprocess.CalledProcessError as exc:
# Success if already cloned, better to test for last update and .git/config
               if str(exc.output).find("already exists") != -1:
                   print("already exists")
                   pass
               else:
                   print("Status : FAIL", exc.returncode, exc.output)
                   rtn = "failure"
                   errorCount = errorCount + 1
                   pass
           else:
               print("Output: \n" + str(output))
           sys.stdout.flush()
       #    print("I/O error:" )
       #    proc = subprocess.Popen(['/usr/bin/git', 'clone', url["href"].lower()], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      #     out, err = proc.communicate()
      #     proc_status = proc.wait()
       #    print('out:'+out) 
       #    print('err:'+err) 
       #    print('proc_status:'+str(proc_status)) 
       #    if proc_status != 0:
       #        if re.search ( r'already exists and is not an empty directory', err, re.M|re.I):
       #            rtn = "success"
       #        else:
       #            rtn = "failure"
       #            errorCount = errorCount + 1
       #    else:
       #        rtn = "success"
       #    print(rtn + '\n' + out);

#       break
exit(errorCount)
