from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    # Optionally, fetch language from user input, request, or default
    language = request.GET.get("language","fr")  # Example: ?language=fr
    trans = translate(language)
    return render(request, 'home.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        # Temporarily switch to the requested language
        activate(language)
        text = gettext("Hello!")
    finally:
        # Restore the original language after translation
        activate(cur_language)
    return text

def Item(request):
    return render(request, 'item.html')

def index(request):
    return render(request, 'index.html')
