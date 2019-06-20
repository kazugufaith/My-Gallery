# import datetime as dt
# from django.db import models

# class Editor(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)


#     def __str__(self):
#         return self.first_name

#     def save_editor(self):
#         self.save()

#     def delete_editor(self):
#         self.delete()

#     class Meta:
#         ordering = ['first_name']


# class tags(models.Model):
#     cname = models.CharField(max_length=30)

#     def __str__(self):
#        return self.cname

#     class Meta:  # Meta subclass specifies model-specific options. This helps in ordering data
#        verbose_name_plural = 'tags'

#     def save_(self):
#        self.save()

# #class tags(models.Model):
#     #name = models.CharField(max_length =30)

#    # def __str__(self):
#         #return self.name

# class Image(models.Model):
#     title = models.CharField(max_length =60)
#     location = models.CharField(max_length =80)
#     description = models.TextField()
#     editor = models.ForeignKey(Editor)
#     category = models.CharField(max_length =60)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     image_image = models.ImageField(upload_to = 'image/')

#     @classmethod
#     def todays_image(cls):
#         today = dt.date.today()
#         image = cls.objects.filter(pub_date__date = today)
#         return image

#     @classmethod
#     def days_image(cls,date):
#         image = cls.objects.filter(pub_date__date = date)
#         return image

#     @classmethod
#     def search_by_title(cls,search_term):
#         image = cls.objects.filter(title__icontains=search_term)
#         return image