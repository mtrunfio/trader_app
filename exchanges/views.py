from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import Exchange


def index(request):
    exchange_list = Exchange.objects.order_by('id')
    context = {'exchange_list': exchange_list}
    return render(request, 'exchanges/index.html', context)


def detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    return render(request, 'exchanges/detail.html', {'exchange': exchange})
