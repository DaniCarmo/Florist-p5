from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from django.contrib import messages

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Review submitted successfully')
            return redirect('profile')
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this review')
    return redirect('profile')

def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.html', {'reviews': reviews})
