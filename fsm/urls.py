from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.pageview import *
from .views.fsmview import *
from .views.fsmstateview import *
from .views.fsmedgeview import *
from .views.abilityview import *
from .views.widgetview import *
from .views.problemsmallanswerview import *

router = DefaultRouter()
router.register('page', FSMPageView)
router.register('page/<int:pk>', FSMPageView)
router.register('fsm', FSMView)
router.register('fsm/<int:pk>', FSMView)
router.register('state', FSMStateView)
router.register('state/<int:pk>', FSMStateView)
router.register('edge', FSMEdgeView)
router.register('edge/<int:pk>', FSMEdgeView)
router.register('ability', AbilityView)
router.register('ability/<int:pk>', AbilityView)
router.register('widget', WidgetView)
router.register('widget/<int:pk>', WidgetView)
router.register('small', SmallView)
router.register('small/<int:pk>', SmallView)
urlpatterns = [
]

urlpatterns += router.urls