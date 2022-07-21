from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Link',views.Linkviewset)
router.register('Comment',views.Commentviewset)

urlpatterns=[
    
    ]
urlpatterns=urlpatterns+router.urls