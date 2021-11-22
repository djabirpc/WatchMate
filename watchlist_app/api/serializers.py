from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['id','active']

    # len_name = serializers.SerializerMethodField()
    #region Validations
    # #To Get by 'get_<columnName>'
    # def get_len_name(self,object):
    #     length = len(object.name)
    #     return length

    # # Validation
    # def validate(self,data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Desc should not be the same!")
    #     return data

    # # 'validate_<columnName>'
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     return value
    #endregion

# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):
    #region Model Serializer From other Fields
    # watchlist = WatchListSerializer(many=True, read_only=True) #Get all information
    # watchlist = serializers.StringRelatedField(many=True) #Follow what she named in Model(__str__)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-details' #Path name and adding 'context={'request':'request}' in Views 'StreamPlatformSerializer'
    # ) #Link to direct Detail
    #endregion

    class Meta:
        model = StreamPlatform
        fields = '__all__'

#region Sereializer
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# class MovieSerializer2(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     # Validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Desc should not be the same!")
#         return data

#     # 'validate_<columnName>'
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         return value
#endregion
