from django.template import Context,loader
from datetime import datetime
from django.http import HttpResponse

def index(request):
    return HttpResponse(
    '<html><body><h1>Hello ,World!</h1><a href="/about">About</a><br> <br> <a href="/contact">Contact</a></body></html>'
    )
def about(request):
    return HttpResponse(
    "<h1>Here is the About Page Want to return home or Go to Contact ?</h1><a\
    href='/'>Home</a><br><br> <a href='/contact'>Contact</a>"
    )
def contact(request):
    return HttpResponse(
    "<h1>Here is the Contact Page. Want to return Home or Go to About? </h1>\
    <a href='/'>Home</a><br><br><a href='/about'>About</a>"
    )
def better(request):
    t=loader.get_template('betterhello.html')
    c=Context({'current_time':datetime.now(),})
    return HttpResponse(t.render(c))
