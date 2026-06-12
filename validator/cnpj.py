"""Módulo para validação e formatação de CNPJ."""

import re


def _clean(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"\D", "", cnpj)


def validate(cnpj: str) -> bool:
    """
    Valida um CNPJ.

    O algoritmo verifica:
    - Comprimento de 14 dígitos
    - Se todos os dígitos são iguais (inválido por definição)
    - Dígitos verificadores usando o algoritmo oficial da Receita Federal

    Args:
        cnpj: String com o CNPJ (formatado como XX.XXX.XXX/XXXX-XX ou só dígitos).

    Returns:
        True se o CNPJ for válido, False caso contrário.

    Examples:
        >>> validate("11.222.333/0001-81")
        True
        >>> validate("00.000.000/0000-00")
        False
    """
    cnpj = _clean(cnpj)

    if len(cnpj) != 14:
        return False

    # CNPJs com todos os dígitos iguais são inválidos
    if cnpj == cnpj[0] * 14:
        return False

    # Primeiro dígito verificador
    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(cnpj[i]) * weights1[i] for i in range(12))
    remainder = total % 11
    first_digit = 0 if remainder < 2 else 11 - remainder

    if int(cnpj[12]) != first_digit:
        return False

    # Segundo dígito verificador
    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    total = sum(int(cnpj[i]) * weights2[i] for i in range(13))
    remainder = total % 11
    second_digit = 0 if remainder < 2 else 11 - remainder

    return int(cnpj[13]) == second_digit


def format_cnpj(cnpj: str) -> str:
    """
    Formata um CNPJ para o padrão XX.XXX.XXX/XXXX-XX.

    Args:
        cnpj: String com o CNPJ (apenas dígitos ou já formatado).

    Returns:
        CNPJ no formato XX.XXX.XXX/XXXX-XX.

    Raises:
        ValueError: Se o CNPJ fornecido não for válido.

    Examples:
        >>> format_cnpj("11222333000181")
        '11.222.333/0001-81'
    """
    cnpj = _clean(cnpj)
    if not validate(cnpj):
        raise ValueError(f"CNPJ inválido: {cnpj}")
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
