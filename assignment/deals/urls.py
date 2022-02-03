from django.urls import path, include

from rest_framework.routers import DefaultRouter
from deals import views

router = DefaultRouter()
router.register(r'deals', views.DealViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('claim/<int:deal_id>/', views.claim_deal, name='clain-deal'),
]
