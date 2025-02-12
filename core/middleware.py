import threading
import logging

# Configuração do logger
logger = logging.getLogger(__name__)

# Objeto thread-local para armazenar informações específicas de cada requisição
_thread_locals = threading.local()

class GlobalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lógica específica para o app 'clientes'
        if hasattr(request, 'user') and request.user.is_authenticated:
            _thread_locals.usuario = request.user
            logger.debug(f"Usuário autenticado armazenado: {_thread_locals.usuario}")
        else:
            _thread_locals.usuario = None
            logger.debug("Nenhum usuário autenticado.")

        # Lógica específica para o app 'pets'
        if hasattr(request, 'pet_id'):
            from pets.models import Pet  # Import local para evitar circular imports
            _thread_locals.pet = Pet.objects.filter(id=request.pet_id).first()
            logger.debug(f"Pet armazenado: {_thread_locals.pet}")
        else:
            _thread_locals.pet = None
            logger.debug("Nenhum pet encontrado na requisição.")

        # Lógica específica para o app 'financeiro'
        if hasattr(request, 'transacao_id'):
            from financeiro.models import Transacao  # Import local para evitar circular imports
            _thread_locals.transacao = Transacao.objects.filter(id=request.transacao_id).first()
            logger.debug(f"Transação armazenada: {_thread_locals.transacao}")
        else:
            _thread_locals.transacao = None
            logger.debug("Nenhuma transação encontrada na requisição.")

        # Continua o processamento da requisição
        response = self.get_response(request)
        return response

# Métodos para recuperar informações do thread-local
def get_current_user():
    user = getattr(_thread_locals, 'usuario', None)
    logger.debug(f"Usuário recuperado do thread-local: {user}")
    return user

def get_current_pet():
    pet = getattr(_thread_locals, 'pet', None)
    logger.debug(f"Pet recuperado do thread-local: {pet}")
    return pet

def get_current_transacao():
    transacao = getattr(_thread_locals, 'transacao', None)
    logger.debug(f"Transação recuperada do thread-local: {transacao}")
    return transacao