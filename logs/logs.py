#!/usr/bin/env python3

'''Criando Logs

    Aplicando a biblioteca Logging para tratamento de erros com Logs.
'''
___version__ = "0.1.0"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import os
import logging
from logging import handlers

# TODO: USAR FUNÇÃO
# TODO: USAR LIB (LOGURU)

# variável de ambiente para definir o level logs
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# instância
log = logging.Logger("Jonatas", log_level)

# adicionando handler para criar arquivo de logs rotativo
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=10**6,
    backupCount=10
)

fh.setLevel(log_level)

# formatação da mensagem de log
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

fh.setFormatter(fmt)

log.addHandler(fh)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))