from .views import BlockedDateViewSet,BookingsViewSet
from django.urls import path,include
from rest_frawework.routers import DefaultRouter


router = DefaultRouter()
router.register('blokdate',BlockedDateViewSet)
router.register('booking',BookingsViewSet)


urlpatterns = [
    path('',include(router.urls))
]
