from django.shortcuts import render, render_to_response, redirect
from django.views.generic.base import View
from django.db.models import Q
from datetime import datetime, timedelta
from apps.books.models import BookImages, BookInfo, BookRecommendation
from .models import *
from .forms import LoginForm, ReaderWishForm, SuggestForm, RegisterForm
from apps.books.views import get_recommended_category, get_last_book_info


class test(View):
    def get(self, request, *args, **kwargs):
        suggestForm = SuggestForm()
        response = render(request, "test.html", {"suggestForm": suggestForm})
        print(request.session.get('test'))
        return response

    def post(self, request, *args, **kwargs):
        suggestForm = SuggestForm(request.POST)
        request.session['test'] = "django"
        print("保存成功")
        return render(request, "test.html", {"suggestForm": suggestForm})


def get_starnum_and_othernum(isbn) -> tuple:
    """根据isbn获取该书籍的推荐数及其分类，然后计算它在同类书籍总推荐数的排名，返回星星数和黄色星星数
        如果没有改ISBN那么返回None, None"""
    try:
        bookInfo = BookInfo.objects.values_list('ISBN', 'category').get(ISBN=isbn)
    except BookInfo.MultipleObjectsReturned as e:
        # 不应该的情况
        print(type(e), e)
    except BookInfo.DoesNotExist as e:
        # 没有该书籍信息
        return None, None
    else:
        # 存在该书籍信息
        # bookISBNLists = BookInfo.objects.values('ISBN').filter(category=bookInfo[1]).exclude(ISBN=bookInfo[0]).order_by('-bookrecommendation__number_of_recommendation')
        bookISBNList = BookRecommendation.objects.values('book_ISBN').filter(book_ISBN__category=bookInfo[1]).order_by(
            '-number_of_recommendation')

        index = 0
        if not bookISBNList:
            # 为空
            starNum = 5
        else:
            for book in bookISBNList:
                if book['book_ISBN'] == isbn:
                    break
                else:
                    index = index + 1
            # index 为当前书籍的排序下标
            percentage = index / len(bookISBNList)
            starNum = 0
            if percentage <= 0.2:
                starNum = 5
            elif percentage <= 0.4:
                starNum = 4
            elif percentage <= 0.6:
                starNum = 3
            elif percentage <= 0.8:
                starNum = 2
            else:
                starNum = 1
        return starNum, 5 - starNum


def get_footer_info() -> tuple:
    """返回(推荐列表，最新图书信息)"""
    recommended_category_list = get_recommended_category()
    category_dict_list = BookInfo.category_choices
    result_category_list = []  # 需要进行模板渲染
    for item in recommended_category_list:
        for each in category_dict_list:
            if item == each[0]:
                result_category_list.append(each)
    last_book_info_list = get_last_book_info()  # 需要仅需模板渲染
    return result_category_list, last_book_info_list


def get_cookies_isLogin_context(request) -> list:
    """返回cookies，isLogin, context{'isLogin', 'category_list', 'last_book_info_list'}"""
    cookies = request.COOKIES
    isLogin = False
    category_list, last_book_info_list = get_footer_info()
    context = {"isLogin": isLogin, "category_list": category_list, "last_book_info_list": last_book_info_list}
    result = [cookies, isLogin, context]
    return result


