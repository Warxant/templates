from django.shortcuts import render
from django.shortcuts import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    servings = int(request.GET.get("servings"))
    
    for x in DATA['omlet']:
        DATA['omlet'][x] = DATA['omlet'][x]*servings
    context = {
        'recipe': DATA['omlet']
    }
    return render(request, 'demo.html', context)


def pasta(request):
    servings = int(request.GET.get("servings"))
    for x in DATA['pasta']:
        DATA['pasta'][x] = DATA['pasta'][x]*servings
    context = {
        'recipe': DATA['pasta']
    }
    return render(request, 'demo.html', context)


def buter(request):
    servings = int(request.GET.get("servings"))
    for x in DATA['buter']:
        DATA['buter'][x] = DATA['buter'][x]*servings
    context = {
        'recipe': DATA['buter']
    }
    return render(request, 'demo.html', context)