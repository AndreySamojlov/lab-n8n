---
project: wildberries
date: 2026-05-02
doc_status: current
doc_type: flow-doc
flow_layer: Engine
flow_type: workflow
flow_name: WB Атрибуты новых страниц
n8n_id: K2b7NpHHLXbr9FDz
---

## 1. Назначение

`WB Атрибуты новых страниц` - subflow для новых листов. Он достраивает заголовки по данным карточки Wildberries и отправляет Telegram-пинг о завершении.

## 2. Steps

#### Node: `Start`
`n8n-nodes-base.executeWorkflowTrigger`

Принимает `sheetName` и `chatId` из source-flow.

#### Node: `Только новые листы`
`n8n-nodes-base.filter`

Пропускает только `resolution = new`.

#### Node: `Читать строку A2 нового листа`
`n8n-nodes-base.httpRequest`

Читает seed-строку листа.

#### Node: `Извлечь SKU и ссылки`
`n8n-nodes-base.code`

Формирует items для первой карточки из строки.

#### Node: `Построить URL card.json`
`n8n-nodes-base.code`

Собирает `cardJsonUrl` по SKU и basket.

#### Node: `Загрузить card.json (новый лист)`
`n8n-nodes-base.httpRequest`

Загружает публичный `card.json`.

#### Node: `Собрать заголовки из карточки`
`n8n-nodes-base.code`

Формирует итоговый список заголовков.

#### Node: `Записать заголовки в лист`
`n8n-nodes-base.httpRequest`

Обновляет первую строку нового листа.

#### Node: `TG Headers Done Payload`
`n8n-nodes-base.code`

Готовит Telegram payload с `chatId`.

#### Node: `TG Headers Done`
`n8n-nodes-base.telegram`

Отправляет сообщение:

`✅ <b>WB Flow</b>: заголовки новых страниц обновлены`

## 3. Contracts

### 3.1. Input

```json
{
  "sheetName": "Косметички",
  "chatId": "272425172"
}
```

### 3.2. Output

Subflow не возвращает пользовательский payload. Он обновляет Google Sheets и завершает run Telegram completion ping.

## 4. Skeleton

```mermaid
flowchart LR
  A["Start"] --> B["Только новые листы"]
  B --> C["Loop Over Items"]
  C --> D["Читать строку A2 нового листа"]
  D --> E["Извлечь SKU и ссылки"]
  E --> F["Построить URL card.json"]
  F --> G["Загрузить card.json (новый лист)"]
  G --> H["Собрать заголовки из карточки"]
  H --> I["Записать заголовки в лист"]
  C --> J["TG Headers Done Payload"]
  J --> K["TG Headers Done"]
```
