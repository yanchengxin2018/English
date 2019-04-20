# 只允许登录用户
class IsAuthPermission:
    message = '登录后才能记录你的信息哦'

    def has_permission(self, request, view):
        return True if request.user else False

    def has_object_permission(self, request, view, obj):
        return bool(request.user)
