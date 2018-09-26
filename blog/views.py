from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

#Views are just Python functions that are a little bit more
#complicated than the ones we wrote in the Introduction to Python chapter.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{"myPostData":posts})
