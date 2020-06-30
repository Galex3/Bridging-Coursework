from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comment, CVExperience, Education, HardSkill, SoftSkill, Project, Interest, Language


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_date', 'active')
    list_filter = ('active', 'created_date')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        queryset.update(active=True)


class CVExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration')


class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('icon',)


class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('text',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'duration')


class InterestAdmin(admin.ModelAdmin):
    list_display = ('icon',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'level')


admin.site.register(Education, EducationAdmin)
admin.site.register(CVExperience, CVExperienceAdmin)
admin.site.register(HardSkill, HardSkillAdmin)
admin.site.register(SoftSkill, SoftSkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# bham2020
