from django.db import models


class Products(models.Model):
    name = models.CharField(
        max_length=30,
        default="",
        null=False,
        blank=False,
        help_text="产品名",
        verbose_name="产品名",
    )

    style = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text="产品风格",
        verbose_name="产品风格"
    )

    site = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        help_text="产品适用场地",
        verbose_name="产品适用场地",
    )
    feature = models.TextField(
        default="",
        null=True,
        blank=True,
        help_text="产品特点",
        verbose_name="产品特点",
    )
    key_word = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        help_text="产品关键词",
        verbose_name="产品关键词",
    )
    cover = models.ImageField(
        verbose_name="产品封面图片",
        help_text="产品封面图片",
        upload_to="images/products/cover/%Y/%m/%d",
        default="images/default/case.jpg",
    )


    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
        ordering = ['-name']

    def __str__(self):
        return self.name


class ProductsImages(models.Model):
    belong = models.ForeignKey(
        Products,
        related_name="products_images",
        on_delete=models.CASCADE,
        verbose_name="图片所属",
        help_text="图片所属"
    )
    image = models.ImageField(
        verbose_name="产品图片",
        help_text="产品图片",
        upload_to="images/products/%Y/%m/%d",
    )

    class Meta:
        verbose_name = "产品图片"
        verbose_name_plural = "产品图片"
        ordering = ['belong']
