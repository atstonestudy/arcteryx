from timeloop import Timeloop
from datetime import timedelta
from scrapy.cmdline import execute
from tool import loghandler

tl = Timeloop()

# 爬取rei平台数据
@tl.job(interval=timedelta(minutes=30))
def sample_job_every_180s():
    # print("sample_job_every_30m----")
    loghandler.logger.warning("crawl rei data--------")

    execute(['scrapy', 'crawl', 'rei_arcteryx'])
   

tl.start(block=True)