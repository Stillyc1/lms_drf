from django.db import models


class Course(models.Model):
    title = models.CharField(verbose_name='Название')
    picture = models.ImageField(verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(verbose_name='Название')
    picture = models.ImageField(verbose_name='Превью')
    description = models.TextField(verbose_name='Описание')
    video = models.URLField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses", verbose_name="курс")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
