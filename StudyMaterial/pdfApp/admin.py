from django.contrib import admin
from .models import Semester,Resource

admin.site.register(Semester)

admin.site.register(Resource)

# from django.contrib import admin
# from .models import PDFDocument,Music

# @admin.register(PDFDocument)
# class PDFDocumentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'uploaded_at')

# @admin.register(Music)
# class MusicAdmin(admin.ModelAdmin):
#     list_display = ('title', 'artist', 'uploaded_at')