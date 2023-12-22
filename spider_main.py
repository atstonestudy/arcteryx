from timeloop import Timeloop
from datetime import timedelta
from scrapy.cmdline import execute
from tool import loghandler
from tool.conf import baseconf
from dbutil.mongoagent import mongo_agent
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import datetime
import subprocess


def job_function():
    print(datetime.datetime.now())
    # execute(['scrapy', 'crawl', 'rei_arcteryx'])
    subprocess.Popen('scrapy crawl rei_arcteryx',shell=True)

def main():

    mongo_agent.initdb(baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"],baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"])
    scheduler = BlockingScheduler()
    scheduler.add_job(job_function, trigger=IntervalTrigger(minutes=baseconf["appconf"]["spiderfq"], timezone="Asia/Shanghai"))
    scheduler.start()


main()