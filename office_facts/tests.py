from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests 
class OfficeFactsTest:


  @classmethod
  def setupTestData(cls):
    testuser1 = get_use_model().objects.create_user(username='testuser1', password= 'password')
    testuser1.save()
  

    testfacts = Office_facts.objects.create(
      author = testuser,
      fact_name = 'green eggs and ham',                                     
      fact_body = 'i love green eggs but not ham because i dont eat mammals',


    )
    testfacts.save()
  
  def test_office_fact_content(self):
    fact = Office_facts.objects.get(id=1)
    actual_author = str(Office_facts.author)
    actual_fact_name = str(Office_facts.fact_name)
    actual_fact_body = str(Office_facts.fact_body)
    self.assertEqaul(actual_author, 'testuser1')
    self.assertEqual(actual_fact_name, 'green eggs and ham')
    self.assertEqual(actual_fact_body, 'i love green eggs but not ham because i dont eat mammals')

 