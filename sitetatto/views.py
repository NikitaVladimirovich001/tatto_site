from django.shortcuts import render
from django.views.generic import ListView
from sitetatto.forms import PaintersFilterForm
from sitetatto.models import Painter, Image

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comment
from .forms import CommentForm

class PainterListView(ListView):
    model = Image
    context_object_name = 'image_list'
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        print(result)
        if self.request.method == 'GET':
            form = PaintersFilterForm(self.request.GET)
            if form.is_valid():
                result[self.context_object_name] = result(self.context_object_name).filter(painter__name=form.painter)
        else:
            form = PaintersFilterForm()
        result['form'] = form
        return result

def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    paginator = Paginator(comments, 1) # Показывать 10 комментариев на странице

    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, доставить первую страницу.
        comments = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы допустимого диапазона (например, 9999), отправьте последнюю страницу результатов.
        comments = paginator.page(paginator.num_pages)

    form = CommentForm()

    return render(request, 'comment_list.html', {'comments': comments, 'form': form})

