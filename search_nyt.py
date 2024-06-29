

API_KEY = "ocPGtmzAk2JgzyEmO0dZHJxDUIJcBhTo"
API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def search_articles(search_term):
    pass

def display_results(search_results):
    pass

while True:
    search_term = input("Your search term: ")
    search_results = search_articles(search_term)
    display_results(search_results)