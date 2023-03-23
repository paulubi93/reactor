import logging 
logger = logging.getLogger(__name__)
logger.propagate = False # para no propagar este nuevo logger al logger base, es decir, 
# en nuestro archivo de trabajo, no obtendremos el mensaje: 
# 03/20/2023 14:54:48-helper-INFO-hello from demo
#de manera directa 
logger.info ('hello from demo')

