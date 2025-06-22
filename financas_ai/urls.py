from django.contrib import admin
from django.urls import path
from agente_financeiro import views  # Corrigido - import do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat, name='chat'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]