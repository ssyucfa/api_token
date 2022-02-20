from django.urls import path

from tokens.views import TokenView

urlpatterns = [
    path('get-information-from-token/', TokenView.as_view())
]
