# 只允许管理员进行这个操作
class IsManagerPermission:
    message = '只允许系统管理员执行这个操作'

    def has_permission(self, request, view):
        password=request.GET.get('password',None)
        if password=='Ycx17686988582':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return False
