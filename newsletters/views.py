from django.shortcuts import render
from .forms import NewsletterUserSgnupForm, NewsLetterCreationForm
from django.contrib import messages
from .models import NewsLettersUser
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.
def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterUserSgnupForm(request.POST)
        if form.is_valid():
            print("formulario valido")
            instance = form.save(commit=False)
            if NewsLettersUser.objects.filter(email  = instance.email).exists():
                print("usuario existente")
                messages.warning(request, 'Email alredy exists.')
            else:
                instance.save()
                print('usuario guardado')
                messages.success(request,'Hemos enviado un correo electrónicoa tu correo, Abrelo y enterate de los mejores estilos que tenmos para ti!')

                #correo electronico
                subject = 'Libro de ciencia'
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]

                html_templates ='newsletters/email_templates/welcome.html'
                html_message = render_to_string(html_templates)
                message = EmailMessage(subject, html_message, from_email,to_email)
                message.content_subtype='html'
                message.send()
        else:
            print("formulario no válido", form.errors)
    else:
        form= NewsletterUserSgnupForm()

    context = {
        'form': form,
    }

    return render(request,'newsletters/home.html', context)       

def newsletter_unsubscribe(request):
    form = NewsletterUserSgnupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLettersUser.objects.filter(email=instance.email).exists():
            NewsLettersUser.objects.filter(email=instance.email).delete()
            messages.success(request,'Email has been removed')
        else:
            print('Email not found')
            messages.warning(request, 'Email not found')

    context = {
        'form':form,
    }
    return render(request,'newsletters/email_templates/unsubscribe.html', context)


