from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from django.db.models import Max,Min,Count,Avg
from django.db.models.functions import ExtractMonth
from django.template.loader import render_to_string
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
	banners=Banner.objects.all().order_by('-id')
	data=Product.objects.filter(is_featured=True).order_by('-id')
	return render(request,'index.html',{'data':data,'banners':banners})



def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})


def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request,'brand_list.html',{'data':data})


def product_list(request):
	total_data=Product.objects.count()
	data=Product.objects.all().order_by('-id')[:3]
	brand = Brand.objects.all()
	category = Category.objects.all()
	size = Size.objects.all()
	color = Color.objects.all()
	min_price=ProductAttribute.objects.aggregate(Min('price'))
	max_price=ProductAttribute.objects.aggregate(Max('price'))
	return render(request,'product_list.html',
		{
			'data':data,
			'brands':brand,
			'sizes':size,
			'cats':category,
			'colors':color,
			'total_data':total_data,
			'min_price':min_price,
			'max_price':max_price,
		}
		)



def category_product_list(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Product.objects.filter(category=category).order_by('-id')
	brand = Brand.objects.all()
	category = Category.objects.all()
	size = Size.objects.all()
	color = Color.objects.all()
	return render(request,'category_product_list.html',{
			'data':data,
			'brands':brand,
			'sizes':size,
			'cats':category,
			'colors':color,
			})





def brand_product_list(request,brand_id):
	brand=Brand.objects.get(id=brand_id)
	data=Product.objects.filter(brand=brand).order_by('-id')
	brand = Brand.objects.all()
	category = Category.objects.all()
	size = Size.objects.all()
	color = Color.objects.all()
	return render(request,'category_product_list.html',{
			'data':data,
			'brands':brand,
			'sizes':size,
			'cats':category,
			'colors':color,
			})


def product_detail(request,slug,id):
	product=Product.objects.get(id=id)
	related_products=Product.objects.filter(category=product.category).exclude(id=id)[:4]
	colors=ProductAttribute.objects.filter(product=product).values('color__id','color__title','color__color_code').distinct()
	sizes=ProductAttribute.objects.filter(product=product).values('size__id','size__title','price','color__id').distinct()
	return render(request, 'product_detail.html',{'data':product, 'related':related_products,'sizes':sizes, 'colors':colors})


def search(request):
	q=request.GET['q']
	data=Product.objects.filter(title__icontains=q).order_by('-id')
	return render(request,'search.html',{'data':data})


def filter_data(request):
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	brands=request.GET.getlist('brand[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	allProducts=Product.objects.all().order_by('-id').distinct()
	allProducts=allProducts.filter(productattribute__price__gte=minPrice)
	allProducts=allProducts.filter(productattribute__price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(productattribute__color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(brands)>0:
		allProducts=allProducts.filter(brand__id__in=brands).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(productattribut__size__id__in=sizes).distinct()
	t=render_to_string('ajax/product-list.html',{'data':allProducts})
	return JsonResponse({'data':t})
