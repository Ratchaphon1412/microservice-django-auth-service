from rest_framework import serializers
from django.contrib.auth import password_validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from Infrastructure.kafka.producer import sendData
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)
        
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name',)
        
class UserProfilesSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    user_permissions = PermissionSerializer(many=True,read_only=True)
    
    class Meta :
        model = UserProfiles
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'password':{'write_only':True},
            'last_login':{'write_only':True},
            
        }
        
      
    def validate(self, attrs):
        # password
        password = attrs.get('password','')
        errors = dict()
        try:
            password_validation.validate_password(password=password)
        except password_validation.ValidationError as e:
            errors['password'] = list(e.messages)
        
        
        
        if errors:
            raise serializers.ValidationError(errors)
        
        
        return super(UserProfilesSerializer,self).validate(attrs)
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
       
        

        user.save()
        
        # Create user group if it doesn't exist
        group, created = Group.objects.get_or_create(name='user')
        
        if created:
            
            change_userprofiles = Permission.objects.get(codename='change_userprofiles')
            delete_userprofiles = Permission.objects.get(codename='delete_userprofiles')
            view_userprofiles = Permission.objects.get(codename='view_userprofiles')
            add_userprofiles = Permission.objects.get(codename='add_userprofiles')
            add_address = Permission.objects.get(codename='add_address')
            change_address = Permission.objects.get(codename='change_address')
            delete_address = Permission.objects.get(codename='delete_address')
            view_address = Permission.objects.get(codename='view_address')
            
            group.permissions.set([change_userprofiles,delete_userprofiles,view_userprofiles,add_userprofiles,add_address,change_address,delete_address,view_address])
            user.groups.add(created)
            
        user.groups.add(group)
        print(group.permissions.all())
        for permission in group.permissions.all():
            user.user_permissions.add(permission)
        
        # sendData('create_user',str(user.id))
        
        return user
    
    def update(self, instance, validated_data):
        
        password = validated_data.pop('password',None)
        
        if password is not None:
            instance.set_password(password)
        
           
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return instance.delete()

    
    

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        return token
    
    def validate(self,attrs):
      
        
       
        user = UserProfiles.objects.filter(email=attrs.get('email','')).first()
        print(user)
        
        if user is None:
            raise serializers.ValidationError("User not found.")
        
        if not user.is_active:
            raise serializers.ValidationError("User is not active.")
        
        if not user.is_email_verified:
            raise serializers.ValidationError("User is not verified.")
        
        data = super(LoginSerializer,self).validate(attrs)
        
        return data

class ReSendEmailVerifySerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        
        def validate_email(self,value):
            try:
                user = UserProfiles.objects.filter(email=value).first()
            except Exception as e:
                user = None
            
            if user is None:
                raise serializers.ValidationError("User not found.")
            
            if user.is_email_verified:
                raise serializers.ValidationError("User is already verified.")
            
            return value
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id','fullname','phone','detail_address','country','province','zip_code']
        read_only_fields = ['address_id']
        extra_kwargs = {
            'user':{'write_only':True},
            
        }
        
    def validate(self, attrs):
        
        
        return super(AddressSerializer,self).validate(attrs)
        
        
    def create(self,validated_data):
        
        address = self.Meta.model(**validated_data)
        address.save()
        return address
    
    def update(self, instance, validated_data):
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        
        return super().update(instance, validated_data)
    
            

    