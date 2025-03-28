from django.db import models
import os

class Semester(models.Model):
    name = models.CharField(max_length=10)  # e.g., "Sem1", "Sem2"

    def __str__(self):
        return self.name

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('practical_files', 'Practical Files'),
        ('books', 'Books'),
        ('question_paper', 'Question Paper'),
    ]

    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=60,blank=True, null=True)
    file = models.FileField(upload_to='resources/')
    file_size = models.PositiveIntegerField(blank=True, null=True, editable=False)  # Size in bytes
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} of size {self.file_size}"
    
    def save(self, *args, **kwargs):
        # Automatically set the file size when a file is uploaded or updated
        if self.file and (not self.file_size or self._state.adding):
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def get_size_in_mb(self):
        """Return the file size in MB."""
        if self.file_size:
            return f"{self.file_size / (1024 * 1024):.2f} MB"
        return "Unknown size"



# class PDFDocument(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, default='Unknown Author')
#     pdf_file = models.FileField(upload_to='pdfs/')
#     file_size = models.PositiveIntegerField(blank=True, null=True, editable=False)  # Size in bytes
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     def save(self, *args, **kwargs):
#         # Automatically set the file size when a file is uploaded or updated
#         if self.pdf_file and (not self.file_size or self._state.adding):
#             self.file_size = self.pdf_file.size
#         super().save(*args, **kwargs)

#     def get_size_in_mb(self):
#         """Return the file size in MB."""
#         if self.file_size:
#             return f"{self.file_size / (1024 * 1024):.2f} MB"
#         return "Unknown size"


# class PDFDocument(models.Model):  ****************
#     title = models.CharField(max_length=255)
#     pdf_file = models.FileField(upload_to='pdfs/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class QuestionsDocument(models.Model): *************
#     title = models.CharField(max_length=255)
#     pdf_file = models.FileField(upload_to='pdfs/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Music(models.Model):
#     title = models.CharField(max_length=255)
#     artist = models.CharField(max_length=255, blank=True, null=True, default='Unknown')
#     music_file = models.FileField(upload_to='musics/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title