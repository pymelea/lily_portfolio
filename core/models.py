from django.db import models


# Create your models here.


class Home(models.Model):
    # TODO: Define fields here}
    name = models.CharField(max_length=50)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class About(models.Model):
    # TODO: Define fields here}
    heading = models.CharField(max_length=50)
    carrer = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.carrer


class Profile(models.Model):
    # TODO: Define fields here}
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=500)
    cv = models.FileField(blank=True, null=True, upload_to='cv/')


# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    # TODO: Define fields here}
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


class Portfolio(models.Model):
    # TODO: Define fields here}
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=500)

    def __str__(self):
        return f'Portfolio {self.id}'


class Education(models.Model):
    name = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    first_date = models.DateField(blank=True, null=True)
    date_final = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    # TODO: Define fields here}
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    # TODO: Define fields here}
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    # TODO: Define fields here}
    name = models.CharField(max_length=50)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    picture_pro = models.ImageField(blank=True, null=True, upload_to='picture_pro/')
    description = models.TextField(max_length=500, blank=True, null=True)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name
