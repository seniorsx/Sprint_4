import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book_with_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        assert collector.books_genre['Книга'] == ''

    def test_add_new_book_add_book_with_empty_genre_and_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Очень длинное название, но меньше 40 символов')
        assert collector.books_genre['Очень длинное название, но меньше 40 символов'] == ''

    def test_add_new_book_does_not_add_invalid_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('A' * 41)
        assert ('A' * 41) not in collector.books_genre

    def test_add_new_book_does_not_add_invalid_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_set_book_genre_sets_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_does_not_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Поэзия')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1']

    def test_get_books_genre_returns_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Комедии')
        assert collector.get_books_genre() == {'Книга': 'Комедии'}

    def test_get_books_for_children_excludes_18plus_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Мультфильмы')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга1']

    def test_add_book_in_favorites_adds_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_add_book_in_favorites_ignores_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favourite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга_1')
        collector.add_new_book('Книга_2')
        collector.add_book_in_favorites('Книга_1')
        collector.add_book_in_favorites('Книга_2')
        assert collector.get_list_of_favorites_books() == ['Книга_1', 'Книга_2']
