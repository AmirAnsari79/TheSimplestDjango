from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from catalogue.models import Product, Category


@login_required()
@require_http_methods(request_method_list=['GET', 'POST'])
# @require_GET()
# @require_POST()
def user(request):
    return HttpResponse('sd')


# @permission_required('Has_score_permission', login_url='/', raise_exception=True)
# @user_passes_test(lambda u: user.is_staff)
def product_list(request):
    products = Product.objects.all()

    category = Category.objects.first()

    products = Product.objects.filter(category_id=1)
    products = Product.objects.filter(category__name='Book')
    products = Product.objects.select_related('category').all()
    return render(request, 'catalogue/product_list.html', context={'products': products})


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return HttpResponse('this product does not exist')
    return render(request, 'catalogue/product_detail.html', context={'product': product})
