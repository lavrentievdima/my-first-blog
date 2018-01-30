активировать виртуальную среду - myvenv\Scripts\activate




Шаги по созданию проэкта:

- создать приложение blog:  (myvenv) ~/djangogirls$ python manage.py startapp blog
затем в mysite/settings.py добавить это приложение в список INSTALLED_APPS [.... , blog,]
- делаем модель
- добавление модели в БД - python manage.py makemigrations blog
затем делаем миграции python manage.py migrate blog
- добавим нашу модель в админку. В blog/admin.py запмшем:
from .models import Post
admin.site.register(Post)
- создать суперпользователа чтоб зайти в админку, в командной строке python manage.py createsuperuser
- URLs. В файл mysite/urls.py добавим в urlpatterns = [ ....., url(r'', include('blog.urls')), ]
    Создай новый пустой файл blog/urls.py
        from django.conf.urls import url
        from . import views
        urlpatterns = [ url(r'^$', views.post_list, name='post_list'),]
- view. Представление. в файле blog/views.py
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
- создаем шаблон в папке blog/templates/blog (папки тоже нужно создать) создаем post_list.html
- CSS. В приложении создать папки static/css. в css создать файл стиля
    Для добавления файлов из static в шаблоне в самом начале пишем {% load staticfiles %} и подгружаем сами файлы <link rel="stylesheet" href="{% static 'css/blog.css' %}">
- расширение шаблона см. https://tutorial.djangogirls.org/ru/template_extending/