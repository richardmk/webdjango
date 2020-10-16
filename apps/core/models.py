from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

class UserManager(BaseUserManager):
	
	def create_user(self, email, name, surname, password = None):
		if not email:
			raise ValueError('El usuario debe tener un correo electrónico.')
		
		user = self.model(email = self.normalize_email(email), name = name, surname = surname)
	   
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, name, surname, password):

		user = self.create_user(email, password=password,name = name, surname = surname)

		user.is_staff = True
		user.save(using=self._db)
		return user



class User(AbstractBaseUser):
	email = models.EmailField('Email', unique=True, max_length=100)
	name = models.CharField('Name', null=True, blank=True, max_length=100)
	surname = models.CharField('Surname', null=True, blank=True, max_length=100)
	picture = models.ImageField('Profile picture', upload_to='profile_picture', blank=True, null=True, max_length=200)
	date_birth = models.DateField('Date of Birth', null=True, blank=True, auto_now=False, auto_now_add=False)
	city =  models.CharField('City', null=True, blank=True, max_length=50)
	country = models.CharField('Country', null=True, blank=True, max_length=50)
	phone = models.CharField('Phone', null=True, blank=True, max_length=50)
	address = models.CharField('Address', null=True, blank=True, max_length=50)
	description = models.TextField()
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	
	def age(self):
		return int((datetime.now().date() - self.date_birth).days / 365.25)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name', 'surname',]

	def __str__(self):
		return f'{self.name} {self.surname}'
	
	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
	
	@property
	def if_staff(self):
		return self.is_staff



class Web(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	link = models.URLField('Link', max_length=200)

	def __str__(self):
		return self.link



class Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date = models.DateField('Start date', auto_now=False, auto_now_add=False)
	ending_date = models.DateField('Ending date', auto_now=False, auto_now_add=False)
	CHOICES = (('Education','Education'),('Professional Experience','Professional Experience'),('Pre-professional practices','Pre-professional practices'))
	type_experience = models.CharField('Type experience', choices=CHOICES, max_length=100)
	title = models.CharField('Title', null= False, max_length=50)
	subtitle = models.CharField('Subtitle', null= False, max_length=50)
	content_exerience = models.TextField()

	def __str__(self):
		return self.title



class Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField('Descripcion', null= False, max_length=100)
	CHOICES = [(i,i) for i in range(11)]
	value = models.PositiveSmallIntegerField('Value', choices=CHOICES)
	
	def __str__(self):
		return self.description



class Testimonial(models.Model):
	image = models.ImageField('Picture', upload_to='testimonials',  max_length=None)
	title = models.CharField('Title', max_length=50)
	subtitle = models.CharField('Subtitle', max_length=100)
	description = models.TextField()
	phone = models.CharField('Phone', max_length=50)

	def __str__(self):
			return self.title



class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField('Picture', upload_to='projects',  max_length=None)
	title = models.CharField('Title', max_length=50)
	url = models.CharField('Url', max_length=200, null=True, blank=True)

	def __str__(self):
			return self.title