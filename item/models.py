from django.db import models
from datetime import datetime

# Create your models here.

class CompanyIntroduction(models.Model):
    main_image = models.ImageField(upload_to='intro/main', null=True, blank=True, help_text='Image Size: width=420px, height=568px')
    vision = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)
    strategy = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='intro/', null=True, blank=True, help_text='Image Size: width=220px, height=216px')
    video_url = models.URLField(help_text="Please enter the url of the video from youtube or other sources")

class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=300, null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    slogan = models.CharField(max_length=300, null=True, blank=True)
    facebook_url = models.URLField(help_text="Please enter the url of your company's facebook", null=True, blank=True )
    youtube_url = models.URLField(help_text="Please enter the url of your company's youtube", null=True, blank=True)
    instagram_url = models.URLField(help_text="Please enter the url of your company's instagram", null=True, blank=True)
    twitter_url = models.URLField(help_text="Please enter the url of your company's twitter", null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)


class Stories(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField()
    profession = models.CharField(max_length=300, null=True, blank=True)
    place_name = models.CharField(max_length=300, null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="story/", null=True, blank=True, help_text='Image Size: width=263px, height=271px')

    def __str__(self):
        return self.name

class Message(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class AboutUs(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    video = models.URLField(help_text="Please enter the url of the video from youtube or other sources")
    thumbnail_image = models.ImageField(upload_to='about/', null=True, blank=True, help_text='Image Size: width=559px, height=487px')

class WhatWeDo(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='service/', null=True, blank=True, help_text='Image Size: width=40px, height=40px')

    def __str__(self):
        return self.title

class Service(models.Model):
    image = models.ImageField(upload_to='image/', null=True, blank=True, help_text='Image Size: width=360px, height=249px')
    detail_image = models.ImageField(upload_to='image/detail_img', null=True, blank=True, help_text='Image Size: width=700px, height=350px')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='servdetail')
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='service_detail/', null=True, blank=True, help_text='Image Size: width=40px, height=40px')


class AwardList(models.Model):
    award_title = models.CharField(max_length=200, null=True, blank=True)
    award_description = models.TextField()

    def __str__(self):
        return self.award_title

class Partnership(models.Model):
    company_logo = models.ImageField(upload_to='logo/', null=True, blank=True, help_text='Image Size: width=1459px, height=1042px')
    company_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company_name

class Testimonial(models.Model):
    description = models.TextField()
    person_image = models.ImageField(upload_to='testimonial/', null=True, blank=True, help_text='Image Size: width=250px, height=216px')
    person_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.person_name

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('News', 'News'),
        ('Event', 'Event'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True, help_text='Image Size: width=360px, height=295px')
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class WorkTogether(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='together/', null=True, blank=True, help_text='Image Size: width=1140px, height=515px')

class WorkFor(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text= "short description about the recipe")
    ingredients = models.TextField(null=True,  blank=True)
    recipe_preparation = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='recipe/', null=True, blank=True, help_text='Image Size: width=360px, height=295px')

    def __str__(self):
        return self.recipe_name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self. name

class ProductCategoryDetail(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True, help_text="If rabbit choose anyone")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text="short description")
    price = models.IntegerField(null=True, blank=True, help_text="Rs. per")
    unit = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter the unit eg. kg, piece etc")
    image = models.ImageField(upload_to='meat/', null=True, blank=True, help_text='Image Size: width=360px, height=295px')

    def __str__(self):
        return self.title

class ProductSubImage(models.Model):
    big_image = models.ImageField(upload_to='productsub/', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='productthumb', null=True, blank=True)
    category = models.ForeignKey(ProductCategoryDetail, on_delete=models.CASCADE, related_name='product_category')

class ProductDetail(models.Model):
    category = models.ForeignKey(ProductCategoryDetail, on_delete=models.CASCADE, related_name='detail_product', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Package(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_package', null=True, blank=True)
    package_name = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.package_name

class PackageService(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package', null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)


class Gallery(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)

    def __str__(self):
        return self.title

class QuestionCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='quecategory/', null=True, blank=True, help_text='Image Size: width=700px, height=350px')

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name='quecat', null=True, blank=True)
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question

class Event(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='eventserv', null=True,blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='event/', null=True, blank=True, help_text='Image Size: width=393px, height=272px')
    slogan = models.CharField(max_length=300, null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OrderInfo(models.Model):
    product_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    quantity = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    note = models.TextField()
    
    def __str__(self):
        return self.product_name

class Program(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="program/", help_text='Image Size: width=650px, height=464px')

    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="offer/", help_text='Image Size: width=262px, height=489px')

    def __str__(self):
        return self.title


