from django.contrib.auth.models import User

user = User.objects.create_user('cleider', 'cleider@gmail.com', 'cleider')

user.firs_name = 'Cleider'
user.last_name = 'Araujo'
user.save()
