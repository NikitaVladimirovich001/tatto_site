from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from record.forms import ContactForm
from django.core.mail import EmailMessage



def record(request):

    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['nomer'], form.cleaned_data['email'], form.cleaned_data['date'], form.cleaned_data['time'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'record.html', context=context)

def send_message(name, nomer, email, date, time):

    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'nomer': nomer, 'email': email, 'date': date, 'time': time}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['nikital983956@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()