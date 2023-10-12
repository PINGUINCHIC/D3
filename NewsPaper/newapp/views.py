from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from django.utils import timezone

class PostList(ListView):
    model = Post
    template_name = 'newapp/news.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now()) # добавим переменную текущей даты time_now
        context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'newapp/new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()



