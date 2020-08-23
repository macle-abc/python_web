from django.db import models


class BookInfo(models.Model):
    category_choices = [
        ('youth', '青春',),
        ('fiction', '小说',),
        ('literature', '文学',),
        ('art', '艺术',),
        ('tutorial', '教程',),
        ('humor', '动漫/幽默',),
        ('fashion', '娱乐时尚',),
        ('tourism', '旅游',),
        ('geography', '地图/地理',),
        ('life', '生活',),
        ('love', '婚恋',),
        ('growing', '育儿/成长',),
        ('health_care', '保健/心理健康',),
        ('physical_culture', '体育',),
        ('encouragement', '励志',),
        ('management', '管理',),
        ('economics', '经济',),
        ('law', '法律',),
        ('politics', '政治/军事',),
        ('philosophy', '哲学/宗教',),
        ('sociology', '社会科学',),
        ('ancient_books', '古籍',),
        ('culture', '文化',),
        ('history', '历史',),
        ('biography', '传记',),
        ('children', '少儿',),
        ('textbook', '中小学教辅',),
        ('foreign_language', '外语',),
        ('exam', '考试',),
        ('teaching_material', '教材',),
        ('reference_book', '工具书',),
        ('poplar_science_books', '科普读物',),
        ('computer', '计算机/网络',),
        ('medicine', '医学',),
        ('science', '科学技术',),
    ]
    number_of_existing = models.PositiveIntegerField(verbose_name="现存数量", default=0)
    category = models.CharField(max_length=30, choices=category_choices, db_index=True, verbose_name='类别',
                                default='youth')
    author = models.CharField(max_length=20, db_index=True, verbose_name='作者', help_text="最长不超过20个字符")
    introduction = models.TextField(verbose_name='简介')
    name = models.CharField(max_length=30, db_index=True, verbose_name='书名', help_text="最长不超过30个字符")
    added_time = models.DateField(db_index=True, verbose_name='上架时间', auto_now_add=True)
    ISBN = models.CharField(max_length=17, primary_key=True, verbose_name="ISBN号",
                            help_text="格式应为X-X-X-X-X(其中X为数字，2007年后为共计13位数字),包括-共计17个字符")
    publishing_company = models.CharField(max_length=20, verbose_name="出版社", help_text="最长不超过20个字符", db_index=True,
                                          default="")

    def __str__(self):
        return self.ISBN

    class Meta:
        verbose_name = "图书信息"
        verbose_name_plural = verbose_name


class BookImages(models.Model):
    book_ISBN = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书信息')
    image = models.ImageField(upload_to='books_images/%Y/%m/%d/', verbose_name='图书图片')

    def __str__(self):
        return str(self.book_ISBN)

    class Meta:
        verbose_name = "图书图片集"
        verbose_name_plural = verbose_name


class BookRecommendation(models.Model):
    book_ISBN = models.OneToOneField(BookInfo, on_delete=models.CASCADE, verbose_name='图书信息')
    current_recommended_time = models.DateTimeField(db_index=True, verbose_name="当前推荐数时间", auto_now=True, null=False)
    number_of_recommendation = models.PositiveIntegerField(verbose_name="推荐数", default=0, db_index=True)

    def __str__(self):
        return str(self.number_of_recommendation)

    class Meta:
        verbose_name = "图书推荐"
        verbose_name_plural = verbose_name
