  
from rest_framework import serializers
from .models import Office_facts



class OfficeFactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'fact_name', 'fact_body', 'season', 'episode','fact_post_date', 'fact_update_post')
        model = Office_facts
