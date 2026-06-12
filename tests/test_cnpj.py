"""Testes unitários para o módulo de validação de CNPJ."""

import pytest

from validator.cnpj import format_cnpj, validate


class TestValidateCNPJ:
    """Testes de validação de CNPJ."""

    def test_cnpj_valido_com_formatacao(self):
        """CNPJ válido no formato XX.XXX.XXX/XXXX-XX deve retornar True."""
        assert validate("11.222.333/0001-81") is True

    def test_cnpj_valido_sem_formatacao(self):
        """CNPJ válido composto apenas de dígitos deve retornar True."""
        assert validate("11222333000181") is True

    def test_cnpj_invalido_primeiro_digito_verificador(self):
        """CNPJ com primeiro dígito verificador errado deve retornar False."""
        assert validate("11.222.333/0001-91") is False

    def test_cnpj_invalido_segundo_digito_verificador(self):
        """CNPJ com segundo dígito verificador errado deve retornar False."""
        assert validate("11.222.333/0001-82") is False

    def test_cnpj_todos_digitos_iguais_retorna_falso(self):
        """Qualquer CNPJ com todos os dígitos iguais é inválido pela Receita Federal."""
        for digit in "0123456789":
            assert validate(digit * 14) is False, f"CNPJ {digit * 14} deveria ser inválido"

    def test_cnpj_tamanho_menor_que_14(self):
        """CNPJ com menos de 14 dígitos deve retornar False."""
        assert validate("112223330001") is False

    def test_cnpj_tamanho_maior_que_14(self):
        """CNPJ com mais de 14 dígitos deve retornar False."""
        assert validate("1122233300018100") is False

    def test_cnpj_vazio_retorna_falso(self):
        """String vazia deve retornar False."""
        assert validate("") is False

    def test_cnpj_com_letras_retorna_falso(self):
        """CNPJ contendo letras deve retornar False após limpeza."""
        assert validate("ab.cde.fgh/ijkl-mn") is False

    def test_cnpj_outro_valido(self):
        """Segundo CNPJ válido para garantir cobertura de casos distintos."""
        # CNPJ da Caixa Econômica Federal
        assert validate("00.360.305/0001-04") is True


class TestFormatCNPJ:
    """Testes de formatação de CNPJ."""

    def test_formatar_cnpj_so_digitos(self):
        """CNPJ válido sem formatação deve ser retornado no formato correto."""
        assert format_cnpj("11222333000181") == "11.222.333/0001-81"

    def test_formatar_cnpj_ja_formatado(self):
        """CNPJ já formatado deve permanecer inalterado após a formatação."""
        assert format_cnpj("11.222.333/0001-81") == "11.222.333/0001-81"

    def test_formatar_cnpj_invalido_levanta_value_error(self):
        """Formatar um CNPJ inválido deve levantar ValueError."""
        with pytest.raises(ValueError, match="CNPJ inválido"):
            format_cnpj("00000000000000")

    def test_formato_resultado_correto(self):
        """O resultado deve seguir o padrão XX.XXX.XXX/XXXX-XX."""
        resultado = format_cnpj("11222333000181")
        assert len(resultado) == 18
        assert resultado[2] == "."
        assert resultado[6] == "."
        assert resultado[10] == "/"
        assert resultado[15] == "-"
