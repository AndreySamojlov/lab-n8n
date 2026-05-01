# lab-n8n

Рабочее пространство практики разработки n8n-workflow для self-host платформы `lab-infra`.

## Что здесь живёт

- `projects/` — отдельные разделы n8n-проектов, включая `wildberries` с engine flow `WB Flow` и utility flow `TG Bot Control`.
- `docs/` — шаблоны и временный AI-generated inbox.
- `scripts/` — локальные guardrails и вспомогательные скрипты.
- `DESIGN.md` — текущий дизайн практики.
- `CLAUDE.md` — главный файл правил агента.
- `AGENTS.md` — тонкий Codex-specific слой.

## Проекты

- [`projects/job-searcher/`](./projects/job-searcher/) — пилот функциональной системы обработки вакансий (`Filter` → `Source` → `Engine` → `Analysis`).
- [`projects/wildberries/`](./projects/wildberries/) — active-проект automation для Wildberries: `WB Flow` + `TG Bot Control`.

## Чего здесь нет

- Инфра-настройки n8n, домены, сертификаты — это `AndreySamojlov/lab-infra` (workspace `../../lab-infra/`).

## Связь с `lab-infra`

Воркфлоу из этого репо разворачиваются на инстансе n8n, поднятом `lab-infra`. Канал создания — MCP-сервер `n8n-mcp` по адресу `https://n8n-mcp.samandrey.work/mcp`. Детали контура, доменов и ротации секретов — в `lab-infra`.

## Дисциплина

- Кодировка: UTF-8 без BOM + LF, проверяется `.gitattributes`, `.editorconfig` и `scripts/check-utf8.py`.
- Секреты в репо не попадают — только `{{ $credentials.* }}` или явные плейсхолдеры.
- Workflow перед фиксацией валидируется и проверяется вручную или через MCP test workflow.

