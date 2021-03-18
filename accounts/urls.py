from django.urls import path, re_path

# from .views import signup
# ,login, logout, send_request, verify, activate,

# urlpatterns = [
#     # path('request/', send_request, name='request'),
#     # path('verify/', verify, name='verify'),
#     path('signup/', signup, name="signup"),
#     # path('logout/', logout, name="logout"),
#     # path('login/', login, name="login"),
#     #re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
#             # activate, name='activate')
# ]

from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPair, Signup, activate, ChangePass, LogOut, UploadAnswerView, \
    PayView, VerifyPayView, UserInfo, TeamInfo, Teams, SendVerifyCode, GetTeamData, ChangePassword, \
    RegistrationInfo, VerifyDiscount

urlpatterns = [
    path('pay/', PayView.as_view(), name="pay"),
    path('pay/verify-payment/', VerifyPayView.as_view(), name="verify-payment"),
    # path('groupSignup/', GroupSignup.as_view(), name="group_signup"),
    path('signup/', Signup.as_view(), name="signup"),
    path('sendVerify/', SendVerifyCode.as_view(), name="send_verify_code"),
    path('teamdata/', GetTeamData.as_view(), name="get_team_data"),
    # path('changePass/', ChangePass.as_view(), name="change_password"),
    path('logout/', LogOut.as_view(), name="logout"),
    path('changepass/', ChangePassword.as_view(), name='change_password'),
    path('token/obtain/', ObtainTokenPair.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('answerFile/', UploadAnswerView.as_view()),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            activate, name='activate'),
    path('userInfo/', UserInfo.as_view(), name="user_info"),
    path('teamInfo/', TeamInfo.as_view(), name="team_info"),
    path('teams/', Teams.as_view(), name="teams"),
    path('registration-info/', RegistrationInfo.as_view(), name="registration_info"),
    path('verify-discount/', VerifyDiscount.as_view(), name="verify_discount"),
]
