from django.shortcuts import render
from .models import Client, Product, Sale

def project_info(request):
    Client = Client.objects.all()
    Product = Product.objects.all()
    Sale = Sale.objects.all()

    # Передаем данные в шаблон
    return render(request, 'project_info.html', {
        'project_name': 'Лабораторна робота №8',  
        'student_name': 'Коноваленко Денис Юрійович',
        'student_group': 'КБ21015Б',
        'Client': Client,
        'Product': Product,
        'Sale': Sale,
    })
