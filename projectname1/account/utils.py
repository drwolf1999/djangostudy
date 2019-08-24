from .models import Account

class Util:
    @staticmethod
    def isValidLogin(form):
        userId = form.data['userId']
        password = form.data['password']

        if Account.objects.filter(userId=userId).count() == 0:
            return False
        user = Account.objects.get(userId=userId)
        if password == user.password:
            return True
        return False