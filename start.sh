#!/bin/bash
# # start 1
echo  "step1"
python3 ./notice_main.py &
echo  "step2"
python3 ./spider_main.py 
echo  "step3"
# # start 2
# nohup python3 ./spider_main.py >log/spider.log 2>&1 &

# python3 ./notice_main.py
# python3 ./spider_main.py 
# just keep this script running
# while [[ true ]]; do
#     sleep 1
# done