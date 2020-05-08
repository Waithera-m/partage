class Quote:

    '''
    class facilitates the creation of quote objects
    '''
    def __init__(self,author,quote):

        '''
        function facilitates the definition of quote properties
        
        Args:
            self.author (str):quote's author
            self.quote (str):actual quote
        '''
        self.author = author
        self.quote = quote