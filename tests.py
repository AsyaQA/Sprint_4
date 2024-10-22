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

    def test_add_new_book_add_one_book_book_not_in_books_genre_and_len_book_from_1_to_40_add_book(self):

        collector = BooksCollector()

        collector.add_new_book('Русалочка')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_book_in_books_genre_and_genre_in_genre_set_book_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.books_genre == {'Шерлок Холмс': 'Детективы'}


    def test_get_book_genre_genre_in_genre_get_book_genre(self):

        collector = BooksCollector()

        collector.add_new_book('На чужой земле')
        collector.set_book_genre('На чужой земле', 'Фантастика')

        assert collector.get_book_genre('На чужой земле') == 'Фантастика'


    def test_get_books_with_specific_genre_book_in_books_genre_and_genre_in_genre_get_books_with_specific_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Хоббит')
        collector.add_new_book('Русалочка')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.set_book_genre('Русалочка', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Властелин колец', 'Хоббит']


    @pytest.mark.parametrize('name', ['Долг легиона', 'Курсант'])
    def test_get_books_genre_one_book_no_genre_get_books_genre(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == collector.books_genre


    def test_get_books_for_children_two_books_genre_not_in_genre_age_rating_get_books_for_children(self):

        collector = BooksCollector()

        collector.add_new_book('Хоббит')
        collector.add_new_book('Русалочка')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.set_book_genre('Русалочка', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Хоббит', 'Русалочка']


    def test_add_book_in_favorites_add_one_book_out_of_two_add_book_in_favorites(self):

        collector = BooksCollector()

        collector.add_new_book('Охотник на ведьм')
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')

        assert 'Война и мир' in collector.favorites


    def test_delete_book_from_favorites_delete_one_book_delete_book_from_favorites(self):

        collector = BooksCollector()

        collector.add_new_book('Золушка')
        collector.add_book_in_favorites('Золушка')
        collector.delete_book_from_favorites('Золушка')

        assert len(collector.favorites) == 0


    def test_get_list_of_favorites_books_add_two_book_get_list_of_favorites(self):

        collector = BooksCollector()

        collector.add_new_book('Кот в сапогах')
        collector.add_new_book('Красная шапочка')
        collector.add_book_in_favorites('Кот в сапогах')
        collector.add_book_in_favorites('Красная шапочка')

        assert collector.get_list_of_favorites_books() == ['Кот в сапогах', 'Красная шапочка']


    @pytest.mark.parametrize('name', ['', 'Жареные зеленые помидоры в кафе "Полустанок"'])
    def test_add_new_book_add_book_len_name_0_and_len_name_more_40_not_add_book(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.books_genre) == 0