from django.contrib import admin

import codeschool.questions.coding_io.models.teststate
from codeschool.questions.coding_io import models

admin.site.register(models.AnswerKey)
admin.site.register(models.CodingIoFeedback)
admin.site.register(models.CodingIoProgress)
admin.site.register(models.CodingIoSubmission)
admin.site.register(models.CodingIoQuestion)
admin.site.register(codeschool.questions.coding_io.models.teststate.TestState)

