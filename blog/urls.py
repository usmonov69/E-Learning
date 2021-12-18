from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index-view' ),
	path('about/', views.about, name='about-view'),
	path('blog/', views.blog,  name='blog-view'),
	path('contact/', views.contact, name='contact-view'),
	path('course/', views.course, name='course-view'),
	path('post-search/', views.post_search, name='post-search'),
	path('course-search/', views.course_search, name='course-search'),
	#post - crud
	path('post_createe/', views.post_create, name='post-create'),
	path('post/<slug:slug>', views.post_detail_comment, name='post-detail'),
	path('post_updatee/<slug:slug>', views.post_update, name='post-update'),
	path('post_deletee/<slug:slug>', views.PostDelete.as_view(), name='post-delete'),
	#course-crud
	path('course_createe/', views.course_create, name='course-create'),
	path('course/<slug:slug>', views.course_detail, name='course-detail'),
	path('course_updatee/<slug:slug>', views.course_update, name='course-update'),
	path('course_deletee/<slug:slug>', views.CourseDelete.as_view(), name='course-delete'),

	path('all_course/', views.all_course, name='all-course'),
]