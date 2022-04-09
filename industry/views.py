from django.shortcuts import render
from django.http import HttpResponse

  
#關於我們aboutus
def aboutus1(request):
    return render(request, 'industry/aboutus1.html')

#產業類industry


#散戶的50道難題
def question1(request):
    return render(request, 'industry/question1.html')
def question2(request):
    return render(request, 'industry/question2.html')
def question3(request):
    return render(request, 'industry/question3.html')