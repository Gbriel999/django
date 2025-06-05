from django.shortcuts import render

def mi_pagina_view(request):
    return render(request, 'mi_app/mi_pagina.html')
