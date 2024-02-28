from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product

# подсчёт общего количества продуктов через базу данных:

def total_in_db(request):
    total = Product.objects.aggregate(Sum('amount'))
    context = {'title': 'Общее количество посчитано в базе данных',
    'total': total,
    }

    return render(request, 'myapp6/total_count.html', context)


# подсчёт общего количества продуктов через само представление:

def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.amount for product in products)
    context = {'title': 'Общее количество посчитано в представлении',
    'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)

# подсчёт общего количества продуктов на через модель Product, а представление пробросит её в шаблон

def total_in_template(request):
    context = {'title': 'Общее количество посчитано в шаблоне',
    'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)