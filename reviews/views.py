from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Product
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
    """
    Allows admin to delete review
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops! Admins only.')
        return redirect('all_reviews')

    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
        messages.success(request, 'Review deleted!')
        return redirect('all_reviews')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('all_reviews')


def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.html', {'reviews': reviews})


def search_results(request):
    query = request.GET.get('query')
    reviews = Review.objects.filter(product__name__icontains=query)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/all_reviews.html', context)
