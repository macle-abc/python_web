from django.db import models

from ..user.models import UserInfo
from ..books.models import BookInfo


class BorrowingInformation(models.Model):
    user_account = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户账号")
    book_ISBN = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="图书ISBN")
    number_of_borrow = models.PositiveIntegerField(verbose_name="借阅数量", db_index=True)
    borrowing_time = models.DateTimeField(verbose_name="借阅时间", db_index=True, auto_now_add=True)
    return_time = models.DateTimeField(verbose_name="归还时间", db_index=True)

    def __str__(self):
        return str(self.user_account) + "借阅:" + str(self.book_ISBN)

    class Meta:
        verbose_name = "借阅信息"
        verbose_name_plural = verbose_name
        unique_together = ('user_account', 'book_ISBN',)


class SuggestedInformation(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20, help_text="最长不超过20个字符")
    email = models.EmailField(verbose_name="邮箱")
    content = models.TextField(verbose_name="建议内容")

    def __str__(self):
        return str(self.name) + "的建议"

    class Meta:
        verbose_name = "建议信息"
        verbose_name_plural = verbose_name


class ReadersWish(models.Model):
    book_name = models.CharField(verbose_name="书名", db_index=True, max_length=30, help_text="最长不超过30个字符")
    author = models.CharField(max_length=20, db_index=True, verbose_name='作者', help_text="最长不超过20个字符")
    other_info = models.TextField(verbose_name="其他书籍相关信息")

    def __str__(self):
        return "读者想要:" + self.book_name

    class Meta:
        verbose_name = "读者心愿"
        verbose_name_plural = verbose_name
