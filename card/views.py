from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card.models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    qs = Post.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render(request, 'card/post_detail.html', {
                                    'post': post,
                                    'form': form,
                                    })

def comment_list(request):
    qs = Comment.objects.all().order_by('-id').select_related('post')

    return render(request, 'card/post_detail.html',{
        'comment_list':qs,
    })


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.password = comment
            comment.delete()
    else:
        form = CommentForm(instance=comment)
    return render(request, 'card/comment_delete.html', {'form': form})
