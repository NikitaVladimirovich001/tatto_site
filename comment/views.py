from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import *

"""страница отзывы"""
def comment_view(request, page_number=1):
    context = {}
    comments = Comments.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()
        context['comment_form'] = form

    paginator = Paginator(comments, 5)
    try:
        page_obj = paginator.page(page_number)
    except Exception:
        if page_number < 1:
            page_obj = paginator.page(1)
        else:
            page_obj = paginator.page(paginator.num_pages)
    return render(request, 'comment.html',
                  {'comments': comments, 'comment_form': form, 'page_comments': page_obj}, )