#!/bin/bash

rtn=(SUCCESS FAILURE)
TO="root@"
subject="Daily Git backup"

outfile="/root/scripts/git_backup.log"

cd /root/git

dobackup () {

# this is the list of project keys to back up
  pkeys=(RES ADM DEPS)

  date 
  for key in ${pkeys[*]}; 
    do
    echo $key
    cd /root/git/$key
    python3 /root/scripts/clone_all.py $key 2>&1
    rval=$(( rval + $? ))
    python3 /root/scripts/pull_all.py $key 2>&1
    rval=$(( rval + $? ))
  done

  du -sk 
  date 
  return $rval
}

out=$( dobackup )
if [ "$?" -ne "0" ]
  then
  rval=1
fi

echo -e "$out \n\nScript=$0\nPath=$(pwd)\nHost=$(hostname)\nUser=$(whoami)" |tee -a $outfile | mail -s "${rtn[$rval]} $subject" ${TO}
