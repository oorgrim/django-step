from django.db.models.signals import post_save, post_delete
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Book
from .forms import BookForm


# Представление для списка книг с поиском
class BookListView(ListView):
    model = Book
    template_name = "book_storage/book_list.html"
    context_object_name = "books"

    # Добавляем возможность поиска по названию книги
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return Book.objects.all()


# Представление для создания книги
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book_storage/book_form.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # После успешного сохранения, передаем request в сигнал post_save
        post_save.send(
            sender=Book, instance=self.object, created=True, request=self.request
        )
        return response


# Представление для обновления книги
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book_storage/book_form.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Передаем request в сигнал post_save после успешного обновления
        post_save.send(
            sender=Book, instance=self.object, created=False, request=self.request
        )
        return response


# Представление для удаления книги
class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_storage/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")

    def delete(self, request, *args, **kwargs):
        # Получаем объект книги для передачи в сигнал
        self.object = self.get_object()
        response = super().delete(request, *args, **kwargs)
        # Передаем request в сигнал post_delete после успешного удаления
        post_delete.send(sender=Book, instance=self.object, request=request)
        return response