# import datetime as dt
# from django.test import TestCase
# from .models import Location,Image,Category

# class LocationTestClass(TestCase):

#   #set up method
#   def setUp(self):
#       self.moringa=Location(first_name ='Faith', last_name = 'Kazungu', email = 'faithmugesia@gmail.com')
#   def tearDown(self):
#     Location.objects.all().delete
#   # Testing  instance
#   def test_instance(self):
#       self.assertTrue(isinstance(self.moringa,Location))

#       # Testing Save Method
#   def test_save_method(self):
#       self.moringa.save_location()
#       locations = Location.objects.all()
#       self.assertTrue(len(locations) > 0)

#   def test_delete_method(self):
#     self.moringa.delete_location()
#     locations = Location .objects.all()
#     self.assertTrue(len(locations) >0)

# class ImageTestClass(TestCase):

#   def setUp(self):
#       # Creating a new location and saving it
#       self.moringa= Location(first_name = 'Faith', last_name ='Kazungu', email ='faithmugesia@gmail.co')
#       self.moringa.save_location()

#       # Creating a new category and saving it
#   def test_save_method(self):
#     self.moringa.save_category()
#     category = Category.objects.all()
#     self.assertTrue(len(category) >0)

#     self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',location = self.moringa)
#     self.new_image.save()

#     self.new_image.category.add(self.new_category)

#     def tearDown(self):
#         Location.objects.all().delete()
#         Category.objects.all().delete()
#         Image.objects.all().delete()


#     def test_get_image_today(self):
#         today_image = Image.todays_image()
#         self.assertTrue(len(today_image)>0)
    
#     def test_get_image_by_date(self):
#         test_date = '2017-03-17'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         image_by_date = Image.days_news(date)
#         self.assertTrue(len(image_by_date) == 0)
    



