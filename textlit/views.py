from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse(''' <h1>Hello</h1> <a href="http://google.com">Google</a>''')

def deletefirstline(request):
    return HttpResponse("deletefirstline")

def analyze(request):
    #get the text 
    djtext = request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    print( removepunc)
    print(djtext)
    punctuations= '''.:;'!@#$%^&()'''
    analyzed = ""
    for  char in djtext:
        if char not in punctuations:analyzed = analyzed + char 
        
     params= {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
  
    return render(request,'analyze.html', params)