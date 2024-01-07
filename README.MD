# SCRAPY PROJECT
- [SCRAPY PROJECT](#scrapy-project)
  - [Technical](#technical)
  - [Project 1 Transcripts](#project-1-transcripts)
    - [Features](#features)
    - [start](#start)
  - [Project 2 Audible](#project-2-audible)
    - [Features](#features-1)
    - [start](#start-1)
  - [Project 3 Worldometers](#project-3-worldometers)
    - [Features](#features-2)
    - [start](#start-2)
## Technical
>use XPATHS

## Project 1 Transcripts
scraping transcript from [subslikescript](https://subslikescript.com/)
### Features
- simple web scrapy
### start
```bash
scrapy crawl transcripts -o datas/transcripts/output.csv  
```
## Project 2 Audible
scraping information audible books from [audible](https://www.audible.com/search)
### Features
- pagination
### start
>change current_page=1 if you want scrap all page
```bash
scrapy crawl audible -o outputs/audible/output.csv
```
## Project 3 Worldometers
scraping information country from [worldometers](https://www.worldometers.info/world-population/population-by-country/)
### Features
- get data from web data table
### start
```bash
scrapy crawl worldometers -o outputs/worldometers/output.csv
```