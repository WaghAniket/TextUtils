# user created
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Index.html')

def analyze(request):
    djtext = request.POST.get('text', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    exspacerem = request.POST.get('exspacerem', 'off')
    params={}
    # Remove punctuations
    if removepunc == 'on':
        analyzed = ''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    # Uppercase
    if capitalize == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    # New Line Remove
    if newlinerem == 'on':
        analyzed = ''
        for char in djtext:
            if char != '/n' and char != "/r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    # Remove Extra Spaces
    if exspacerem == 'on':
        analyzed = ''
        for i, char in enumerate(djtext):
            if not (djtext[i] == ' ' and djtext[i + 1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    #exception
    if (removepunc != "on" and newlinerem != "on" and exspacerem != "on" and capitalize != "on"):
        return HttpResponse("error")

    return render(request, 'Analyze.html', params)
