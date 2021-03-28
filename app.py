# 7f45e57cdcb84b11a3d26bc019d5cc58

# pip install newsapi-python
from newsapi.newsapi_client  import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key='7f45e57cdcb84b11a3d26bc019d5cc58')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-03-01',
                                      to='2021-03-28',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)



# /v2/sources
sources = newsapi.get_sources()
print(json.loads(str(sources)))
