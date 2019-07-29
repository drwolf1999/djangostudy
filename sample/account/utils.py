# 유틸리티
from .models import User


class Utils():

    @staticmethod
    def isValidLoginInformation(LoginInfo):
        userId = LoginInfo.data['userId']
        password = LoginInfo.data['password']
        print(userId, password)
        if User.objects.filter(userId=userId).count() == 0:
            return False
        user = User.objects.get(userId=userId)
        print(user)
        if user:
            if user.password == password:
                return True
        return False
