from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from .models import Product

class ProductListView(ListView):
	queryset = Product.objects.all()
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		return context


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request,'products/product_list.html',context)

class ProductDetailView(DetailView):
	model = Product
	

# class ProductDetailView(DetailView):
# 	model = Product
# 	def setup(self,request,*args,**kwargs):
# 		print(args)
# 		print(kwargs)
# 		kwargs['pk'] = kwargs['id']
# 		del kwargs['id']
# 		return super().setup(request,*args,**kwargs)

		