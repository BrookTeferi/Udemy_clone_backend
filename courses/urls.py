from django.urls import path
from rest_framework import routers
from courses.views import CourseStudy, GetCartDetail, AddComment, CoursesHomeView, CourseDetail,SectorCourse,SearchCourse





# router=routers.SimpleRouter()
# router.register(r'courses',CoursesHomeView )
# urlpatterns = router.urls

urlpatterns=[
    path('detail/<uuid:course_uuid>/', CourseDetail.as_view()),
    path('search/<str:search_term>/', SearchCourse.as_view()),
    path('cart/', GetCartDetail.as_view()),
    path('comment/<course_uuid>',AddComment.as_view()),
    path('study/<uuid:course_uuid>/', CourseStudy.as_view()),
    path('<uuid:sector_uuid>/', SectorCourse.as_view()),
    path('',CoursesHomeView.as_view())

]
