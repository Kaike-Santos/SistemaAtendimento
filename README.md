# Sistema de Atendimento e Análise

Sistema completo de gerenciamento de atendimentos para clínicas e centrais de atendimento, desenvolvido como projeto acadêmico.

## Requisitos
- Python 3.10+
- tkinter (já incluído no Python padrão)

## Como executar
```bash
python main.py
```

## Estrutura de pastas
```
sistema-atendimento/
├── models/        # Classes de domínio
├── structures/    # Estruturas de dados
├── business/      # Regras de negócio
├── reports/       # Relatórios e exportação
├── gui/           # Interface gráfica tkinter
├── data/          # Persistência JSON
└── tests/         # Testes unitários
```

## Estruturas usadas e justificativa Big-O

| Estrutura | Uso | Inserção | Busca | Remoção |
|---|---|---|---|---|
| Vetor ordenado | Busca rápida de cliente por ID | O(n) | O(log n) | O(n) |
| Fila FIFO | Atendimentos normais | O(1) | — | O(1) |
| Fila de prioridade | Atendimentos urgentes na frente | O(1) | — | O(n) |
| Pilha LIFO | Desfazer última finalização | O(1) | — | O(1) |
| Lista encadeada | Clientes ativos com remoção eficiente | O(1) | O(n) | O(n) |
| Merge sort | Ordenar relatórios por duração | — | — | O(n log n) |
| Quick sort | Ranking top 5 clientes | — | — | O(n log n) médio |
| Busca recursiva | Histórico por cliente | O(n) | — | — |

## Testes
```bash
python -m unittest discover tests
```

## Integrantes
- Kaike Machado 
- Henrique Silva 
- Gabriel dos Anjos 
- Maria Eduarda Gobira
- João Nelson
- Esther Mendonça
