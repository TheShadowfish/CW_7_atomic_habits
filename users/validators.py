from rest_framework import serializers


class UsersValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value is None:
            raise serializers.ValidationError(
                    'У пользователя обязательно должен быть телеграм ID (для рассылки оповещений)')