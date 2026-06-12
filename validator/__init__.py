"""Pacote de validação de documentos brasileiros (CPF e CNPJ)."""

from .cpf import format_cpf
from .cpf import validate as validate_cpf
from .cnpj import format_cnpj
from .cnpj import validate as validate_cnpj

__all__ = ["validate_cpf", "format_cpf", "validate_cnpj", "format_cnpj"]
__version__ = "1.0.0"
