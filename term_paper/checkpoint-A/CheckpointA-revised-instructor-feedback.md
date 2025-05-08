Here's a revised version of your Checkpoint A report that incorporates the teacher's feedback and comments:

---

**Checkpoint A: Topic Choice, Initial Schema Definition, and Likely Data Sources**  
**MSDS 459 Technology Sector Team**  
**Nick Butler, Michael Rivera, and Richard Pereira**  
**April 27, 2025**

### ABSTRACT

This report outlines the early stages of a research project aimed at developing a knowledge graph and web-crawling framework focused on media measures related to publicly traded technology companies. The project specifically targets the ability to monitor and predict market movements based on media signals tied to the ~Generative AI domain and related sectors~. _**TODO: pick specific companies in the tech sector**_. The management problem motivating this research is the challenge companies face in extracting actionable insights from a diverse range of data sources. By creating a graph-based knowledge base that unifies financial, technical, and media information, this project aims to enable effective market predictions based on structured media measures.

### 1\. INTRODUCTION

The fast-paced nature of innovation in the technology sector, particularly around Generative AI, makes it increasingly difficult for companies to react proactively to competitive shifts. Understanding how media signals can predict market performance is critical for corporate strategists, market intelligence analysts, and product managers. The core management question guiding this research is: **How can a technology company utilize media measures to predict market movements of publicly traded firms?**

To address this question, the project proposes a knowledge base that integrates structured and unstructured data into a coherent framework aimed at enabling predictive analytics related to market behavior. The knowledge base will track media signals such as news articles, product announcements, and financial performance relevant to established firms in the sector, ensuring a focus on measurable outcomes.

### 2\. LITERATURE REVIEW

This research is grounded in web data mining and knowledge graph construction. Foundational work by Chakrabarti, van den Berg, and Dom (1999) introduced focused crawling—a strategic method for retrieving topic-relevant content from the web. Their proposed architecture includes a crawler, a distiller (to prioritize high-value pages), and a classifier for evaluating content relevance. These components are essential for navigating the vast online information landscape.

Building on this, Chakrabarti (2003) explores discovering knowledge from hypertext data. The methodologies outlined in this work have influenced our crawler and knowledge base schema design, and practical guidance from sources like Mitchell (2018) and Hajba (2018) will aid in the implementation of web scraping using Python frameworks like Scrapy and BeautifulSoup.

### 3\. METHODOLOGY

#### Topic Selection

The research will now concentrate on tracking publicly traded technology firms rather than emerging Generative AI companies. This decision ensures that we can develop a viable predictive model within the project timeline. The revised focus supports decision-making by enabling insights into established firms with available stock price data.

#### Schema Design

The knowledge base will follow a graph-relational structure designed for implementation in EdgeDB or a similar platform. The node types include:

*   **Company**: Publicly traded technology firms
*   **Product**: Significant products developed by these firms
*   **Patent**: Relevant patent filings
*   **News Article**: Unstructured media content
*   **Financial Event**: Earnings reports, funding rounds, or stock movements
*   **Market Performance**: Historical stock prices and performance indicators

**Relationships** will include:

*   Company to Product (develops)
*   Company to Patent (holds or files)
*   Company to News Article (mentioned in)
*   Company to Financial Event (experiences)
*   Company to Market Performance (associated with)

This revised schema allows for effective querying and facilitates the integration of data that supports our goal of using media measures to predict market movement.

### 4\. DATA SOURCES AND COLLECTION

The team has identified 24 trusted sources of structured and unstructured data, categorized as follows:

*   **Financial Data**: Yahoo Finance, SEC EDGAR, company investor sites
*   **Company Data**: Crunchbase, PitchBook
*   **News Data**: TechCrunch, Wired, The Verge, IEEE Spectrum
*   **Market Performance**: Historical stock data from Yahoo Finance and Google Finance
*   **Trends**: Google Trends, McKinsey reports

Initial data collection is being conducted using Python-based tools like Scrapy and BeautifulSoup. Extracted content will be stored in JSON Lines format, ensuring each entry includes metadata such as source URL, publication date, and content body.

### 5\. USER NEEDS AND QUESTIONS

**Primary users** of this knowledge base include corporate strategists and analysts focused on market performance. Anticipated user questions include:

*   How do media signals correlate with stock price movements for Company X?
*   Which firms are mentioned most frequently in the media in relation to their stock performance?
*   What trends in product announcements correlate with positive stock performance?
*   How do funding announcements impact stock prices in the technology sector?

### 6\. APPLICATION USEFULNESS

The envisioned application will provide capabilities including information retrieval, question answering, and personalized recommendations based on media measures. Users will be equipped to analyze media data and its relation to stock performance, allowing organizations to respond proactively to shifts in market dynamics.

### 7\. RESULTS

To date, the team has made progress in defining the schema and identifying relevant data sources. Preliminary crawling tests on Yahoo Finance and TechCrunch have confirmed the feasibility of automated data extraction, capturing essential article metadata and financial data for the knowledge base.

Challenges noted include data formatting inconsistencies in unstructured sources and the limitations imposed by some financial websites. To address these issues, the team is evaluating the use of Selenium or Puppeteer for more complex scraping needs.

### 8\. CONCLUSIONS

This research aims to enhance technology companies' capabilities to monitor market movements by developing a unified knowledge base that integrates structured and unstructured data. Our refined focus on public companies will enable the development of a predictive model that aligns with the goals of this term project. By addressing the management problem directly, we will facilitate effective market insights and strategic decision-making for our users.

---

### APPENDIX A – Data Sources Table

\[Data sources table remains the same as provided in the original report.\]

---

This revised version incorporates the teacher's feedback, clarifying the project focus, enhancing the methodology, and establishing a clear path toward achieving the project's goals within the constraints of the course timeline. 