from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


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
    'ovsyanka': {
        'Молоко': 1,
        'Вода': 3,
        'Овсянка': 1,
        'Яжевика': 3,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, recipe_name):
    if recipe_name not in DATA:
        return HttpResponse(f'Рецепта {recipe_name} нету в списке')
   
    servings = int(request.GET.get('servings'))

    recipe_data = DATA[recipe_name]
    context = {'recipe': {}}
    
    for ingredient, amount in recipe_data.items():
        context['recipe'][ingredient] = amount * servings
    return render(request, 'calculator/index.html', context)
    
    