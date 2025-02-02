import datetime
from django.contrib import admin
from django.utils import timezone

from .models import Question, Choice


# admin.site.site_header = "Polls Admininstration"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = (
        (
            None,
            {
                "fields": (["question_text"]),
            },
        ),
        (
            None,
            {
                "fields": (["pub_date"]),
            },
        ),
    )
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
