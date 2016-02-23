from django.conf.urls import url, include
from rest_framework import routers
from puzzle import views

router = routers.DefaultRouter()
router.register(r'solutions', views.SolutionViewSet)
router.register(r'pieces', views.PieceViewSet)

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^puzzles/(?P<puzzle_id>[0-9]+)$', views.PuzzleView.as_view(), name='Puzzles'),
    url(r'^puzzles/', views.PuzzleView.as_view(), name='Puzzles'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
