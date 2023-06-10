from django.shortcuts import render
from django.views.generic import ListView
from sitetatto.forms import PaintersFilterForm
from sitetatto.models import Painter, Image

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
            result[self.context_object_name] = result(self.context_object_name).filter()
        return result