class SingleProduct(View):
    def get(self, request, *args, **kwargs):
        # result = get_cookies_isLogin_context(request)
        # cookies = result[0]
        # context = result[2]
        # if cookies:
        #     if 'isLogin' in cookies and cookies['isLogin'] == "True":
        #         context['isLogin'] = True
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        if 'ISBN' in kwargs:
            book_ISBN = kwargs['ISBN']
            # 存在没有上传图片的情况
            book_images = BookImages.objects.filter(book_ISBN=book_ISBN)
            if not len(book_images):
                book_images = [{
                    'image': {
                        'url': '/static/images/noImage.jfif',
                    }
                }]
            book_info = BookInfo.objects.get(ISBN=book_ISBN)
            category = book_info.category
            same_category_books = BookInfo.objects.filter(category=category).exclude(ISBN=book_ISBN).values_list('ISBN',
                                                                                                                 'name',
                                                                                                                 'author',
                                                                                                                 'number_of_existing')[
                                  :4]
            same_category_books_result = []
            # 推荐数倒序排序
            # 当前书的推荐数的下标占总数的
            for same_category_book in same_category_books:
                # 可能存在没有图片的情况
                try:
                    bookImage = BookImages.objects.filter(book_ISBN=same_category_book[0])[0]
                except IndexError as e:
                    # 该书没有上传图片
                    # 采用默认图片
                    bookImage = {'image':
                        {
                            'url': "/static/images/noImage.jfif",
                        },
                    }
                # all = BookRecommendation.objects.all().order_by('-number_of_recommendation')
                # index = 0
                # for item in all:
                #     if item.book_ISBN.ISBN == same_category_book[0]:
                #         break
                #     else:
                #         index += 1
                # percentage = index / len(all)
                # starNum = 0
                # if percentage < 0.2:
                #     starNum = 5
                # elif percentage < 0.4:
                #     starNum = 4
                # elif percentage < 0.6:
                #     starNum = 3
                # elif percentage < 0.8:
                #     starNum = 2
                # else:
                #     starNum = 1
                # bookRecommendation = BookRecommendation.objects.get(
                #     book_ISBN=same_category_book[0]).number_of_recommendation
                # 获取借阅数量
                borrow_count = 0
                # otherNum = 5 - starNum
                starNum, otherNum = get_starnum_and_othernum(same_category_book[0])
                try:
                    borrow_count = BorrowingInformation.objects.get(book_ISBN=same_category_book[0]).number_of_borrow
                except BorrowingInformation.DoesNotExist as e:
                    pass
                tempDict = {'all_count': borrow_count + same_category_book[3], 'ISBN': same_category_book[0],
                            'name': same_category_book[1], 'author': same_category_book[2],
                            'number_of_existing': same_category_book[3],
                            'image': bookImage.image.url if type(bookImage) != dict else bookImage['image']['url'],
                            'starNum': list(range(starNum)), 'otherNum': list(range(otherNum)), }
                same_category_books_result.append(tempDict)

            # 获取同类书籍
            # 图片 书名  作者 推荐数 现存数量
            context['same_category_books_result'] = same_category_books_result
            context['book_info'] = book_info  # 当前要展示的图书信息
            context['book_images'] = book_images  # 当前图书全部图片
            return render(request, "single_product.html", context)
        else:
            return redirect("operation:shop")

    def post(self, request, *args, **kwargs):
        return render(request, "single_product.html")


class Wish(View):
    # def get(self, request, *args, **kwargs):
    #     return render(request, "single_product.html")

    def post(self, request, *args, **kwargs):
        readerWishForm = ReaderWishForm(request.POST)
        if readerWishForm.is_valid():
            # 检查数据是否存在
            try:
                bookInfo = BookInfo.objects.get(name=readerWishForm.cleaned_data['name'])
            except BookInfo.DoesNotExist as e:
                ReadersWish.objects.create(book_name=readerWishForm.cleaned_data['name'],
                                           author=readerWishForm.cleaned_data['author'],
                                           other_info=readerWishForm.cleaned_data['other'])
                return redirect(request.headers._store['referer'][1])
            except BookInfo.MultipleObjectsReturned as e:
                return redirect('operation:single_product', ISBN=
                BookInfo.objects.values('ISBN').filter(name=readerWishForm.cleaned_data['name'])[0]['ISBN'])
            else:
                return redirect('operation:single_product', ISBN=bookInfo.ISBN)
        else:
            return redirect(request.headers._store['referer'][1])


class Suggest(View):
    def post(self, request, *args, **kwargs):
        suggestForm = SuggestForm(request.POST)
        if suggestForm.is_valid():
            SuggestedInformation.objects.create(name=suggestForm.cleaned_data['name'],
                                                email=suggestForm.cleaned_data['email'],
                                                content=suggestForm.cleaned_data['suggest'])
        return redirect('operation:contact')


