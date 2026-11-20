



from django.urls import path


from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import StudentProfileGetView
from accounts.views import StudentProfileUpdateView

from accounts.views import TrainerCreateView
from accounts.views import TrainerProfileGetView
from accounts.views import TrainerProfileUpdateView

from  rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
                # route to admin create
                path("admin/register/",AdminCreateView.as_view()),


                # route to student create
                path("student/register/",StudentCreateView.as_view()),

                path("student/profile/get/me/",StudentProfileGetView.as_view()),
                path("student/profile/complete/",StudentProfileUpdateView.as_view()),


                # route to trainer create
                path("trainer/register/",TrainerCreateView.as_view()), 

                path("trainer/profile/get/me/",TrainerProfileGetView.as_view()),
                path("trainer/profile/complete/",TrainerProfileUpdateView.as_view()),             


                # Token authentication
                path("token/generation/",ObtainAuthToken.as_view())
                

]