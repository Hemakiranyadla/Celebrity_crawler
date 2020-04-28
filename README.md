# Celebrity_crawler
Celebrity Crawler 

4 steps to extract the data from Imdb.com
Clone the dictionary using:
step 1: https://github.com/Hemakiranyadla/Celebrity_crawler.git

Navigate to the folder from terminal:
step 2: $ cd Celebrity_crawler/
Step 3: $ cd imdb_scraper/

Open Shell 
step 4: $ pipenv shell

Install the frozen environment file:
step 5: $ pipenv install

Navigate to the dictionary where the scrapy spiders are coded:
step 6: cd imdb_scraper/

Scrape the webpage using the crawl command and download in the required format:
step 7: scrapy crawl -o celeb.csv 
(can be obtained in json/XML/csv just change the .extention) 
