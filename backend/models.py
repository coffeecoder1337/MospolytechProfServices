from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=500, blank=False, verbose_name="Заголовок")
    content = models.TextField(blank=False, verbose_name="Текст")
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created'])
        ]

