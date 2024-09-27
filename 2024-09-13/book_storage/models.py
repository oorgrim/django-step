from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)
    author = models.CharField(verbose_name="Автор", max_length=200)
    published_date = models.DateField(verbose_name="Дата публикации", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
