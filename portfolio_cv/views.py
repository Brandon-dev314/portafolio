from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project, Tag, Experience
from .forms import ContactForm
# Create your views here.

def project_list(request):
    tag_slug = request.GET.get('tag')
    projects = Project.objects.all()
    active_tag = None
    if tag_slug:
        active_tag = Tag.objects.filter(slug=tag_slug).first()
        if active_tag:
            projects = projects.filter(tags=active_tag)

    experiences = Experience.objects.all()  


    return render(request, 'portfolio_cv/project_list.html', {
        'projects': projects,
        'tags': Tag.objects.all().order_by('name'),
        'active_tag': active_tag,
        'experiences': experiences,   
    })
    

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = (
        Project.objects.filter(tags__in = project.tags.all())
        .exclude(pk = project.pk)
        .distinct()
        [:3]
    )
    return render(request, 'portfolio_cv/project_detail.html', {
        'project': project,
        'related': related
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f"Nuevo mensaje de {name}",
                message=f"De: {name}\n Correo: {email}\n Mensaje: {message}",
                from_email=None,
                recipient_list=['tbdonran.23@gmail.com'],
            )
            messages.success(request, 'Tu mensaje ha sido enviado, te responderé pronto.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio_cv/contact.html', {'form': form})