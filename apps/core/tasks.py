from celery.utils.log import get_task_logger

from webScrapingProdutos.celery import app
from apps.core.utils.atualiza_produtos import atualizar_produtos


logger = get_task_logger(__name__)


@app.task(name='atualiza_produtos', queue='produtos')
def task_atualizar_produtos():
    logger.info("Iniciando atualização de tarefas")
    atualizar_produtos()
    logger.info("Finalizando atualização de tarefas")
