# Sistema de Atendimento e Análise

Sistema completo de gerenciamento de atendimentos com fila, histórico e relatórios.

## Requisitos
- Python 3.10+
- tkinter (já incluso no Python padrão)

## Como executar
```bash
python main.py
```

## Estrutura
- `models/` — Classes de domínio (Cliente, Atendente, Atendimento)
- `structures/` — Estruturas de dados (fila, pilha, lista encadeada, vetor)
- `business/` — Regras de negócio
- `reports/` — Relatórios, ordenação e exportação
- `gui/` — Interface gráfica tkinter
- `data/` — Persistência em JSON
- `tests/` — Testes unitários