class Contact(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        return render(request, "contact.html", context)


class Search(View):
    def post(self, request, *args, **kwargs):
        # 率先判断书名
        # 然后书名没有则为作者
        if 'search' in request.POST:
            # 处理
            keyword = request.POST['search']
            bookInfo = BookInfo.objects.filter(name=keyword)
            if bookInfo:
                bookInfo = bookInfo[0]
                # 返回到详情页
                return redirect('operation:single_product', ISBN=bookInfo.ISBN)
            else:
                # 丢给shop，作者处理
                return redirect('operation:shop_author_get', author=keyword)
        else:
            return redirect(request.headers._store['referer'][1])


class Process(View):
    def post(self, request, *args, **kwargs):
        dataList = []
        for name, value in request.POST.items():
            if name.startswith('ISBN'):
                dataList.append(value)
            elif name.startswith('count'):
                dataList.append(value)
        result = []
        for index, value in enumerate(dataList):
            if not index % 2:
                result.append({
                    'ISBN': value,
                    'count': dataList[index + 1],
                })
        account = kwargs['account']
        # 更新书籍信息
        errorList = []
        for item in result:
            bookInfos = BookInfo.objects.get(ISBN=item['ISBN'])
            if bookInfos.number_of_existing >= int(item['count']):
                # 允许借阅
                bookInfos.number_of_existing = bookInfos.number_of_existing - int(item['count'])
                bookInfos.save()
                # 更新用户借阅表
                # 判断是否已经存在该记录
                try:
                    borrowInfo = BorrowingInformation.objects.get(user_account=account, book_ISBN=item['ISBN'])
                except BorrowingInformation.DoesNotExist as e:
                    BorrowingInformation.objects.create(user_account=UserInfo.objects.get(account=account),
                                                        book_ISBN=BookInfo.objects.get(ISBN=item['ISBN']),
                                                        number_of_borrow=int(item['count']),
                                                        borrowing_time=datetime.now(),
                                                        return_time=datetime.now() + timedelta(days=30))
                else:
                    borrowInfo.number_of_borrow = borrowInfo.number_of_borrow + int(item['count'])
                    borrowInfo.save()

            else:
                temp = bookInfos.number_of_existing
                bookInfos.number_of_existing = 0
                bookInfos.save()
                try:
                    borrowInfo = BorrowingInformation.objects.get(user_account=account, book_ISBN=item['ISBN'])
                except BorrowingInformation.DoesNotExist as e:
                    BorrowingInformation.objects.create(user_account=UserInfo.objects.get(account=account),
                                                        book_ISBN=BookInfo.objects.get(ISBN=item['ISBN']),
                                                        number_of_borrow=temp,
                                                        borrowing_time=datetime.now(),
                                                        return_time=datetime.now() + timedelta(days=30))
                else:
                    borrowInfo.number_of_borrow = borrowInfo.number_of_borrow + temp
                    borrowInfo.save()
                error = {
                    'ISBN': item['ISBN'],
                    'message': f"由于库存不足，只允许借阅{temp}本"
                }
                errorList.append(error)
        errorMessage = ""
        for error in errorList:
            errorMessage = f"{errorMessage}ISBN:{error['ISBN']},错误信息:{error['message']}\\n"
        request.session.flush()
        if errorList:
            return render(request, "tips.html", {"message": errorMessage, "url": "/operation/shop/"})
        else:
            return render(request, "tips.html", {"message": "借阅成功!", "url": "/operation/shop/"})


class Delete(View):
    def get(self, request, *args, **kwargs):
        if 'ISBN' in kwargs:
            ISBN = kwargs['ISBN']
            import json
            userWish = json.loads(request.session.get('userWish'))
            wishList = userWish['wishList']
            bookInfos = []
            for wish in wishList:
                if wish['ISBN'] == ISBN:
                    wishList.remove(wish)
                    break
            userWish['wishList'] = wishList
            request.session['userWish'] = json.dumps(userWish)
            return redirect(request.headers._store['referer'][1])


class Checkout(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        # 需要获取租借信息
        # 展示字段有，图书图片，isbn，数量，书名
        import json
        temp = request.session.get('userWish')
        if not temp:
            userWish = {
                'wishList': []
            }
        else:
            userWish = json.loads(request.session.get('userWish'))
        wishList = userWish['wishList']
        # print(wishList)
        bookInfos = []
        for wish in wishList:
            tempData = {}
            ISBN = wish['ISBN']
            tempData['ISBN'] = ISBN
            bookInfo = BookInfo.objects.values_list('ISBN', 'name').get(ISBN=ISBN)
            # 获取图书图片
            bookImage = BookImages.objects.values('image').filter(book_ISBN=ISBN)
            if bookImage:
                bookImage = '/media/' + bookImage[0]['image']

                # 不止一个
            else:
                bookImage = "/static/images/noImage.jfif"
            tempData['imageUrl'] = bookImage
            tempData['count'] = wish['count']
            tempData['name'] = bookInfo[1]
            bookInfos.append(tempData)
        context['all_num'] = len(bookInfos)
        context['bookInfos'] = bookInfos
        return render(request, "checkout.html", context)

    def post(self, request, *args, **kwargs):
        # 唯一需要处理的就是isbn
        cookies = request.COOKIES
        if 'isLogin' in cookies and cookies['isLogin'] and 'account' in cookies:
            # redis维护状态
            account = cookies['account']
            ISBN = request.POST['ISBN']
            # 首先获取用户当前心愿
            import json
            userWish = request.session.get('userWish')
            if userWish:
                userWish = json.loads(userWish)
                # 更新用户心愿
                isChange = False
                for item in userWish['wishList']:
                    if item['ISBN'] == ISBN:
                        index = userWish['wishList'].index(item)
                        userWish['wishList'][index]['count'] = userWish['wishList'][index]['count'] + 1
                        isChange = True
                        break
                if not isChange:
                    # 添加新数据
                    userWish['wishList'].append({
                        'ISBN': ISBN,
                        'count': 1,
                    })
            else:
                wishList = [
                    {
                        'ISBN': ISBN,
                        'count': 1,
                    },
                ]
                userWish = {
                    'account': account,
                    'wishList': wishList
                }
            request.session['userWish'] = json.dumps(userWish)
            return render(request, "tips.html", {"message": "添加成功!", "url": request.headers._store['referer'][1][21:]})
        else:
            return render(request, "tips.html", {"message": "请登录后进行操作", "url": "/operation/login"})


class Thumbs(View):
    def get(self, request, *args, **kwargs):
        cookies = request.COOKIES
        if 'isLogin' in cookies and cookies['isLogin']:
            try:
                bookRecommendation = BookRecommendation.objects.get(book_ISBN=kwargs['ISBN'])
            except BookRecommendation.DoesNotExist as e:
                BookRecommendation.objects.create(book_ISBN=BookInfo.objects.get(ISBN=kwargs['ISBN']),
                                                  number_of_recommendation=1)
                return render(request, "tips.html",
                              {"message": "推荐成功!", "url": request.headers._store['referer'][1][21:]})
            else:
                bookRecommendation.number_of_recommendation = bookRecommendation.number_of_recommendation + 1
                bookRecommendation.save()
                return render(request, "tips.html",
                              {"message": "推荐成功!", "url": request.headers._store['referer'][1][21:]})
            # 处理
        else:
            return render(request, "tips.html", {"message": "请登录后进行推荐", "url": "/operation/login"})


class Shop(View):
    #  path('shop/', Shop.as_view(), name="shop"),  # 默认显示全部
    #
    #     path('shop/categories/<path:category>', Shop.as_view(), name="shop_categories"),  # 根据图书分类过滤  get请求
    #
    #     path('shop/author/', Shop.as_view(), name="shop_author"),  # 根据作者过滤 post请求 redirect到get请求
    #     path('shop/author/<path:author>', Shop.as_view(), name="shop_author_get"),
    #
    #     path('shop/added_time/', Shop.as_view(), name="shop_added_time"), # 根据时间过滤 post请求 redirect到get请求
    #     path('shop/added_time/<path:added_time>', Shop.as_view(), name="shop_added_time_get"),
    #
    #     path('shop/recommend/<path:recommend>', Shop.as_view(), name="shop_recommend"), # 根据喜欢程度过滤 get请求
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        context['categories'] = BookInfo.category_choices
        # 图书图片， 书名， 作者， 推荐数， 现存， 共计
        bookInfos = None
        if 'category' in kwargs and kwargs['category'] in [item[0] for item in BookInfo.category_choices]:
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').filter(
                category=kwargs['category']
            )

        # 根据图书分类过滤
        elif 'category' in kwargs and kwargs['category'] == "inline":
            categories = request.session.get('categories')
            # print("key", request.session.session_key)

            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').filter(
                category__in=categories
            )

        # 根据作者过滤
        elif 'author' in kwargs and kwargs['author'] == 'inline':
            author = request.session.get('author')
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').filter(
                author=author
            )

        elif 'author' in kwargs:
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').filter(
                author=kwargs['author']
            )

        # 根据日期过滤
        elif 'added_time' in kwargs and kwargs['added_time'] == 'inline':
            added_time = request.session.get('added_time')[0]
            from datetime import datetime, timedelta
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').filter(
                added_time__gte=datetime.now() - timedelta(days=30 * int(added_time))
            )

        # 根据喜欢程度过滤
        elif 'recommend' in kwargs:
            # 获取所有书籍信息
            recommend = kwargs['recommend']
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow')
            tempList = []
            for temp in bookInfos:
                starNum, otherNum = get_starnum_and_othernum(temp[0])
                if starNum == recommend:
                    tempList.append(temp)
            bookInfos = tempList

        else:
            bookInfos = BookInfo.objects.values_list('ISBN', 'name', 'author',
                                                     'bookrecommendation__number_of_recommendation',
                                                     'number_of_existing',
                                                     'borrowinginformation__number_of_borrow').all()

        bookInfoList = []
        if bookInfos:
            # 不为空
            # 遍历

            for bookInfo in bookInfos:
                # bookInfo为tuple     isbn, name, author, 推荐数， 现存数目， 借阅数目
                tempData = {
                }
                bookImage = BookImages.objects.filter(book_ISBN=bookInfo[0])
                if not bookImage:  # 为空
                    bookImage = "/static/images/noImage.jfif"
                else:  # 有数据
                    bookImage = bookImage[0].image.url
                tempData['ISBN'] = bookInfo[0]
                tempData['imageUrl'] = bookImage
                tempData['name'] = bookInfo[1]
                tempData['author'] = bookInfo[2]
                # tempData['recommendation'] = bookInfo[3]
                starNum, otherNum = get_starnum_and_othernum(bookInfo[0])
                tempData['starNum'] = list(range(starNum))
                tempData['otherNum'] = list(range(otherNum))
                tempData['number_of_existing'] = bookInfo[4]
                tempData['all_number'] = int(bookInfo[4]) + int(bookInfo[5] if bookInfo[5] else 0)
                bookInfoList.append(tempData)
        context['bookInfoList'] = bookInfoList  # 书籍信息
        return render(request, "shop.html", context)

    def post(self, request, *args, **kwargs):
        # result = get_cookies_isLogin_context(request)
        # cookies = result[0]
        # context = result[2]
        # if cookies:
        #     if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
        #         context['isLogin'] = True
        #         account = cookies['account']
        #         # 获取用户信息
        #         try:
        #             userInfo = UserInfo.objects.get(account=account)
        #         except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
        #             return redirect("operation:login")
        #         else:
        #             context['userInfo'] = userInfo
        # context['categories'] = BookInfo.category_choices
        if 'category' in kwargs and kwargs['category'] == "categories":
            categories = request.POST.getlist('categories')
            # 转发给get请求
            request.session['categories'] = categories
            response = redirect("operation:shop_categories", category="inline")
            # response.set_cookie("session_shop_id", request.session.session_key)
        if 'author' in kwargs and kwargs['author'] == "author":
            author = request.POST['author']
            request.session['author'] = author
            response = redirect("operation:shop_author_get", author="inline")
        if 'added_time' in kwargs and kwargs['added_time'] == 'added_time':
            added_time = request.POST.getlist('added_time')
            request.session['added_time'] = added_time
            response = redirect("operation:shop_added_time_get", added_time="inline")
        return response


