from django.contrib import admin  # Djangoのadminモジュールをインポート
from django.contrib.auth.admin import UserAdmin  # auth.adminからUserAdminクラスをインポート
from .models import *  # 現在のアプリのmodels.pyからすべてのクラスをインポート

class CustomUserModelAdmin(UserAdmin):  # UserAdminを継承したCustomUserModelAdminクラスを定義
    list_display = ('name', 'email', 'is_active', 'is_staff')  # 管理画面のユーザーリストで表示するフィールド

    fieldsets = (  # ユーザー編集画面でのフィールドのグループ化
        (None, {'fields': ('email', 'password')}),  # 基本情報
        ('Personal info', {'fields': ('name',)}),  # 個人情報
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # 権限設定
        ('Important dates', {'fields': ('last_login',)}),  # 重要な日付情報
    )

    add_fieldsets = (  # ユーザー追加画面でのフィールドのグループ化
        (None, {
            'classes': ('wide',),  # CSSクラス
            'fields': ('email', 'name', 'password1', 'password2'),  # フィールド
        }),
    )

    search_fields = ('email',)  # 管理画面での検索フィールド
    ordering = ('email',)  # 管理画面でのソート順

admin.site.register(CustomUserModel, CustomUserModelAdmin)  # CustomUserModelをCustomUserModelAdminで管理画面に登録