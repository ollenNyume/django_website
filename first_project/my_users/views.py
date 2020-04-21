from django.shortcuts import render

# Create your views here.


def my_users_dis(request):

    return render(request, 'my_users/my_users.html')
