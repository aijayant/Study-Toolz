from django.shortcuts import render, get_object_or_404
from .models import Semester, Resource

def home(request):
    semesters = Semester.objects.all()
    return render(request, 'front/home.html', {'semesters': semesters})

def semester_detail(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)
    return render(request, 'Semester.html', {'semester': semester})

def category_list(request, semester_id, category):
    semester = get_object_or_404(Semester, id=semester_id)
    resources = Resource.objects.filter(semester=semester, category=category)
    categoryName = category.replace("_", " ").title()
    return render(request, 'category_list.html', {'resources': resources, 'category': category, 'categoryName': categoryName,'semester': semester})




# from django.shortcuts import render,HttpResponse
# from .models import PDFDocument,Music

# # Create your views here.
# def home(request):
#     return render(request,'front/home.html')

# def pdf_list(request):
#     pdfs = PDFDocument.objects.all()
#     return render(request, 'pdf_list.html', {'pdfs': pdfs})

# def music_list(request):
#     musics = Music.objects.all()
#     return render(request,'music.html',{'musics':musics})

# def question_list(request):
#     # musics = PDFDocument.objects.all()
#     return render(request,'questions.html')