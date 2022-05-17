import urllib.request,json
# import requests

# from .models import Quote
base_url = None



def configure_requests(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

    # return requests.get(url).json()
    
def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quote_url ='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
    return get_quote_response

