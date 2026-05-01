---
project: <project-slug>
date: YYYY-MM-DD
doc_status: draft
doc_type: project-readme
project_status: draft
n8n_namespace: "<Project Name>"
---

# <Project Name>

## Бизнес-ценность

<Что проект делает, для кого и зачем существует.>

<Как проект достигает результата: какие источники, фильтры, нормализация, анализ или storage участвуют в ценностной цепочке.>

## Карта проекта

### As Is

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "10px"
  }
}}%%
flowchart LR
    A["Current<br/>Flow"] --> B["Current<br/>Output"]
```

### To Be

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "10px"
  }
}}%%
flowchart LR
    A["Source"] --> B["Engine"] --> C["Analysis"]
```

## Flow-паспорта

| Layer | Type | Flow | Passport |
| ----- | ---- | ---- | -------- |
| Source | workflow | <Exact n8n flow name> | [`<flow-slug>`](./flow-docs/<flow-slug>.md) |

## Contracts

- `<Boundary>`: <короткий контракт между слоями или workflow>.

## Open Questions

1. <Вопрос, который влияет на следующий инженерный шаг.>

