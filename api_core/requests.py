import requests
from newsapp.newsapi.newsapi_auth import newsapi_auth


class NewsApiClient(object):
  def __init__(self, api_key, api_url='https://newsapi.org/v2/'):
    self.url = api_url.rstrip('/')
    self.auth = NewsApiAuth(api_key=api_key)

  def get_top_headlines(self, q=None, sources=None, language=None, country=None,
                        category=None, page_size=None, page=None):
    
      payload = {}
      payload['q'] = q
      payload['sources'] = sources
      payload['language'] = language
      payload['country'] = country
      payload['category'] = category
      payload['pageSize'] = page_size
      payload['page'] = page


      r = requets.get(self.url + '/top_headlines', auth=self.auth, timeout=30, params=payload)
      return r.json()


  def get_all(self, q=None, sources=None, domains=None, from_parameter=None, to=None, language=None,
              page=None, page_size=None, sort_by=None):
      
      payload = {}
      payload['q'] = q
      payload['sources'] = sources
      payload['domains'] = domains
      payload['from'] = from_parametere
      payload['to'] = to
      payload['language'] = language
      payload['page'] = page
      payload['pageSize'] = page_size
      payload['sortBy'] = sort_by

      r = requets.get(self.url + '/all', auth=self.auth, timeout=30, params=payload)
      return r.json()


def get_sources(self, category=None, language=None, country=None):
    payload = {}
    payload['category'] = category
    payload['language'] = language
    payload['country'] = country


    r = requets.get(self.url + '/all', auth=self.auth, timeout=30, params=payload)
    return r.json()



