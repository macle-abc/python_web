from django.shortcuts import render
from .models import BookRecommendation, BookInfo


def get_recommended_category() -> tuple:
    bookRecommendationList = BookRecommendation.objects.order_by('-number_of_recommendation')
    result = []
    category_count_dict = {}
    if bookRecommendationList:
        bookRecommendationList = bookRecommendationList[:100]  # 根据推荐前100
        for book in bookRecommendationList:
            bookInfo = BookInfo.objects.get(ISBN=book.book_ISBN_id)
            if bookInfo.category in category_count_dict:
                category_count_dict[bookInfo.category] += 1  # 书的类别
            else:
                category_count_dict[bookInfo.category] = 1
        result = sorted(category_count_dict.items(), key=lambda x: x[1], reverse=True)
        temp = []
        for item in result:
            temp.append(item[0])
        result = temp[:8]
    return tuple(result)


def get_last_book_info() -> list:
    # 书名 ，上架时间， ISBN
    result = []
    books_info = BookInfo.objects.order_by("-added_time")
    if books_info:
        for book_info in books_info:
            name = book_info.name
            added_time = book_info.added_time
            ISBN = book_info.ISBN
            result.append((ISBN, name, added_time,))
    return result[:4]
