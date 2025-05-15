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
    @pytest.fixture
    def collector():
        collector = BooksCollector()
        collector.init()
        return collector


    @pytest.mark.parametrize('book_name', ['Книга', 'Очень длинное название, но меньше 40 символов'])
    def test_add_new_book_adds_book_with_empty_genre(collector, book_name):
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''


    @pytest.mark.parametrize('invalid_name', ['', 'A' * 41])
    def test_add_new_book_does_not_add_invalid_name(collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.books_genre


    def test_set_book_genre_sets_valid_genre(collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'


    def test_set_book_genre_does_not_set_invalid_genre(collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Поэзия')
        assert collector.get_book_genre('Книга') == ''


    def test_get_books_with_specific_genre_returns_correct_books(collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1']


    def test_get_books_genre_returns_full_dictionary(collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Комедии')
        assert collector.get_books_genre() == {'Книга': 'Комедии'}


    def test_get_books_for_children_excludes_18plus_genres(collector):
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Мультфильмы')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга1']


    def test_add_book_in_favorites_adds_only_once(collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']


    def test_add_book_in_favorites_ignores_nonexistent_book(collector):
        collector.add_book_in_favorites('Неизвестная книга')
        assert collector.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_removes_book(collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []
