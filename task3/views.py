from django.shortcuts import render

# Create your views here.

def main_page(request):
    title = 'Главная'
    text = 'Главная страница'
    context = {
        'text': text,
        'title': title
    }
    return render(request, 'third_task/main_page.html', context)


def basket(request):
    title = 'Корзина'
    text = 'Корзина'
    context = {
        'text': text,
        'title': title
    }
    return render(request, 'third_task/basket.html', context)


def shop(request):
    title = 'Магазин'
    text = 'Магазин'
    context = {
        'text': text,
        'title': title,
        'game1': 'Atomic',
        'game2': 'Stalker',
        'game3': 'Cyberpunk2077'
    }
    return render(request, 'third_task/shop.html', context)