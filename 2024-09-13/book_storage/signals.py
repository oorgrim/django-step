# book_storage/signals.py
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from django.contrib import messages
from .models import Book
from icecream import ic

# Сигнал для создания или обновления книги с добавлением сообщения
@receiver(post_save, sender=Book)
def send_email_on_create_update(sender, instance, created, **kwargs):
    request = kwargs.get('request')  # Получаем объект request, если он передан
    if created:
        subject = f'Новая книга создана: {instance.title}'
        message = f'Книга "{instance.title}" была успешно создана.'
        if request:
            messages.success(request, f'Книга "{instance.title}" успешно создана.')
    else:
        subject = f'Книга обновлена: {instance.title}'
        message = f'Книга "{instance.title}" была успешно обновлена.'
        if request:
            messages.success(request, f'Книга "{instance.title}" успешно обновлена.')

    ic(message, settings.DEFAULT_FROM_EMAIL)
    # Отправка email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],  # Замените на нужный email
        fail_silently=False,
    )

# Сигнал для удаления книги с добавлением сообщения
@receiver(post_delete, sender=Book)
def send_email_on_delete(sender, instance, **kwargs):
    request = kwargs.get('request')  # Получаем объект request, если он передан
    subject = f'Книга удалена: {instance.title}'
    message = f'Книга "{instance.title}" была успешно удалена.'

    if request:
        messages.success(request, f'Книга "{instance.title}" успешно удалена.')

    # Отправка email
    # send_mail(
    #     subject,
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     ['admin@example.com'],  # Замените на нужный email
    #     fail_silently=False,
    # )
