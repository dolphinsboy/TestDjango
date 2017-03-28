from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ["question"]}),
        ('Date information', {'fields': ["pub_date"]})
    ]
    inlines = [ChoiceInline]
    list_display = ("question", "pub_date", "was_published_recently")
    list_filter = ['question', 'pub_date']

admin.site.register(Question, QuestionAdmin)