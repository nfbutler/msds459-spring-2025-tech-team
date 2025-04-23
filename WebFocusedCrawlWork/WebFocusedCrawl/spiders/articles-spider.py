# Scrape Wikipedia, saving page html code to wikipages directory 
# Most Wikipedia pages have lots of text 
# We scrape the text data creating a JSON lines file items.jl
# with each line of JSON representing a Wikipedia page/document
# Subsequent text parsing of these JSON data will be needed
# This example is for a list of companies in the Materials sector
# Replace the urls list with appropriate Wikipedia URLs
# for your team's industry sector of interest

# ensure that NLTK has been installed along with the stopwords corpora
# pip install nltk
# python -m nltk.downloader stopwords

import scrapy
import os.path
from WebFocusedCrawl.items import WebfocusedcrawlItem  # item class 
import nltk  # used to remove stopwords from tags
import re  # regular expressions used to parse tags

def remove_stopwords(tokens):
    stopword_list = nltk.corpus.stopwords.words('english')
    good_tokens = [token for token in tokens if token not in stopword_list]
    return good_tokens     

class ArticlesSpider(scrapy.Spider):
    name = "articles-spider"

    def start_requests(self):
        allowed_domains = ['en.wikipedia.org'] 
        # list of Wikipedia URLs for topic of interest
        # top ten companies in the industry sector (Materials)
        # urls = [
        #     "https://en.wikipedia.org/wiki/Linde_plc",
        #     "https://en.wikipedia.org/wiki/Sherwin-Williams",
        #     "https://en.wikipedia.org/wiki/Ecolab",
        #     "https://en.wikipedia.org/wiki/Southern_Copper_Corporation",
        #     "https://en.wikipedia.org/wiki/Air_Products",
        #     "https://en.wikipedia.org/wiki/CRH_plc",
        #     "https://en.wikipedia.org/wiki/Newmont",
        #     "https://en.wikipedia.org/wiki/Freeport-McMoRan",
        #     "https://en.wikipedia.org/wiki/Corteva",
        #     "https://en.wikipedia.org/wiki/Vulcan_Materials_Company"
        #     ]
        urls = [
                "https://en.wikipedia.org/wiki/Mistral_AI",
                "https://en.wikipedia.org/wiki/Cohere",
                "https://en.wikipedia.org/wiki/Aleph_Alpha",
                "https://en.wikipedia.org/wiki/LightOn",
                "https://en.wikipedia.org/wiki/Writer_Inc",
                "https://en.wikipedia.org/wiki/Runway_(company)",
                "https://en.wikipedia.org/wiki/Synthesia_(company)",
                "https://en.wikipedia.org/wiki/LangChain"
            ]    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # scraping and parsing commands are designed for Wikipedia
    # revisions will likely be needed for other websites
    def parse(self, response):
        # first part: save wikipedia page html to wikipages directory
        page = response.url.split("/")[4]
        page_dirname = 'wikipages'
        filename = '%s.html' % page
        with open(os.path.join(page_dirname,filename), 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename) 

        # second part: extract text for the item for document corpus
        item = WebfocusedcrawlItem()
        item['url'] = response.url
        item['title'] = response.css('h1::text').extract_first()
        item['text'] = response.xpath('//div[@id="mw-content-text"]//text()')\
                           .extract()                                                             
        tags_list = [response.url.split("/")[2],
                     response.url.split("/")[3]]
        more_tags = [x.lower() for x in remove_stopwords(response.url\
                       	    .split("/")[4].split("_"))]
        for tag in more_tags:
            tag = re.sub('[^a-zA-Z]', '', tag)  # alphanumeric values only  
            tags_list.append(tag)
        item['tags'] = tags_list                 
        return item 
