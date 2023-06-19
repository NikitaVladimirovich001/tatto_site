from django.shortcuts import render, redirect
from django.views.generic import ListView
from sitetatto.forms import PaintersFilterForm
from sitetatto.models import Painter, Image
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def tatto(request): # доп страница информации
    return render(request, 'tatto.html')

@login_required
def removal(request): # доп страница информации
    return render(request, 'removal.html')

def correction(request): # доп страница информации
    return render(request, 'correction.html')

@login_required
def add_comment(request): # Добавления комментариев
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    else:
        form = CommentForm(initial={'author': request.user.username})
    return render(request, 'index.html', {'form': form})

@login_required
def comments_list(request): # Вывод списка комментариев
    comments = Comment.objects.all()
    return render(request, 'index.html', {'comments': comments})


class PainterListView(LoginRequiredMixin, ListView): # Вывод списка мастеров и изображений конкретного мастера (по дефолту отображаются все изображения)
    model = Image
    context_object_name = 'image_list'
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        print(result)
        if self.request.method == 'GET':
            form = PaintersFilterForm(self.request.GET)
            if form.is_valid():
                cd = form.cleaned_data
                if int(cd['painter']) != 0:
                    result[self.context_object_name] = self.model.objects.filter(painter__id=int(cd['painter']))
            else:
                form = PaintersFilterForm()
            result['form'] = form
            return result

class Search(ListView):
    template_name = 'index.html'
    context_object_name = 'image_list'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Image.objects.filter(painter__name__icontains=query)
        else:
            return Image.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context



