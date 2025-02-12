from django.shortcuts import render
from clientes.models import ClienteSoftware
from pets.models import Pet, Consulta
from financeiro.models import Cobranca

def dashboard(request):
    # Dados para o dashboard
    total_clientes = ClienteSoftware.objects.count()
    total_pets = Pet.objects.count()
    total_consultas = Consulta.objects.count()
    cobrancas_pendentes = Cobranca.objects.filter(status='Pendente')

    context = {
        'total_clientes': total_clientes,
        'total_pets': total_pets,
        'total_consultas': total_consultas,
        'cobrancas_pendentes': cobrancas_pendentes,
    }
    return render(request, 'core/dashboard.html', context)
