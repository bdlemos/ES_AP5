"""Módulo para validação e formatação de CPF."""

import re


def _clean(cpf: str) -> str:
    """Remove caracteres não numéricos do CPF."""
    return re.sub(r"\D", "", cpf)


def validate(cpf: str) -> bool:
    """
    Valida um CPF.

    O algoritmo verifica:
    - Comprimento de 11 dígitos
    - Se todos os dígitos são iguais (inválido por definição)
    - Dígitos verificadores usando o algoritmo oficial da Receita Federal

    Args:
        cpf: String com o CPF (formatado como XXX.XXX.XXX-XX ou só dígitos).

    Returns:
        True se o CPF for válido, False caso contrário.

    Examples:
        >>> validate("529.982.247-25")
        True
        >>> validate("000.000.000-00")
        False
    """
    cpf = _clean(cpf)

    if len(cpf) != 11:
        return False

    # CPFs com todos os dígitos iguais são inválidos
    if cpf == cpf[0] * 11:
        return False

    # Primeiro dígito verificador
    total = sum(int(cpf[i]) * (10 - i) for i in range(9))
    remainder = total % 11
    first_digit = 0 if remainder < 2 else 11 - remainder

    if int(cpf[9]) != first_digit:
        return False

    # Segundo dígito verificador
    total = sum(int(cpf[i]) * (11 - i) for i in range(10))
    remainder = total % 11
    second_digit = 0 if remainder < 2 else 11 - remainder

    return int(cpf[10]) == second_digit


def format_cpf(cpf: str) -> str:
    """
    Formata um CPF para o padrão XXX.XXX.XXX-XX.

    Args:
        cpf: String com o CPF (apenas dígitos ou já formatado).

    Returns:
        CPF no formato XXX.XXX.XXX-XX.

    Raises:
        ValueError: Se o CPF fornecido não for válido.

    Examples:
        >>> format_cpf("52998224725")
        '529.982.247-25'
    """
    cpf = _clean(cpf)
    if not validate(cpf):
        raise ValueError(f"CPF inválido: {cpf}")
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
