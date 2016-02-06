from django.conf.urls import url, include
from rest_framework import routers
from puzzle import views

router = routers.DefaultRouter()
router.register(r'puzzles', views.PuzzleViewSet)
router.register(r'solutions', views.SolutionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
