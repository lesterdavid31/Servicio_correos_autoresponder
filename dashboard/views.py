
from django.views.generic import TemplateView, View, UpdateView, DeleteView
from newsletters.models import NewsLetter
from django.shortcuts import render, redirect, get_object_or_404
from newsletters.forms import NewsLetterCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy

# Create your views khere.
# class DashboardHome(TemplateView):
#     template_name = "dashboard/index.html"
    

class NewsLettersDashboardHomeView(View):
    def get(self,request, *args, **kwargs):
        newsletters = NewsLetter.objects.all()
        context = {
            "newsletters": newsletters,

        }
        return render(request,'dashboard/list.html', context)
    

class NewsletterCreateView(View):
    def get(self, request, *args, **kwargs):
        form = NewsLetterCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'dashboard/create.html', context)
    
    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            form = NewsLetterCreationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                newsletter = NewsLetter.objects.get(id=instance.id)
                if newsletter.status == "Published":
                    subject= newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for email in newsletter.email.all():
                        send_mail(subject, from_email= from_email, recipient_list=[email], message=body, fail_silently=True)
                return redirect("dashboard:list")
            
            context={
                'form': form,
            }
        return render(request, 'dashboard/create.html', context)


class NewsletterDetailView(View):
    def get(self,request,pk,*args, **kwargs):
        newsletter = get_object_or_404(NewsLetter, pk=pk)
        context={
            "newsletter": newsletter    
            }
        return render(request, "dashboard/detail.html",context)


class NewsletterUpdateView(UpdateView):
    model = NewsLetter
    form_class = NewsLetterCreationForm
    template_name = "dashboard/update.html"
    success_url = "dashboard/detail/2/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "view_type":"update"
        })
        return context
    
    def post(self,request,pk, *args, **kwargs):
        newsletter = get_object_or_404(NewsLetter, pk=pk)
        
        if request.method == "POST":
            form = NewsLetterCreationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                newsletter = NewsLetter.objects.get(id=instance.id)
                if newsletter.status == "Published":
                    subject= newsletter.subject
                    body = newsletter.body
                    from_email = settings.EMAIL_HOST_USER
                    for email in newsletter.email.all():
                        send_mail(subject, from_email= from_email, recipient_list=[email], message=body, fail_silently=True)
                return redirect("dashboard:detail", pk=newsletter.id)
            return redirect("dashboard:detail", pk= newsletter.id)
        else:
            form = NewsLetterCreationForm(instance=newsletter)
        context={
            'form': form,
            }
            
        return render(request, 'dashboard/update.html', context)
