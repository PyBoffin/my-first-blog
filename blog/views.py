from django.shortcuts import render

# Create your views here.

#Views are just Python functions that are a little bit more
#complicated than the ones we wrote in the Introduction to Python chapter.

def post_list(request):
    return render(request,'blog/post_list.html',{})
    
