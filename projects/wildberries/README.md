---
project: wildberries
date: 2026-05-02
doc_status: current
doc_type: project-readme
project_status: active
n8n_namespace: "Wildberries"
---

# Wildberries

Автоматизация ведения товарного справочника в Google Sheets на основе данных Wildberries. Система отслеживает новые листы (SKU-группы), разворачивает атрибутную структуру, заполняет строки нормализованными данными и переименовывает листы по категории. Управление — через Telegram-бот (одна кнопка `ВКЛЮЧИТЬ`).

**Состояние на 2026-05-02: все 5 флоу активны, система в рабочем состоянии.**

## Карта проекта

```mermaid
%%{init: {"themeVariables": {"fontSize": "10px"}}}%%
flowchart LR
    TG["TG Bot Control\n[Utility]"]
    WH["WB Flow Webhook\n[Source/Orchestrator]"]
    AT["WB Атрибуты новых страниц\n[Engine/Subflow]"]
    ZP["WB Заполнение новых строк\n[Engine/Subflow]"]
    RN["WB Ренейминг листа\n[Engine/Subflow]"]
    GS[("Google Sheets")]
    WBApi[("WB card.json API")]

    TG -->|"Включить → Execute"| WH
    WH -->|"resolution=new"| AT
    WH -->|"sheetName"| ZP
    WH -->|"все листы + типы"| RN
    AT & ZP -->|"R/W"| GS
    AT & ZP -->|"GET"| WBApi
    RN -->|"batchUpdate title"| GS
```

## Flow-паспорта

| Layer | Type | n8n Name | ID | Паспорт | JSON |
|-------|------|----------|----|---------|------|
| Utility | workflow | `Wildberries / Utility / TG Bot Control` | `OCOu4G3k5W7JchYE` | [tg-bot-control](./flow-docs/tg-bot-control.md) | [→](./flows/wildberries-utility-tg-bot-control.json) |
| Source | orchestrator | `Wildberries / Source / WB Flow Webhook` | `5v6bHbLoj1tNjrhT` | [wb-flow-webhook](./flow-docs/wb-flow-webhook.md) | [→](./flows/wildberries-source-wb-flow-webhook.json) |
| Engine | subflow | `WB Атрибуты новых страниц` | `K2b7NpHHLXbr9FDz` | [wb-atributy-novyh-stranic](./flow-docs/wb-attributes-new-pages.md) | [→](./flows/wb-atributy-novyh-stranic.json) |
| Engine | subflow | `WB Заполнение новых строк` | `88LhHNzfuXNgHTR8` | [wb-zapolnenie-novyh-strok](./flow-docs/wb-fill-new-rows.md) | [→](./flows/wb-zapolnenie-novyh-strok.json) |
| Engine | subflow | `WB Ренейминг листа` | `JgnGeSxjOeSLeZQT` | [wb-renejming-lista](./flow-docs/wb-rename-sheet.md) | [→](./flows/wb-renejming-lista.json) |

## Contracts

- **TG Bot Control → WB Flow Webhook**: вызов через `executeWorkflow`, входных данных нет.
- **WB Flow Webhook → WB Атрибуты новых страниц**: листы с `resolution=new`; сабфлоу пишет заголовки в A1.
- **WB Flow Webhook → WB Заполнение новых строк**: `sheetName`; сабфлоу читает весь лист, заполняет незаполненные строки батчем.
- **WB Flow Webhook → WB Ренейминг листа**: все листы со `sheetId`; фильтрует шаблонные и переименовывает через batchUpdate.
- **Google Sheets**: spreadsheet ID `1L3LBcyYm1pY0UTTenMr53kCruzaD0XNjkFPYqfPUbNg`; технический лист (ренейминг) — `gid=771469630`.
- **WB card.json**: URL = `https://basket-{basket}.wbbasket.ru/vol{vol}/part{part}/{nm}/info/ru/card.json`.

## Нейминг

Три Engine-сабфлоу созданы до конвенции `Wildberries / <Layer> / <Name>`. Переименование — в backlog; текущее состояние canonical.
