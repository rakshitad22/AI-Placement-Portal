from django.shortcuts import render, redirect
from .models import Resume

def upload_resume(request):
    if request.method == 'POST':
        name = request.POST['name']
        resume_file = request.FILES['resume']

        Resume.objects.create(
            name=name,
            resume=resume_file
        )

        return redirect('/resume/ats/')

    return render(request, 'upload_resume.html')
def ats_score(request):
    score = 78

    return render(request, 'ats_result.html', {
        'score': score
    })