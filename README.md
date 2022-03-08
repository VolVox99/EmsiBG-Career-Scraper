# Scrapes [Emsi BG's open job positions](https://www.economicmodeling.com/open-positions/) 👀

![Home Page](assets/home_page.png)

### Using scrapy, we scrape open position data from Emsi's website.

### The already harvested data is available to view and download in two different formats.
* [data.csv](assets/data.csv)
* [data.json](assets/data.json)
* [data.xml](assets/data.xml)


## To run scraper locally 
- Follow the [scrapy installation guide](https://docs.scrapy.org/en/latest/intro/install.html)

## Then Run 
```py 
scrapy crawl careers -O <output_file>
```
