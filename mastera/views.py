from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from sitetatto.models import Painter
from django.contrib.auth.mixins import LoginRequiredMixin


class PaintersList(LoginRequiredMixin, ListView):
    model = Painter
    context_object_name = 'painter_list'
    template_name = 'mastera.html'
    paginate_by = 3


def painter_detail(request, painter_id):
    painter = get_object_or_404(Painter, pk=id)
    return render(request, 'painter_detail.html', {'painter': painter})
