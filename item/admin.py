from django.contrib import admin
from . models import CompanyIntroduction, CompanyDetail, Stories, Message, AboutUs, Service, AwardList, Partnership, Testimonial, Blog, WorkTogether, Recipe, Category, CategoryDetail, Package, PackageService, Gallery, GalleryCategory, QuestionCategory, Question, ServiceDetail, Event, OrderInfo, WhatWeDo, Program, Offer, WorkFor, ProductSubImage, ProductDetail, Tour, TourDetailItinerary, IncludedCost

# Register your models here.

class PackageServiceInline(admin.TabularInline):
    model = PackageService
    extra = 4

class PackageAdmin(admin.ModelAdmin):
    inlines = [ PackageServiceInline, ]

class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 3

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ ServiceDetailInline, ]

class ProductSubImageInline(admin.TabularInline):
    model = ProductSubImage
    extra = 3

class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 3

class ProductSubAdmin(admin.ModelAdmin):
    inlines = [ ProductSubImageInline, ProductDetailInline, ]

class TourDetailInline(admin.TabularInline):
    model = TourDetailItinerary
    extra = 2

class IncludedCostInline(admin.TabularInline):
    model = IncludedCost
    extra = 2

class TourAdmin(admin.ModelAdmin):
    inlines = [ TourDetailInline, IncludedCostInline, ]

admin.site.register(CompanyIntroduction)
admin.site.register(CompanyDetail)
admin.site.register(Stories)
admin.site.register(Message)
admin.site.register(AboutUs)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AwardList)
admin.site.register(Partnership)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(WorkTogether)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(CategoryDetail, ProductSubAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Gallery)
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Event)
admin.site.register(OrderInfo)
admin.site.register(WhatWeDo)
admin.site.register(Program)
admin.site.register(Offer)
admin.site.register(WorkFor)
admin.site.register(Tour, TourAdmin)
admin.site.register(GalleryCategory)