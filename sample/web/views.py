from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from web.models import Board, Comment
from account.models import User
from .forms import BoardForm, CommentForm


# Create your views here.
# BoardList = [{'id': i, 'title': '호우 %s' % (str(i)), 'content': '호우호우 %s' % (str(i))} for i in range(4)]


class IndexView(ListView):
    template_name = 'web/index.html'
    context_object_name = 'BoardList'

    def get_queryset(self):
        if self.kwargs.get('title'):
            return Board.objects.filter(title=self.kwargs.get('title'))
        else:
            return Board.objects.all()


# def index(request):
#     BoardList = Board.objects.all()
#     context = {
#         'BoardList': BoardList
#     }
#     return render(request, 'web/index.html', context)

class BoardView(DetailView):
    template_name = 'web/board.html'
    context_object_name = 'Board'
    model = Board

    # def get_queryset(self):
    #     return Board.objects.filter(id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super(BoardView, self).get_context_data(**kwargs)
        context['Board'] = Board.objects.filter(id=self.kwargs.get('pk')).first()
        context['form'] = CommentForm
        return context


# def board(request, BoardId):
#     board = Board.objects.filter(id=BoardId).first()
#     print(board)
#     context = {
#         'Board': board
#     }
#     return render(request, 'web/board.html', context)

# class BoardCreate(CreateView):
#     form_class = BoardForm
#     template_name = 'web/new.html'
#     success_url = '/web'


def BoardCreate(request):
    if request.method == 'POST':
        if 'userId' not in request.session.keys():
            return redirect('/account/login')
        user = User.objects.get(userId=request.session['userId'])
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = user
            board.save()
        return redirect('/web/')
    else:
        form = BoardForm()
        context = {
            'form': form,
        }
        return render(request, 'web/new.html', context)

class BoardDelete(DeleteView):
    model = Board
    success_url = '/web'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


def BoardUpdate(request, pk):
    board = Board.objects.get(id=pk)
    form = BoardForm(request.POST or None, instance=board)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/web/board/%d' % pk)
    else:
        print(form)
        context = {
            'form': form,
            'id': pk,
        }
        return render(request, 'web/update.html', context)


class CommentCreate(CreateView):
    # model = Comment
    form_class = CommentForm

    # fields = ('content', )

    def form_valid(self, form):
        board = Board.objects.filter(id=self.kwargs.get('pk')).first()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.save()
        return redirect('/web/board/' + str(self.kwargs.get('pk')))
# def CommentCreate(request, pk):
#     board = Board.objects.get(id=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit = False)
#         comment.board = board
#         comment.save()
#     return redirect('/web/board/' + str(pk))
