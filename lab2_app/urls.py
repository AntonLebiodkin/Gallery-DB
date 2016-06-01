from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loadcsv$', views.upload_file, name='upload_file'),
    url(r'^load_crud$', views.load_crud, name='load_crud'),
    url(r'^update_photo$', views.update_photo, name='update_photo'),
    url(r'^delete_photo$', views.delete_photo, name='delete_photo'),
    url(r'^add_photo$', views.add_photo, name='add_photo'),
    url(r'^search_photo$', views.search_photo, name='search_photo'),
    url(r'^search_author$', views.search_author, name='search_author'),
    url(r'^match_photo$', views.get_match_photo, name='get_match_photo'),
    url(r'^not_match_photo$', views.get_not_match_photo, name='get_match_photo'),
    url(r'^get_places$', views.get_places, name='get_places'),
    url(r'^get_photoalbums$', views.get_photoalbums, name='get_photoalbums'),
    url(r'^get_authors$', views.get_authors, name='get_authors'),
    url(r'^get_formats$', views.get_formats, name='get_formats')
]