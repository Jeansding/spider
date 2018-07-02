cd .
@echo on
set /a hour=%time:~0,2%
set /a min=time:~3,2%
set /a sec=%time:~6,2%

set filename=%date:~0,4%%date:~5,2%%date:~8,2%%hour%%min%%sec%
scrapy crawl Wechat>>./log/%filename%.log
pause