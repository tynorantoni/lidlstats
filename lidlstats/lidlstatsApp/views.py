from django.shortcuts import render


def index(request):

    context={}
    return render(request, 'lidlstatsApp/index.html', context)

def data(request):

    context={}
    return render(request, 'lidlstatsApp/data.html', context)

def user_settings(request):

    context={}

    return render(request, 'lidlstatsApp/user.html', context)

# def login(request)
# def logout(request)