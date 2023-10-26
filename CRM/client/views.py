from django.shortcuts import render

def clients_list(request):
    return render(request, 'client/clients_list.html')
