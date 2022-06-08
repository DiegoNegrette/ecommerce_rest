from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_units/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicators/', IndicatorListAPIView.as_view(), name='indicator'),
    path('category_products/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_listcreate'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieveupdatedestroy'),
]
