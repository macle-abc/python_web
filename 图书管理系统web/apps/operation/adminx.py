import xadmin

from .models import BorrowingInformation, ReadersWish, SuggestedInformation


class GlobalSettings:
    site_title = "图书管理系统"
    site_footer = "美度图书"


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)


class BorrowingInformationAdmin:
    list_display = ('user_account', 'book_ISBN', 'number_of_borrow',)
    list_filter = ('user_account', 'book_ISBN', 'number_of_borrow', 'borrowing_time', 'return_time',)


xadmin.site.register(BorrowingInformation, BorrowingInformationAdmin)


class ReadersWishAdmin:
    list_display = ('book_name', 'author',)
    search_fields = ('book_name', 'author',)
    list_filter = ('book_name', 'author',)


xadmin.site.register(ReadersWish, ReadersWishAdmin)


class SuggestedInformationAdmin:
    list_display = ('name', 'email',)
    search_fields = ('name', 'email', 'content',)
    list_filter = ('name', 'email',)


xadmin.site.register(SuggestedInformation, SuggestedInformationAdmin)
