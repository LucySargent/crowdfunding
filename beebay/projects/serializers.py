from rest_framework import serializers
from .models import Project, Pledge, Beefriend, SUB_CHOICES

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project_id = serializers.IntegerField()

    # this will be called for POST /pledges to create a new pledge
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    suburbs = serializers.ChoiceField(choices=SUB_CHOICES)
    beehives = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    min_required = serializers.IntegerField(default=300)
    goal = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
 
# leaving the pledges out of list view so that we don't have to get 
# all of the pledges and all of the projects in one go
# pledges = PledgeSerializer(many=True, read_only=True)

# this will be called for POST /projects to create a new project
    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class BeefriendSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    comment = serializers.CharField(max_length=200)
    # supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    beefriend = serializers.ReadOnlyField(source='beefriend.id')
    

    # this will be called for POST /beefriend to create a new beefriend
    def create(self, validated_data):
        return Beefriend.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
# many=True tells the nested serializer to include a list of items
# read_only=True means it's only used for GET, not PUT (which means you don't/can't 
# provide pledges when updating a project)
    pledges = PledgeSerializer(many=True, read_only=True)
    adoptions = BeefriendSerializer(many=True, read_only=True)
   
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.beehives = validated_data.get('beehives', instance.beehives)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount',instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.save()
        return instance

class BeefriendDetailSerializer(BeefriendSerializer):
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment',instance.comment)
        instance.save()
        return instance

