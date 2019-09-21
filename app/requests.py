# import urllib.request,json
# from .models import Weather


# def get_quotes():
#     base_url = 'http://quotes.stormconsultancy.co.uk/random.json'
#     '''
#     Function that gets the json response to our url request
#     '''
#     with urllib.request.urlopen(base_url) as url:
#         get_quote_response = json.loads(url.read())

#         quote_results = None

#         if get_quote_response:
#             quote_results = process_results(get_quote_response)

#     return quote_results


# def process_results(quote_item):
#     '''
#     Function  that processes the quote result and transform them to a list of Objects
#     Args:
#         quote_item: A single quote with quote details
#     Returns :
#         quote_object
#     '''
#     id = quote_item.get('id')
#     author = quote_item.get('author')
#     quote = quote_item.get('quote')

#     quote_object = Quote(id, author,quote)

#     return quote_object
