from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from . forms import ContactForm, ShopForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from . models import CompanyDetail, CompanyIntroduction, AboutUs, WhatWeDo, Partnership, AwardList, Testimonial, Service, ServiceDetail, Event, Package, PackageService, Gallery, Category, CategoryDetail, CompanyDetail, Message, OrderInfo, Recipe, Question, QuestionCategory, Blog, Program, Offer, WorkTogether, WorkFor, Stories, ProductDetail, ProductSubImage

# Create your views here.
class IndexView(TemplateView):
    template_name = 'item/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_detail'] = CompanyDetail.objects.last()
        context['company_intro'] = CompanyIntroduction.objects.last()
        context['recent'] = Blog.objects.all().order_by('-date')[:3]
        context['program'] = Program.objects.all()
        context['offer'] = Offer.objects.all()[:3]
        context['work_together'] = WorkTogether.objects.last()
        context['work_for'] = WorkFor.objects.all()
        context['story'] = Stories.objects.all()
        return context

class About(TemplateView):
    template_name = 'item/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.objects.last()
        context['we_do'] = WhatWeDo.objects.all()
        context['partner'] = Partnership.objects.all()
        context['award'] = AwardList.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        return context
   

class Services(TemplateView):
    template_name = 'item/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        context['package'] = Package.objects.filter(service_id__isnull=True)
        return context

class ServicesDetail(DetailView):
    model = Service
    template_name = 'item/service-detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_detail'] = ServiceDetail.objects.filter(service__id=self.kwargs.get("pk"))
        context['event'] = Event.objects.filter(service_id=self.kwargs.get("pk"))
        context['package'] = Package.objects.filter(service_id=self.kwargs.get("pk"))
        return context
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Service, pk=id_)

class ProductPage(ListView):
    template_name = 'item/product.html'
    model = CategoryDetail
    paginate_by = 4
    context_object_name = "list"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by('name')
        context['category'] = categories
        return context
    
    def get_queryset(self, **kwargs):
        categories = Category.objects.all().order_by('name')
        return CategoryDetail.objects.filter(category_id=categories[0].id)


class ProductDetails(DetailView):
    model = CategoryDetail
    template_name = 'item/product_detail.html'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = CategoryDetail.objects.get(id=self.kwargs.get("pk"))
        return context

class ProductCategory(ListView):
    template_name = 'item/product.html'
    model = CategoryDetail
    paginate_by = 4
    context_object_name = "list"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by('name')
        context['category'] = categories
        return context
    
    def get_queryset(self, **kwargs):
        return CategoryDetail.objects.filter(category_id=self.kwargs.get("pk"))
    

class GalleryPage(TemplateView):
    template_name = 'item/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.all()
        return context

class Shop(TemplateView):
    template_name = 'item/shop.html'
    model = OrderInfo
    form_class = ShopForm

    def post(self, request, *args, **kwargs):
        product_name = request.POST.get('product_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        quantity = request.POST.get('quantity')
        address = request.POST.get('address')
        note = request.POST.get('note')

        success = OrderInfo.objects.create(product_name=product_name,  email=email, phone_number=phone_number, quantity=quantity, address=address,  note=note)

        return HttpResponseRedirect('/') 

class BlogPage(TemplateView):
    template_name = 'item/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.all()
        context['recent'] = Blog.objects.all().order_by('-date')
        return context

class BlogDetail(DetailView):
    template_name = 'item/blog-detail.html'
    model = Blog
    context_object_name = 'blog_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.first()
        context['recent'] = Blog.objects.all().order_by('-date')[:4]
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Blog, pk=id_)

class Contact(TemplateView):
    template_name = 'item/contact-us.html'
    model = Message
    form_class = ContactForm

    def get_context_data(sel, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = CompanyDetail.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        message = request.POST.get('message')

        success = Message.objects.create(full_name=full_name,  email=email, phone_number=phone_number, address=address,  message=message)

        return HttpResponseRedirect('/')

class RecipePage(ListView):
    template_name = 'item/recipes.html'
    model = Recipe
    context_object_name = 'recipe'
    paginate_by = 4

class RecipeDetail(DetailView):
    template_name = 'item/recipes-detail.html'
    model = Recipe
    context_object_name = 'recipe_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.first()
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Recipe, pk=id_)

class FaqPage(TemplateView):
    template_name = 'item/faq.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = QuestionCategory.objects.all()
        return context
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Question, pk=id_)
