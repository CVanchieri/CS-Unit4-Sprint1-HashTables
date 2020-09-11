### Make a web client that fetches URL's ###
## It should cache the resuls of the call

# On 1st request, client fetches the web page
# On 2nd request, client returns from the cache
# On any subsequent request, client returns from the cache

# Why would we make this?
## Speed! dont have to reoad the entire page
## So we dont download images etc again
## Fewer network calls - for security

## How to use hash tables to make a cahce?
### What is the key, whats the value?

### What are we given? use as key
### What are we figuring out? use as value

## key: URL
## Value: web page data
import requests

cache = {}

class Cache_Entry:
    def __init__(self, page):
        self.page = page
        self.time_fetched = time.time()

def client_fetch(url):
    if url in cache:
        print('Web already have this!')
        cache_entry = cache[url]

        if time.time() - cache_entry.time_fetched > TIMEOUT:
            pass
            
        return cache[url]
    else:

        ## otherwise, go get the url
        # urllib.request
        data = requests.get(url).text
        cache[url] = data
        return cache[url]

client_fetch('http://www.google.com')

## Stale data in the cache
### How to solve?
#### put a timestamp on the cached pages and check the timestamp in the if block

## Cache will fill up! use a lot of memory
