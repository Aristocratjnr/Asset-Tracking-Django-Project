from django.shortcuts import render
from django.http import JsonResponse
from .forms import AssetForm, OrderForm # type: ignore
from .models import Asset, Order # type: ignore

def dashboard(request):
    assets = Asset.objects.all()
    orders = Order.objects.all()
    asset_form = AssetForm()
    order_form = OrderForm()
    return render(request, 'dashboard/dashboard.html', {
        'assets': assets,
        'orders': orders,
        'asset_form': asset_form,
        'order_form': order_form
    })

def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Asset added successfully'})
    return JsonResponse({'message': 'Error adding asset'}, status=400)

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Order added successfully'})
    return JsonResponse({'message': 'Error adding order'}, status=400)
