from django.db import models
from django.utils.text import slugify
# Create your models here.

class Tag(models.Model):
    name  = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    short_description = models.CharField(max_length=220)
    description = models.TextField(blank=True)
    cover = models.URLField(help_text="URL del GIF animado", blank = True)
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    Project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='images')
    image = models.URLField(help_text="URL del GIF animado", blank=True)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.Project.title}"

class Experience(models.Model):
    role = models.CharField(max_length=120)                 # p.ej. "Data Scientist Jr"
    company = models.CharField(max_length=120)              # p.ej. "Nexu"
    company_url = models.URLField(blank=True)
    image_url = models.URLField(help_text="URL del GIF animado", blank=True)
    location = models.CharField(max_length=120, blank=True) # p.ej. "CDMX (remoto)"
    start_date = models.DateField()                          # p.ej. 2024-03-01
    end_date = models.DateField(blank=True, null=True)       # null = “Actual”
    summary = models.TextField(blank=True)                   # 1–3 líneas
    technologies = models.CharField(max_length=200, blank=True)  # p.ej. "Python, Django, PostgreSQL"

    order = models.PositiveIntegerField(default=0, help_text="Para reordenar manualmente (0 arriba).")

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} · {self.company}"

    @property
    def is_current(self):
        return self.end_date is None
