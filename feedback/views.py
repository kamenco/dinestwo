from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def feedback_page(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Feedback.objects.create(user=request.user, comment=comment)
        return redirect('feedback')

    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback.html', {'feedbacks': feedbacks})

@login_required
def delete_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    if feedback.user == request.user:
        feedback.delete()
    return redirect('feedback')
