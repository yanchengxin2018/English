from rest_framework import serializers
from app_databases.models import EnglishWordModel


#制作单词数据库
class MakeEnglishWordSerializer(serializers.ModelSerializer):

    class Meta:
        model=EnglishWordModel
        fields=('id','index','english','chinese','pronunciation',)

    def create(self, validated_data):
        index=validated_data.get('index')
        english_word_obj=EnglishWordModel.objects.filter(pk=index).first()
        if english_word_obj:
            serializer_update_obj=MakeEnglishWordSerializer(english_word_obj,validated_data)
            serializer_update_obj.is_valid(raise_exception=True)
            return serializer_update_obj.save()
        else:
            return super().create(validated_data)


#英语单词列表
class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWordModel
        fields = ('id', 'index', 'english', 'chinese', 'pronunciation',)













