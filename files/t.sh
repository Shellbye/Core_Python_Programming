#!/bin/bash
now=`date +'%Y-%m-%d-%T-%I-%M-%S'`
mv log.log  log.log${now}
touch log.log
mysqldump -u root test > test${now}.sql
