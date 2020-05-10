import unittest
from app.models import Quote




class TestModelQuote(unittest.TestCase):

    '''
    class inherits from TestCase class and facilitates the development of test units to test Quote class' behavior
    '''
    def setUp(self):

        '''
        function executes before every test
        '''
        self.new_quote = Quote(1,'Terry Pratchett','Studies have shown that an ant can carry one hundred times its own weight, but there is no known limit to the lifting power of the average tiny eighty-year-old Spanish peasant grandmother')

    def test_instance(self):

        '''
        function checks if new quote is initialized properly
        '''
        self.assertTrue(isinstance(self.new_quote,Quote))
    
    def test_instance_variables(self):

        '''
        function checks if quote variables are initialized properly
        '''
        self.assertEqual(self.new_quote.id,1)
        self.assertEqual(self.new_quote.author,'Terry Pratchett')
        self.assertEqual(self.new_quote.quote,'Studies have shown that an ant can carry one hundred times its own weight, but there is no known limit to the lifting power of the average tiny eighty-year-old Spanish peasant grandmother')