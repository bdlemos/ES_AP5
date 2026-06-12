# GitHub Actions — Validador de CPF/CNPJ

## Objetivo

Explorar o uso do [GitHub Actions](https://docs.github.com/en/actions) para teste em múltiplos sistemas operacionais e versões de linguagens de programação.

## Descrição

1. **Criar programa com testes no GitHub:** Crie um repositório no GitHub. Implemente um pequeno programa (na linguagem de sua escolha) e escreva pelo menos 5 testes de unidade.

2. **Executar os testes no GitHub Actions**: Configure a ferramenta de CI/CD GitHub Actions executar os testes automaticamente a cada commit. No GitHub, você encontra exemplos sobre como utilizar o GitHub Actions em linguagens (https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing).

3. **Executar Actions nos sistemas operacionais Ubuntu, MacOS e Windows**: Configure o seu workflow do GitHub Actions para dar o build e testar o programa em três sistemas operacionais: Ubuntu, MacOS e Windows.

4. **Executar Actions em pelo menos duas versões da linguagem de programação**: Configure o seu workflow do GitHub Actions para dar o build testar o programa em pelo menos duas versões da linguagem escolhida.

## Submissão

Submeter no Moodle o link do último build com sucesso do GitHub Actions.
Por exemplo: https://github.com/Textualize/rich/actions/runs/18370672554

---

## Projeto: Validador de CPF/CNPJ

Biblioteca Python para validação e formatação de documentos brasileiros (CPF e CNPJ) implementando o algoritmo oficial da Receita Federal.

### Estrutura do Projeto

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline CI/CD GitHub Actions
├── validator/
│   ├── __init__.py         # API pública do pacote
│   ├── cpf.py              # Validação e formatação de CPF
│   └── cnpj.py             # Validação e formatação de CNPJ
├── tests/
│   ├── __init__.py
│   ├── test_cpf.py         # Testes unitários — CPF
│   └── test_cnpj.py        # Testes unitários — CNPJ
├── pyproject.toml
├── requirements.txt
└── README.MD
```

### Como executar localmente

```bash
# Instalar dependências
pip install -r requirements.txt
pip install -e .

# Rodar os testes
pytest

# Rodar com cobertura
pytest --cov=validator --cov-report=term-missing
```

### CI/CD — GitHub Actions

O workflow `.github/workflows/ci.yml` executa os testes em **matriz** de:

| Sistema Operacional | Versões Python |
|---|---|
| Ubuntu | 3.10, 3.12 |
| macOS | 3.10, 3.12 |
| Windows | 3.10, 3.12 |

**Total: 6 execuções paralelas a cada push.**