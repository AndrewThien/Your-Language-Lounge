from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Choice
from django.urls import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'your_library/your_library.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        #Return the last five published questions.
        return Post.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'your_library/details.html'

class ResultsView(generic.DetailView):
    model = Post
    template_name = 'your_library/results.html'

@login_required
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    try:
        selected_choice = post.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
       # Display the form again and the error message
        return render(request, 'your_library/details.html', {
            'post': post,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(
        reverse('your_library:results', args=(post_id,))
    )