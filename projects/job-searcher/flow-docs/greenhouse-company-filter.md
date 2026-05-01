---
project: job-searcher
date: 2026-04-29
doc_status: draft
doc_type: flow-doc
flow_layer: Filter
flow_type: subflow
flow_name: "Job Searcher / Filter / Greenhouse Company Filter"
---

## 1. Назначение

Subflow готовит company/token критерии для Greenhouse-источников.

## 2. Steps

TBD после сверки с текущим canvas n8n.

## 3. Contracts

### 3.1. Входной

TBD.

### 3.2. Выходной

TBD: список Greenhouse company/token критериев для source-flow.

## 4. Skeleton

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "10px"
  }
}}%%
flowchart LR
    A["Input"] --> B["Greenhouse<br/>Company<br/>Filter"] --> C["Company<br/>Criteria"]
```

