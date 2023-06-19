from django.contrib import admin

from question_widget.models import *

############ QUESTIONS ############


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(ShortAnswerQuestion)
class ShortAnswerQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(LongAnswerQuestion)
class LongAnswerQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadFileQuestion)
class UploadFileQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(InviteeUsernameQuestion)
class InviteeUsernameQuestionAdmin(admin.ModelAdmin):
    pass

############ ANSWERS ############


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(ShortAnswer)
class ShortAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(LongAnswer)
class LongAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(UploadFileAnswer)
class UploadFileAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(InviteeUsernameAnswer)
class InviteeUsernameAnswerAdmin(admin.ModelAdmin):
    pass