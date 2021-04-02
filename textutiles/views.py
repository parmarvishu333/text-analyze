
# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox values

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+ char
        params = {'purpose': 'remove punctuations', 'analyzed_text':analyzed}
        #Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'new lines remover', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
        params = {'purpose': 'space remover', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcount == "on"):
        analyzed = 0
        analyzed = analyzed + len(djtext)
        params = {'purpose': 'your char count is', 'analyzed_text': analyzed}
    #     # Analyze the text
    if(removepunc != 'on' and fullcaps != 'on' and newlineremover !='on' and spaceremover != 'on' and charcount != 'on'):
        return HttpResponse("ErrorPOST")

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("ErrorPOST")







