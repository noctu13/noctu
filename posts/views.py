from django.shortcuts import render
from .pageback import PageBack
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    page_back = PageBack(request, post_list)
    return render(
        request,
        'posts/index.html',
        {
            'page': page_back.page,
            'paginator': page_back.paginator
        }
    )
