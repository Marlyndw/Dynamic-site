import glob
import os
#import request
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    # This is similar to ones we have done before. Instead of keeping
#    # the HTML / template in a separate directory, we just reply with
#    # the HTML embedded here.
#    return HttpResponse('''
#        <h1>Welcome to my home page!</h1>
#        <a href="/about-me">About me</a> <br />
#        <a href="/github-api-example">See my GitHub contributions</a> <br />
#    ''')


def bio(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
    
    "bio_is_active": "active",
     }
    
    return render(request, 'bio.html', context)
    

def resume(request):
    
    context = {
    
    "resume_is_active": "active",
     }
    
    return render(request, 'resume.html', context)
    

def contact(request):
    
    context = {
    
    "contact_is_active": "active",
     }
    
    return render(request, 'contact.html', context)
    
    
def index(request):
    
    context = {
    
    "index_is_active": "active",
     }
    
    return render(request, 'index.html', context)


