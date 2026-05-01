---
project: job-searcher
date: 2026-04-29
doc_status: draft
doc_type: flow-doc
flow_layer: Source
flow_type: workflow
flow_name: "Job Searcher / 01 Sources / Greenhouse Orchestrate Registry"
---

## 1. Назначение

Workflow обходит Greenhouse registry/company tokens и получает вакансии из Greenhouse-источников.

## 2. Steps

TBD после сверки с текущим canvas n8n.

## 3. Contracts

### 3.1. Входной

TBD: company/token критерии.

### 3.2. Выходной

TBD: source-level вакансии Greenhouse для будущего `Engine`.

## 4. Skeleton

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "10px"
  }
}}%%
flowchart LR
    A["Trigger"] --> B["Greenhouse<br/>Registry"] --> C["Source<br/>Output"]
```

