import xadmin

from .models import BookInfo, BookImages, BookRecommendation


class BookInfoAdmin:
    list_display = ('name', 'author', 'number_of_existing', 'category', 'publishing_company',)
    search_fields = ('name', 'author', 'ISBN', 'publishing_company',)
    list_filter = ('category', 'author', 'added_time', 'publishing_company',)


xadmin.site.register(BookInfo, BookInfoAdmin)


class BookImagesAdmin:
    # image
    list_display = ('get_name', 'book_ISBN', 'image',)
    list_filter = ('book_ISBN',)

    # def get_tname(self, obj):
    #     return '%s' % obj.tid.tname  # ☆☆☆☆☆
    #
    # get_tname.short_description = '老师'
    def get_name(self, obj):
        return f"{obj.book_ISBN.name}"
    get_name.short_description = "书名"


xadmin.site.register(BookImages, BookImagesAdmin)


class BookRecommendationAdmin:
    list_display = ('get_name', 'book_ISBN', 'current_recommended_time', 'number_of_recommendation',)
    list_filter = ('number_of_recommendation',)
    refresh_times = [10, 30, 60, ]
    def get_name(self, obj):
        return f"{obj.book_ISBN.name}"
    get_name.short_description = "书名"


xadmin.site.register(BookRecommendation, BookRecommendationAdmin)



