from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    #path('', views.get_accounts, name='get_accounts'),
    #path('<int:id>', views.get_account_detail, name='get_account_detail'),
    #path('login', views.user_login, name='user_login'),
    ############
    # 以下是正式api
    ############
    path('register', views.register, name='register'),
    path('changeinfo', views.user_changeinfo, name='user_changeinfo'),
    path('scope1', views.Scope1upload, name='Scope1upload'),
    path('scope2', views.Scope2upload, name='Scope2upload'),
    path('scope3', views.Scope3upload, name='Scope3upload'),
    path('offset', views.offsetupload, name='offsetupload'),
    #path('getemissioninfo', views.get_emission_info, name='get_emission_info'),
    path('getmassage',views.get_massage,name='get_massage'),
    path('getinfoall',views.get_info_all,name='get_info_all'),
    path('getenterpriseinfo',views.get_enterprise_info,name='get_enterprise_info'),
    path('getenterprisereport',views.get_enterprise_report,name='get_enterprise_report'),
    path('gethistory',views.get_history,name='get_history'),
    ####
    path('token/', views.roleTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]