from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    # Get all available products
    products = Product.objects.filter(is_available=True).order_by('created_date')
    
    # Attach reviews to each product
    for product in products:
        product.reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
