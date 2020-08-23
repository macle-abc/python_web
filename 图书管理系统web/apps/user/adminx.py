import xadmin

from .models import UserInfo


class UserInfoAdmin:
    list_display = ('account', 'nickname', 'email', 'sex')
    search_fields = ('account', 'nickname', 'email')
    list_filter = ('sex',)


xadmin.site.register(UserInfo, UserInfoAdmin)
