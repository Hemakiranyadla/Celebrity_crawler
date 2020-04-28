# Celebrity_crawler
4 steps to extract the data from Imdb.com


## Installation


Clone the repository using:

step 1: git clone https://github.com/dojutsu-user/IMDB-Scraper.git

### Navigate to the folder from terminal:

step 2: $ cd Celebrity_crawler/

Step 3: $ cd imdb_scraper/

### Open Shell 

step 4: $ pipenv shell

Install the frozen environment file:
step 5: $ pipenv install

Navigate to the dictionary where the scrapy spiders are coded:
step 6: cd imdb_scraper/

### Scrape the webpage
Scrape the webpage using the crawl command and download in the required format:

step 7: scrapy crawl -o celeb.csv 
(can be obtained in json/XML/csv just change the .extention) 



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Extracted Data
[Celebrity.csv](https://github.com/Hemakiranyadla/Celebrity_crawler/blob/master/imdb_scraper/celeb.csv)

File consists of 5 attributes scraped from IMDB.com:

1. Name 
2. Profession
3. Dob
4. Image
5. Notable Work
