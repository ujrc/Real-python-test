from django.shortcuts import render,get_object_or_404,render_to_response,redirect

# Create your views here.
from django.http import HttpResponse
from django.template import Context,loader,RequestContext

from blog.models import Post
from blog.forms import PostForm
#Helper functions
def get_popular_posts():
    popular_posts=Post.objects.order_by('-views')[:5]
    return popular_posts
"""
def encode_url(url):
    return url.replace(' ','_')"""

def index(request):
    latest_posts=Post.objects.all().order_by('-created_at')
    #popular_posts=Post.objects.order_by('-views')[:5]
    t=loader.get_template('blog/index.html')
    context_dict={'latest_posts':latest_posts,
    'popular_posts':get_popular_posts(),}
    #for post in latest_posts:
        #post.url=encode_url(post.title)

    #for popular_post in popular_posts:
    #    popular_post.url=encode_url(popular_post.title)
    #c=Context({'latest_posts':latest_posts, })
    c=Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    single_post=get_object_or_404(Post, slug=slug)
    single_post.views+=1 #inrement the number of views
    single_post.save() #and save it
    t=loader.get_template(('blog/post.html'))
    context_dict={'single_post': single_post,
    'popular_posts':get_popular_posts(), }
    c=Context(context_dict)
    return HttpResponse(t.render(c))

def add_post(request):
    context=RequestContext(request)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid(): # is the form valid?
            form.save(commit=True) # yes? save to database
            return redirect(index)
        else:
            print form.errors # no? display errors to end user
    else:
        form=PostForm()
    return render_to_response('blog/add_post.html',{'form' :form},
    context)
