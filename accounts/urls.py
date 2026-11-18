



from django.urls import path


from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import StudentProfileGetView
from accounts.views import StudentProfileUpdateView


urlpatterns = [
                # route to admin create
                path("admin/register/",AdminCreateView.as_view()),


                # route to student create
                path("student/register/",StudentCreateView.as_view()),

                path("student/profile/get/me/",StudentProfileGetView.as_view()),
                path("student/profile/complete/",StudentProfileUpdateView.as_view()),

                

]