from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expenses.views import CategoryViewSet, TransactionViewSet, BudgetViewSet, GoalViewSet
from ai.views import AIReportView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'goals', GoalViewSet, basename='goal')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/ai/report/", AIReportView.as_view(), name='ai-report'),
    path("api/", include(router.urls)),
]
