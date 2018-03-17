
from django.test import TestCase
from . models import Neighbourhood,Profile, Business

class NeighbourTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighborhood_name = 'ugwaro', neighborhood_location ='kikuyu', occupants_count = 1)

    def test_isInstance(self):
        '''
        Checks if an object is an instance 
        '''
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood)) 

    def test_create_neighborhood(self):
        '''
        Tests if the save_neighborhood function works
        '''
        self.neighbourhood.create_neighborhood()
        neighborhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)

    def test_delete_neighborhood(self):
        '''
        Test the delete_neighborhood method
        '''
        self.neighbourhood.save()
        self.neighborhood2 = Neighbourhood(neighborhood_name = 'gardens', neighborhood_location ='kikuyu', occupants_count = 1)
        self.neighborhood2.save()
        self.neighbourhood.delete_neighborhood()
        neighborhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighborhoods)==1)

    def test_update_neighborhood(self):
        '''
        Test the update_neighborhood method
        '''
        self.neighbourhood.save()
        self.neighbourhood.update_neighborhood('kikuyu','california',1)
        self.neighbourhood.save()
        updated_neighborhood = Neighbourhood.objects.get() 
        self.assertTrue(updated_neighborhood.neighborhood_name == 'kikuyu',updated_neighborhood.occupants_count == 1)

    def test_find_neigborhood(self):
        '''
        Test the find_neighborhood method using the neighbourhood id 
        '''
        pass

class User_ProfileTestClass(TestCase):
    '''
    A class that test the User_ class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.profile = Profile(name = 'Brandford', id=1, email= 'brandford@rocketmail.com')

    def test_isInstance(self):
        '''
        Test if the creted object is an instance of the User_profile model
        '''
        self.assertTrue(isinstance(self.profile,Profile))

class BusinessTestClass(TestCase):
    '''
    A class that test the User_ class model
    '''

    def setUp(self):
        '''
        method that runs at the begginning of each test
        '''
        self.business = Business(business_name = 'Business_name', business_email= 'business@rocketmail.com')

    def test_isInstance(self):
        '''
        Test if the object is an instance of the Business model
        '''
        self.assertTrue(isinstance(self.business,Business))

    def test_create_business(self):
        '''
        Test the create business  method 
        '''
        self.business.create_business()
        found_businesses = Business.objects.all()
        self.assertTrue(len(found_businesses)==1)

    def test_delete_business(self):
        '''
        Test the delete business method
        '''
        self.business.save()
        business2 = Business(business_name = 'Business_name2', business_email= 'business2@rocketmail.com')
        business2.save()
        self.business.delete_business()
        found_businesses = Business.objects.all()
        self.assertTrue(len(found_businesses)==1)

    def test_update_business(self):
        '''
        Tests the update_business method
        '''
        self.business.save()
        self.business.update_business('Business_name2','business2@rocketmail.com')
        self.business.save()
        self.assertTrue(self.business.business_name == 'Business_name2',self.business.business_email =='business2@rocketmail.com')

    def test_find_business(self):
        '''
        Tests the find business method using an id
        '''
        pass

    def test_search_business(self):
        '''
        Tests the search business method
        '''
        self.business.save()
        found_business = Business.search_business('Business_name')
        self.assertTrue(found_business.business_name == 'Business_name')