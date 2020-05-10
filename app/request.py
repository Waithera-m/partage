# import urllib.request,json
# from .models import Quote

# quote_url = None

# def configure_request(app):

#     '''
#     function assigns quote_url the url value defined in config.py
#     '''
#     global quote_url

#     quote_url = app.config['QUOTE_URL']

#     print(quote_url)
#     print('hey')


# def get_quote():

#     '''
#     function uses the provides api to get a single random quote
#     '''
#     with urllib.request.urlopen(quote_url) as url:
#         get_quote_data = url.read()
#         get_quote_response = json.loads(get_quote_data)
    
#         quote_object = None
#         if get_quote_response:
#             id = get_quote_response.get('id')
#             author = get_quote_response.get('author')
#             quote = get_quote_response.get('quote')

#             quote_object = Quote(id,author,quote)
    
#     return quote_object
    
