# qa_python_sprint_4

## 1. test_add_new_book_add_one_book_book_not_in_books_genre_and_len_book_from_1_to_40_add_book
Данный тест проверяет добавление одной книги, которой нет в списке books_genre, название книги содержит от 1 до 40 символов.

## 2. test_set_book_genre_book_in_books_genre_and_genre_in_genre_set_book_genre
Данный тест проверяет присвоение книге, которая есть в списке books_genre, жанра, который есть в списке genre.

## 3. test_get_book_genre_genre_in_genre_get_book_genre
Данный тест проверяет возвращение жанра книги, жанр которой есть в списке genre.

## 4. test_get_books_with_specific_genre_book_in_books_genre_and_genre_in_genre_get_books_with_specific_genre
Данный тест проверяет вывод список книг с определённым жанром.

## 5. test_get_books_genre_one_book_no_genre_get_books_genre
Данный тест проверяет мотод, который должен возвращать словарь books_genre.

## 6. test_get_books_for_children_two_books_genre_not_in_genre_age_rating_get_books_for_children
Данный тест проверяет метод, который возвращает книги, которые подходят детям.

## 7. test_add_book_in_favorites_add_one_book_out_of_two_add_book_in_favorites
Данный тест проверяет метод, который добавляет книги в избранное.

## 8. test_delete_book_from_favorites_delete_one_book_delete_book_from_favorites
Данный тест проверяет удаление книги из списка избранное.

## 9. test_get_list_of_favorites_books_add_two_book_get_list_of_favorites
Данный тест проверяет метод получения списка избранного.

## 10. test_add_new_book_add_book_len_name_0_and_len_name_more_40_not_add_book
Неативный тест, который проверяет, что метод add_new_book не добавляет в список books_genre книги в названии которых нет символов или их больше 40.