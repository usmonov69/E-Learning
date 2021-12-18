from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


User = get_user_model()


from accounts.models import Account


class PostViewCount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

class CourseViewCount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)


class CategoryPost(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)



class CategoryCourse(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.name)

class Comment(models.Model):
	user = models.CharField(max_length=100, null=True, blank=True)
	content = models.TextField() 
	timestamp = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
 
	def __str__(self):
		return str(self.user)



class Post(models.Model):
	title = models.CharField(max_length=170)
	image =  models.ImageField(upload_to='images/')
	body = RichTextField()
	categories = models.ManyToManyField(CategoryPost)
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.title)

	def get_categories(self):
		return self.categories.all()

	def get_absolute_url(self):
		return reverse('blog:post-detail', kwargs={
			'slug': self.slug
			})
	@property
	def post_view_count(self):
		return PostViewCount.objects.filter(post=self).count()

	def get_comments(self):
		return self.comments.all().order_by('-timestamp')

	def comment_count(self):
		return Comment.objects.filter(post=self).count()
		

	def save(self, *args, **kwargs):
		if self.slug == '':
			self.slug = slugify(self.title)[:10]
		return super().save(*args, **kwargs)

	class Meta:
		ordering = ['-created_date']



class Course(models.Model):
	title = models.CharField(max_length=200)
	body = RichTextField()
	categories = models.ManyToManyField(CategoryCourse)
	image = models.ImageField(upload_to='image-course/') 
	slug = models.SlugField(unique=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True) 
	author = models.ForeignKey(Account, on_delete=models.CASCADE)
	featured = models.BooleanField(default=False)


	def __str__(self):
		return str(self.title)


	def get_absolute_url(self):
		return reverse('blog:course-detail', kwargs={
			'slug':self.slug
			})
	def get_update_url(self):
		return reverse('blog:course-update', kwargs={
			'slug':self.slug
			})
	def get_delete_url(self):
		return reverse('blog:course-delete', kwargs={
			'slug':self.slug
			})

	@property
	def course_view_count(self):
		return CourseViewCount.objects.filter(course=self).count()

	def get_categories(self):
		return self.categories.all()

	def save(self, *args, **kwargs):
		if self.slug == '':
			self.slug = slugify(self.title)[:15]
		return super().save(*args, **kwargs)


	class Meta:
		ordering = ['-created_date']	


class Contact(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField(max_length=100)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['-timestamp'] 