class About(View):
    def get(self, request, *args, **kwargs):
        # 允许过滤
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        return render(request, "about.html", context)


class ForGot(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        return render(request, "forgot.html", context)

    def post(self, request, *args, **kwargs):
        # 账号，密保问题，答案
        account = request.POST['account']
        security_question = request.POST['security_question']
        answer = request.POST['answer']
        password = request.POST['password']
        try:
            userInfo = UserInfo.objects.get(account=account, security_question=security_question, answer=answer)
        except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
            # 失败
            return redirect('operation:forgot')
        else:
            # 成功
            userInfo = UserInfo.objects.get(account=account)
            userInfo.password = password
            userInfo.save()
            response = render_to_response('tips.html', {'message': "密码修改成功!", 'url': "/operation/index"})
            response.set_cookie("isLogin", "True", max_age=3600 * 10)
            response.set_cookie("account", account, max_age=3600 * 10)
            return response


class Index(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
        books_count = len(BookInfo.objects.all())
        books_categories_count = len(BookInfo.objects.values('category').distinct())
        # 获取每日推荐

        recommendationList = BookRecommendation.objects.order_by('-number_of_recommendation')[:8]
        booksInfoList = []
        for recommendation in recommendationList:
            bookInfo = {}
            bookInfo['id'] = recommendation.book_ISBN_id
            tempBookInfo = BookInfo.objects.get(ISBN=bookInfo['id'])
            bookInfo['name'] = tempBookInfo.name
            bookInfo['author'] = tempBookInfo.author
            bookInfo['introduction'] = tempBookInfo.introduction
            tempBookImage = BookImages.objects.filter(book_ISBN=bookInfo['id'])
            try:
                bookInfo['image'] = tempBookImage[0].image
            except IndexError as e:
                bookInfo['image'] = {
                    'url': '/static/images/noImage.jfif',
                }
            # print(bookInfo['image'].url)
            booksInfoList.append(bookInfo)
        # print(booksInfoList)
        # 书名简介作者，图片
        context['booksInfoListLength'] = len(booksInfoList)
        mid = len(booksInfoList) // 2
        context['booksInfoList'] = booksInfoList[mid:]
        context['booksInfoListActive'] = booksInfoList[:mid]
        context['books_count'] = books_count
        context['books_categories_count'] = books_categories_count
        return render(request, "index.html", context)


class Login(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True":
                context['isLogin'] = True
                return redirect("/operation/index", context)
            else:
                registerForm = RegisterForm()
                context['registerForm'] = registerForm
                return render(request, "login.html", context)
        else:
            registerForm = RegisterForm()
            context['registerForm'] = registerForm
            return render(request, "login.html", context)

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        msg = ""
        if login_form.is_valid():
            # 通过数据库来检查
            try:
                account = login_form.cleaned_data['account']
                password = login_form.cleaned_data['password']
                userInfo = UserInfo.objects.get(account=str(account), password=str(password))
            except UserInfo.DoesNotExist as e:
                msg = "账号或密码错误"
                return render(request, "login.html", {"login_form": login_form, "msg": msg})
            else:
                # response = redirect("/operation/index")
                response = render_to_response("tips.html", {"message": "登录成功!", "url": "/operation/index"})
                if "remember" in request.POST and str(request.POST['remember']) == "1":
                    response.set_cookie("isLogin", "True", max_age=3600 * 24 * 2)
                    response.set_cookie("account", str(account), max_age=3600 * 24 * 2)
                else:
                    response.set_cookie("isLogin", "True")
                    response.set_cookie("account", str(account))
                return response
        else:
            msg = "账号或密码格式不正确"
            return render(request, "login.html", {"login_form": login_form, "msg": msg})


class RegisterView(View):
    # def get(self, request, *args, **kwargs):
    #     registerForm = RegisterForm()
    #     return render(request, "login.html", {"registerForm": registerForm})

    def post(self, request, *args, **kwargs):
        registerForm = RegisterForm(request.POST, request.FILES)
        if registerForm.is_valid():
            registerForm.save()
            response = render_to_response("tips.html", {"message": "注册成功!", "url": "/operation/index"})
            response.set_cookie("isLogin", "True", max_age=3600 * 10)
            response.set_cookie("account", str(registerForm.cleaned_data['account']), max_age=3600 * 10)
            return response
        else:
            return redirect("operation:login")


class UserRentalView(View):
    def get(self, request, *args, **kwargs):
        result = get_cookies_isLogin_context(request)
        cookies = result[0]
        context = result[2]
        if cookies:
            if 'isLogin' in cookies and cookies['isLogin'] == "True" and 'account' in cookies:
                context['isLogin'] = True
                account = cookies['account']
                # 获取用户信息
                try:
                    userInfo = UserInfo.objects.get(account=account)
                except (UserInfo.DoesNotExist, UserInfo.MultipleObjectsReturned) as e:
                    return redirect("operation:login")
                else:
                    context['userInfo'] = userInfo
                    # 判断id
                    page = kwargs['page']
                    """ 要显示的分页栏
                                          有:
                                              分页栏的条数为5
                                              首页 上一页(如果当前页为1不显示) 1 2 3 4 5 下一页(如果当前页为最后一页不显示) 尾页
                                              如果当前页为6,尾页不足10,那么只显示6-最后,否则显示到10
                                              如果当前页为7,尾页不足10,那么只显示6-最后,否则显示到10
                    """
                    # 每页显示的记录数目
                    eachPageShowRentalsNum: int = 4
                    rentalInfos = BorrowingInformation.objects.filter(user_account=account)
                    countRenal = len(rentalInfos)
                    context['showPaging'] = False if countRenal < eachPageShowRentalsNum else True
                    results = rentalInfos.filter(user_account=account).values_list(
                        'book_ISBN', 'book_ISBN__name', 'book_ISBN__author', 'number_of_borrow',
                        'borrowing_time', 'return_time',
                    ).order_by('-return_time')
                    if context['showPaging']:
                        # 保存首页和最后一页
                        context['first'] = 1
                        context[
                            'end'] = countRenal // eachPageShowRentalsNum if not countRenal % eachPageShowRentalsNum else (
                                countRenal // eachPageShowRentalsNum + 1)
                        # 分页每次5页
                        eachPageShowItemNum = 5
                        # 决定是否显示上一页和下一页,及其上一页和下一页的页数
                        context['showPrev'] = True if page != 1 else False
                        context['prev'] = page - 1 if context['showPrev'] else None
                        context['showNext'] = True if page != context['end'] else False
                        context['next'] = page + 1 if context['showNext'] else None

                        # 决定显示的分页数目
                        if not page % eachPageShowItemNum:
                            currentEnd = page
                            currentStart = page - eachPageShowItemNum + 1
                        else:
                            currentEnd = context['end'] \
                                if context['end'] < (page // eachPageShowItemNum + 1) * eachPageShowItemNum \
                                else (page // eachPageShowItemNum + 1) * eachPageShowItemNum
                            currentStart = (page // eachPageShowItemNum) * eachPageShowItemNum \
                                if page // eachPageShowItemNum \
                                else 1
                        currentRange = range(currentStart, currentEnd + 1)
                        context['currentRange'] = currentRange
                        results = results[(page - 1) * eachPageShowRentalsNum: page * eachPageShowRentalsNum]
                    context['results'] = results
                    return render(request, "rental.html", context)
            else:
                return redirect("operation:login")
        else:
            return redirect("operation:login")

    def post(self, request, *args, **kwargs):
        if 'ISBN' in request.POST:
            ISBN = request.POST['ISBN']
            account = request.COOKIES['account']
            try:
                borrowingInfo = BorrowingInformation.objects.get(book_ISBN=ISBN, user_account=account)
            except BorrowingInformation.DoesNotExist as e:
                return redirect("operation:rental", 1)
            else:
                number_of_borrow = borrowingInfo.number_of_borrow
                # 销毁该记录
                borrowingInfo.delete()
                # 更新书籍信息
                try:
                    bookInfo = BookInfo.objects.get(ISBN=ISBN)
                except BookInfo.DoesNotExist as e:
                    return redirect("operation:rental", 1)
                else:
                    bookInfo.number_of_existing = bookInfo.number_of_existing + number_of_borrow
                    bookInfo.save()
                    return render(request, "tips.html", {"message": "归还成功!", "url": "/operation/rental/1"})
        else:
            return redirect("operation:rental", 1)
