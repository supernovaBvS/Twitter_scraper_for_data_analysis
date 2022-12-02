# Twitter_scraper_for_data_analysis
twitter scraper for data analysis (development)

## GOALS
- Use python to scrap tweets with keyword:  #ANYWORD
- Collect tweets from ANY time interval
- Make analysis on tweet data 

## Workflow
1. Communicate and consider our users requirement
2. Scrape tweets base on the time period 
3. Store the tweet data into SQL Database
4. Make analysis on tweet data


<img width="678" alt="Screenshot 2022-12-02 at 10 08 14 PM" src="https://user-images.githubusercontent.com/112676063/205311317-d7aa8a72-1b00-496c-b262-498be6b774b3.png">

## Database Schema
The scraped twitter data will be loaded and stored in a MySQL database table:
- Username
- Date
- TweetURL
- User
- Source
- Location
- Tweet
- Likes_Count
- Retweet_Count
- Quote_Count
- Reply_Count

## Data Pineline

### The LIBRARY we will be using
<pre><code>import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import snscrape.modules.twitter as sntwitter
from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine
from transformers import pipeline
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import spacy as sp
from pysentimiento import create_analyzer
import datetime
import radar 
import emoji
</code></pre>

## Data Visualisation
<img width="673" alt="Screenshot 2022-12-02 at 10 08 27 PM" src="https://user-images.githubusercontent.com/112676063/205311352-20115003-a2f2-4cfb-a3a9-faee3e2a2dd3.png">
<!-- 
### Pie Chart
<kbd>
<img width="325" alt="螢幕截圖 2022-10-09 下午9 25 33" src="https://user-images.githubusercontent.com/112631794/199660414-d526569b-8e9f-4c1c-91c9-da8576d49e67.png">
</kbd>

### Word Cloud
<kbd>
  <img width="325" height="180" alt="螢幕截圖 2022-10-09 下午9 26 21" src="https://user-images.githubusercontent.com/112631794/199660669-df10eff2-592d-49ca-a3c9-381ace87c6d2.png"> <img width="325" height="180" alt="螢幕截圖 2022-10-09 下午9 26 56" src="https://user-images.githubusercontent.com/112631794/199660687-ad76f082-8766-4c35-93d0-c2e4fd277dd5.png"> <img width="325" height="180" alt="螢幕截圖 2022-10-09 下午9 27 26" src="https://user-images.githubusercontent.com/112631794/199660720-c1d8f4c0-2606-4804-aaea-2e2059203cd5.png">
</kbd>

### 100% stacked column chart
<kbd>
<img width="990" alt="螢幕截圖 2022-10-09 下午9 24 45" src="https://user-images.githubusercontent.com/112631794/199664103-ae8b227f-b282-485f-93d0-879ea2d1536b.png">
</kbd> -->

## Sentiment Analysis
### Machine learning 
<img width="676" alt="Screenshot 2022-12-02 at 10 08 19 PM" src="https://user-images.githubusercontent.com/112676063/205311473-498131a6-9276-479f-9e7a-160b6fe6c3ab.png">


## Contributers
- [Allen Kong](https://www.linkedin.com/in/allen-kong-21568b250/)
- [Bobby Pany](https://www.linkedin.com/in/bobby-pang-398104245/)
- [Brian Cheng](https://github.com/BrianCheng25)
- [Gordon Kwok](https://www.linkedin.com/in/gordonkwokch/)
