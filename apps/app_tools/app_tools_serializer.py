from app_exception import custom_exceptions


def get_view_from_serializer(serializer_obj):
    try:
        context=serializer_obj.context
        view_obj=context.get('view')
        return view_obj
    except:
        custom_exceptions.Status_503('系统发生计划外异常:不能从当前序列化器上下文中得到view对象')








