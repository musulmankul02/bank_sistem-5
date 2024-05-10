from rest_framework import serializers
import re, random, string

from apps.users.models import User
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'age', 'email','phone', 'balance','created_at', 'password', 'password_confirm', 'wallet_address')
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True},
            'wallet_address': {'read_only': True},
            'balance': {'read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError("Пароли не совпадают!")

        wallet_address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        validated_data['wallet_address'] = wallet_address

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


    
    def validate_phone(self, value):
        if not re.match(r'^\+996\d{9}$', value):
            raise serializers.ValidationError("""Неверный формат номера телефона! Введите телефонный номер формате(+996...)""")
        return value
    
    def validate(self, attrs):
        attrs = super().validate(attrs) 
        phone = attrs.get('phone')
        if phone:
            self.validate_phone(phone)
        return attrs