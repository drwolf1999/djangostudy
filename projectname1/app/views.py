from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Board, Comment
from .forms import BoardForm, CommentForm
# Create your views here.
# boardList = [{'id': i, 'title': 'title%d' % i, 'content': 'content%d' % i} for i in range(10)]

class IndexView(ListView):
    template_name = 'app/index.html'
    context_object_name = 'boardList'
    def get_queryset(self):
        return Board.objects.all()

# def index(request):
#     boardList = Board.objects.all()
#     context = {
#         'boardList': boardList
#     }
#     return render(request, 'app/index.html', context)


class BoardDetail(DetailView):
    template_name = 'app/board.html'
    context_object_name = 'board'
    model = Board
    # def get_queryset(self):
    #     return Board.objects.filter(id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = Board.objects.filter(id=self.kwargs.get('pk')).first()
        context['form'] = CommentForm()
        return context

# def detailBoard(request, boardId):
#     board = Board.objects.get(id=boardId)
#     context = {
#         'board': board
#     }
#     return render(request, 'app/board.html', context)


def newBoard(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app')
    else:
        form = BoardForm()
        context = {
            'form': form
        }
        return render(request, 'app/new.html', context)

def BoardDelete(request, boardId):
    board = Board.objects.get(id=boardId)
    board.delete()
    return redirect('/app')

def CommentCreate(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
        return redirect('/app/board/' + str(pk))
