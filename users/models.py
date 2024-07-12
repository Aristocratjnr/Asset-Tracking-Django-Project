# views.py
from django.shortcuts import render
from sklearn import model_selection
from .models import Block, House, Payment, Sale

def dashboard(request):
    total_blocks = Block.objects.count()
    total_houses = House.objects.count()
    total_occupied_houses = House.objects.filter(occuppied=True).count()
    total_payments = Payment.objects.count()
    total_sales = Sale.objects.count()
    total_sales_amount = Sale.objects.aggregate(model_selection.Sum('price'))['price__sum']

    recent_payments = Payment.objects.order_by('-payment_id')[:5]
    recent_sales = Sale.objects.order_by('-id')[:5]

    context = {
        'total_blocks': total_blocks,
        'total_houses': total_houses,
        'total_occupied_houses': total_occupied_houses,
        'total_payments': total_payments,
        'total_sales': total_sales,
        'total_sales_amount': total_sales_amount,
        'recent_payments': recent_payments,
        'recent_sales': recent_sales,
    }
    return render(request, 'dashboard.html', context)
