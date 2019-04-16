

#只允许管理员进行这个操作
class IsManagerPermission:
    message='只允许系统管理员执行这个操作'

    def has_permission(self, request, view):
            return False

    def has_object_permission(self, request, view, obj):
        return False









