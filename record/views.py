from django.shortcuts import render

from record.forms import ContactForm


def record(request):
    context = dict()
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'record.html', context=context)

def contacts(request):
    return render(
        request,
        'record.html'
    )

