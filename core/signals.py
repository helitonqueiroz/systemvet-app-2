import logging
from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.middleware import get_current_user
from core.models import Log

# Configuração do logger
logger = logging.getLogger(__name__)

# Lista de modelos que devem ser ignorados pelos signals
IGNORED_MODELS = ['Log']

@receiver(post_save)
def log_post_save(sender, instance, created, **kwargs):
    # Logs para depuração
    logger.debug(f"Signal post_save acionado para o modelo: {sender.__name__}")

    # Ignora modelos específicos
    if sender.__name__ in IGNORED_MODELS:
        logger.debug(f"Ignorando signal post_save para o modelo: {sender.__name__}")
        return

    # Garante que a operação seja atômica
    with transaction.atomic():
        usuario = get_current_user()
        if usuario:
            logger.debug(f"Usuário recuperado nos signals: {usuario}")
            Log.objects.create(
                usuario=usuario,
                acao='CREATE' if created else 'UPDATE',
                modelo=sender.__name__,
                instancia_id=instance.id,
                detalhes=str(instance.__dict__)
            )
        else:
            logger.debug("Nenhum usuário recuperado nos signals.")

@receiver(post_delete)
def log_post_delete(sender, instance, **kwargs):
    # Logs para depuração
    logger.debug(f"Signal post_delete acionado para o modelo: {sender.__name__}")

    # Ignora modelos específicos
    if sender.__name__ in IGNORED_MODELS:
        logger.debug(f"Ignorando signal post_delete para o modelo: {sender.__name__}")
        return

    # Garante que a operação seja atômica
    with transaction.atomic():
        usuario = get_current_user()
        if usuario:
            logger.debug(f"Usuário recuperado nos signals: {usuario}")
            Log.objects.create(
                usuario=usuario,
                acao='DELETE',
                modelo=sender.__name__,
                instancia_id=instance.id,
                detalhes=str(instance.__dict__)
            )
        else:
            logger.debug("Nenhum usuário recuperado nos signals.")