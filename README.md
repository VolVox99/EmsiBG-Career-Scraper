# Scrape Emsi BG's open job positions 👀

![Home Page](assets/home_page.png)

## Background
[Emsi](https://www.economicmodeling.com/) is a labor market data company with headquarters in Boston and Moscow, Idaho, along with offices in the UK, Europe, India, and other global locations. They serve clients across the US, the UK, Canada, the European Union, and the Asia-Pacific region, helping them clients solve a variety of problems.

They have many [open job positions](https://www.economicmodeling.com/open-positions/) on their website, which many may be interested in. The jobs are grouped by different teams that they belong to, such as legal or marketing. For each group there are multiple different actual job postings.

## Approach 
Using the amazing framework known as [scrapy](https://scrapy.org/), the code scrapes open position data from the Emsi Burning Glass website. The code crawls the site and extracts all of the job postings for the different teams. From there it extracts the details for each posting, which are detailed below.

## Use case
This data can be used to extract various insights. For example, one could sort the jobs by the date posted, and find the jobs that have been open the longest. It would be reasonable to suppose that apply for those jobs would have a higher than average acceptance rage, presuming you meet the qualifications.

The data can also be used to monitor the pace at which different teams are opening new positions. One could examine the change in the number of positions posted on a particular team over time to see if the pace is quickening.

---
## ✔️ Fields Scraped & Example Row
|Job Title                              |Job Description                                                                |Location                  |Department        |Commitment         |Team                 |Team Openings|Date Posted        |URL                                                                        |ID                                  |
|---------------------------------------|---|--------------------------|------------------|-------------------|---------------------|-------------|-------------------|---------------------------------------------------------------------------|------------------------------------|
|Education Success Team Lead            |We are seeking a collaborative, detail-oriented... |Moscow, ID                |Education         |Full Time          |Client Services      |1            |2022-01-05 09:38:43|https://jobs.lever.co/economicmodeling/390d26a0-e45c-4f6d-9bfd-ad7c50da188c|390d26a0-e45c-4f6d-9bfd-ad7c50da188c|

---
## Full data
The full harvested data is available to view and download in multiple different formats.
* [data.csv](assets/data.csv)
* [data.json](assets/data.json)
* [data.xml](assets/data.xml)

---

## 💡 To run the scraper locally 
- Follow the [scrapy installation guide](https://docs.scrapy.org/en/latest/intro/install.html)
- Clone the repository
- `cd` into the EmsiBG directory
-  run 
    ```py 
    scrapy crawl careers -O <output_file>
    ```
See the [scrapy documenation](https://github.com/VolVox99/EmsiBG-Career-Scraper) for more details