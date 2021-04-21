from django.contrib import admin
<<<<<<< HEAD
from .models import Polls

admin.site.register(Polls)
=======
<<<<<<< HEAD

from .models import Question, Choice

admin.site.site_header = "Indecisive Admin"
admin.site.site_title = "Indecisive Admin Area"
admin.site.index_title = "Welcome to the Indecisive admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
=======
from .models import Polls

admin.site.register(Polls)
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2
