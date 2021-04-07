from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail, GenericAPIView, ArticleViewSet, ArticleModelViewSet, ArticleGenericViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('modelarticle', ArticleModelViewSet, basename='modelarticle')
router.register('genericarticle', ArticleGenericViewSet, basename='genericarticle')



urlpatterns = [

    path('genericviewset/', include(router.urls)),
    path('genericviewset/<int:pk>', include(router.urls)),
    path('modelviewset/', include(router.urls)),
    path('modelviewset/<int:pk>', include(router.urls)),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
]