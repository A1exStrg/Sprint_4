from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize('book_name', ['HarryPotter', 'Война и мир', 'Золушка'])
    def test_add_book_name_book_in_dict(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_book_name_genre_is_none(self):
        collector = BooksCollector()
        book_name = 'HarryPotter'
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''

    @pytest.mark.parametrize('book_name, genre_name',
                             [
                                 ['HarryPotter', 'Фантастика'],
                                 ['Война и мир', 'Детективы'],
                                 ['Золушка', 'Мультфильмы']
                             ])
    def test_set_book_genre_book_has_genre(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.books_genre[book_name] == genre_name

    @pytest.mark.parametrize('book_name, genre_name',
                             [
                                 ['HarryPotter', 'Фантастика'],
                                 ['Война и мир', 'Детективы'],
                                 ['Золушка', 'Мультфильмы']
                             ])
    def test_get_book_genre_get_genres(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_book_genre(book_name) == genre_name

    @pytest.mark.parametrize('book_name, genre_name',
                             [
                                 ['HarryPotter', 'Фантастика'],
                                 ['Война и мир', 'Детективы'],
                                 ['Золушка', 'Мультфильмы']
                             ])
    def test_get_books_with_specific_genre_get_specific_book(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert book_name in collector.get_books_with_specific_genre(genre_name)

    @pytest.mark.parametrize('book_name, genre_name',
                             [
                                 ['HarryPotter', 'Фантастика'],
                                 ['Война и мир', 'Детективы'],
                                 ['Золушка', 'Мультфильмы']
                             ])
    def test_get_books_genre_get_genre(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert book_name in collector.books_genre
        assert collector.get_book_genre(book_name) == genre_name

    @pytest.mark.parametrize('book_name, genre_name',
                             [
                                 ['HarryPotter', 'Фантастика'],
                                 ['Война и мир', 'Мультфильмы'],
                                 ['Золушка', 'Мультфильмы']
                             ])
    def test_get_books_for_children_get_books_for_child(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize('book_name', ['HarryPotter', 'Война и мир', 'Золушка'])
    def test_add_book_in_favorites_fav_book_in_dict(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_delete_book_from_favorites_book_remove_dict(self):
        collector = BooksCollector()
        book_name = 'HarryPotter'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites

    def test_get_list_of_favorites_books_get_fav_books(self):
        collector = BooksCollector()
        book_name = 'HarryPotter'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()