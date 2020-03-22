from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='home'),
    path('aboutus/', views.About.as_view(), name='about'),
    path('services/', views.Services.as_view(), name='service'),
    path('service/detail/<int:pk>/', views.ServicesDetail.as_view(), name='service-detail'),
    path('product/', views.ProductPage.as_view(), name='product'),
    path('product/category/<int:pk>', views.ProductCategory.as_view(), name='product-category'),
    path('product/detail/<int:pk>', views.ProductDetails.as_view(), name='product-detail'),
    path('gallery/', views.GalleryPage.as_view(), name='gallery'),
    # path('gallery/category/<int:pk>', views.GalleryCategory.as_view(), name='gallery-category'),
    path('shop/', views.Shop.as_view(), name='shop'),
    path('blog/', views.BlogPage.as_view(), name='blog'),
    path('blog/detail/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('recipe/', views.RecipePage.as_view(), name='recipe'),
    path('recipe/detail/<int:pk>', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('faq/', views.FaqPage.as_view(), name='faq'),
    path('tour/detail/<int:pk>', views.TourDetail.as_view(), name='tour-detail'),
]

