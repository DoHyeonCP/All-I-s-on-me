from forcast.models import ImageFile
from rest_framework import serializers

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(user_url = True)
    
    class meta:
        model = ImageFile
        fields = ('file_name', 'image')