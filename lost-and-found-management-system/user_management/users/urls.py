from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, CreateAdminUserView, AssignRoleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('<str:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('create-admin/', CreateAdminUserView.as_view(), name='create-admin'),
    path('assign-role/', AssignRoleView.as_view(), name='assign-role'),  
]
