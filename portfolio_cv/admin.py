from django.contrib import admin
from .models import Project, Tag, ProjectImage, Experience
# Register your models here.

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class projectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_featured')
    list_filter = ("is_featured", "tags")
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "order")
    list_filter = ("company",)
    search_fields = ("role", "company", "summary", "technologies")