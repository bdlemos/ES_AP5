"""Testes unitários para o módulo de validação de CPF."""

import pytest

from validator.cpf import format_cpf, validate


class TestValidateCPF:
    """Testes de validação de CPF."""

    def test_cpf_valido_com_formatacao(self):
        """CPF válido no formato XXX.XXX.XXX-XX deve retornar True."""
        assert validate("529.982.247-25") is True

    def test_cpf_valido_sem_formatacao(self):
        """CPF válido composto apenas de dígitos deve retornar True."""
        assert validate("52998224725") is True

    def test_cpf_invalido_primeiro_digito_verificador(self):
        """CPF com primeiro dígito verificador errado deve retornar False."""
        assert validate("529.982.247-35") is False

    def test_cpf_invalido_segundo_digito_verificador(self):
        """CPF com segundo dígito verificador errado deve retornar False."""
        assert validate("529.982.247-24") is False

    def test_cpf_todos_digitos_iguais_retorna_falso(self):
        """Qualquer CPF com todos os dígitos iguais é inválido pela Receita Federal."""
        for digit in "0123456789":
            assert validate(digit * 11) is False, f"CPF {digit * 11} deveria ser inválido"

    def test_cpf_tamanho_menor_que_11(self):
        """CPF com menos de 11 dígitos deve retornar False."""
        assert validate("123456789") is False

    def test_cpf_tamanho_maior_que_11(self):
        """CPF com mais de 11 dígitos deve retornar False."""
        assert validate("123456789012") is False

    def test_cpf_vazio_retorna_falso(self):
        """String vazia deve retornar False."""
        assert validate("") is False

    def test_cpf_com_letras_retorna_falso(self):
        """CPF contendo letras deve retornar False após limpeza."""
        assert validate("abc.def.ghi-jk") is False

    def test_cpf_outro_valido(self):
        """Segundo CPF válido para garantir cobertura de casos distintos."""
        assert validate("111.444.777-35") is True


class TestFormatCPF:
    """Testes de formatação de CPF."""

    def test_formatar_cpf_so_digitos(self):
        """CPF válido sem formatação deve ser retornado no formato correto."""
        assert format_cpf("52998224725") == "529.982.247-25"

    def test_formatar_cpf_ja_formatado(self):
        """CPF já formatado deve permanecer inalterado após a formatação."""
        assert format_cpf("529.982.247-25") == "529.982.247-25"

    def test_formatar_cpf_invalido_levanta_value_error(self):
        """Formatar um CPF inválido deve levantar ValueError."""
        with pytest.raises(ValueError, match="CPF inválido"):
            format_cpf("00000000000")

    def test_formato_resultado_correto(self):
        """O resultado deve seguir o padrão XXX.XXX.XXX-XX."""
        resultado = format_cpf("11144477735")
        assert len(resultado) == 14
        assert resultado[3] == "."
        assert resultado[7] == "."
        assert resultado[11] == "-"
