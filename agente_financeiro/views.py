
from django.shortcuts import render
from .services.agent_service import FinancialAgentService
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat(request):
    return render(request, 'agente_financeiro/chat.html')

@csrf_exempt
def enviar_mensagem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('mensagem')
        agent_service = FinancialAgentService()
        resposta = agent_service.query(texto)
        return JsonResponse({'resposta': resposta})
    return JsonResponse({'erro': 'Método não permitido'}, status=405)