---
project: job-searcher
date: 2026-04-29
doc_status: draft
doc_type: flow-doc
flow_layer: Filter
flow_type: subflow
flow_name: "Job Searcher / Filter / Role Cluster Filter"
---

## 1. Назначение

Subflow формирует или применяет role/title критерии для отбора вакансий.

## 2. Steps

TBD после сверки с текущим canvas n8n.

## 3. Contracts

### 3.1. Входной

TBD.

### 3.2. Выходной

TBD: критерии role/title для source-flow.

## 4. Skeleton

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "10px"
  }
}}%%
flowchart LR
    A["Input"] --> B["Role<br/>Cluster<br/>Filter"] --> C["Filter<br/>Criteria"]
```

