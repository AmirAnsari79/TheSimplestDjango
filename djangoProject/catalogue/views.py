from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from catalogue.models import Product, Category


@login_required()
@require_http_methods(request_method_list=['GET', 'POST'])
@require_GET()
@require_POST()
def user(request):
    return HttpResponse('sd')

@permission_required('')
@user_passes_test(lambda u: user.is_staff)
def product_list(request):
    products = Product.objects.all()

    category = Category.objects.first()

    products = Product.objects.filter(category_id=1)
    products = Product.objects.filter(category__name='Book')
    return HttpResponse('catalogue product list ')
