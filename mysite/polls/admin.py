from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']

    # adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    list_filter = ['pub_date']

    # adds a search box at the top of the change list
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)