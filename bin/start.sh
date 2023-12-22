#!/bin/bash
nohup python3 main.py >log/log.log 2>&1 &

# start 1
nohup python3 notice_main.py >log/notice.log 2>&1 &
# start 2
nohup python3 spider_main.py >log/spider.log 2>&1 &
 
# # just keep this script running
# while [[ true ]]; do
#     sleep 1
# done