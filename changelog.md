# lab-n8n changelog

## 2026-05-02 (сессия 2)

- Зафиксировано canonical состояние проекта Wildberries: все 5 флоу (`Wildberries / Utility / TG Bot Control`, `Wildberries / Source / WB Flow Webhook`, `WB Атрибуты новых страниц`, `WB Заполнение новых строк`, `WB Ренейминг листа`) активны и отлажены.
- Скачаны и сохранены canonical JSON-экспорты всех 5 флоу в `projects/wildberries/flows/` (файлы `wildberries-utility-tg-bot-control.json`, `wildberries-source-wb-flow-webhook.json`, `wb-atributy-novyh-stranic.json`, `wb-zapolnenie-novyh-strok.json`, `wb-renejming-lista.json`).
- Обновлены `projects/wildberries/README.md` и `projects/wildberries/flows/README.md`: теперь отражают canonical состояние, карту проекта с mermaid-схемой, контракты и ссылки на новые JSON-файлы.

## 2026-05-02

- Restored the Wildberries Telegram control bot as an active one-button launcher: `TG Bot Control` now shows only `ВКЛЮЧИТЬ` and calls the orchestrator `WB Flow Webhook` via webhook `wb-flow`.
- Kept `WB Flow Webhook` as the active orchestrator and updated its source-flow passport/docs to reflect the Telegram-driven launch path.
- Added canonical passports for `WB Flow Webhook`, `TG Bot Control`, `WB Атрибуты новых страниц`, `WB Заполнение новых строк`, and `WB Ренейминг листа`.
- Added matching MCP export snapshots for the restored bot and the active Wildberries flows, then updated the project/flow-doc indexes to point at them.

## 2026-05-01

- Fixed Wildberries main flow rename guard: `Фильтр конфликтов имён` now ignores the exact sheet title `Шаблон` during collision checks, so technical sheets can still be renamed when that reserved name is involved.
- Added a workspace rule: before creating any new node, first run `search_templates` to review ready-made templates and patterns, then design the node manually.
- Added new workspace rule: when creating a new flow or subflow, write the flow-doc passport first, mark it `unimplemented`, then create an n8n skeleton with default-setting placeholder nodes and synchronized names/notes; also added `docs/development-ideas.md` for future ideas like AI-in-n8n UI support and node error analysis without full flow export.
- Documented the Wildberries Telegram utility flow: added `projects/wildberries/flow-docs/tg-bot-control.md`, promoted `projects/wildberries/README.md` and `projects/wildberries/flow-docs/README.md` to a two-flow index, and noted the live-only export state in `projects/wildberries/flows/README.md`.
- Exported the first working snapshot of `TG Bot Control` to `projects/wildberries/flows/tg-bot-control.mcp-export.latest.json` and linked it from the Wildberries project indexes.
- Fixed live `Wildberries / Utility / TG Bot Control`: all Telegram reply nodes now use plain string `chatId` expressions instead of resource-locator objects (`Send Menu`/`Reply Status` from `$json.chatId`, `Reply On`/`Reply Off` from `$('Switch Action').item.json.chatId`). The workflow is reactivated and validation is `valid=true` with warnings only.
- Fixed live `WB Flow` template/new-sheet detection regression: `Получить заголовки листа` was reverted to `!1:1`, so `Определить тип листа` could not see row 2 and classified filled 3-column sheets as `template`. Restored the live range to `!1:2`; validation remains at the pre-existing `Фильтр конфликтов имён` validator error plus warnings.
- Added §14 Fetch-стратегия to CLAUDE.md: passport-first hierarchy (паспорт → mode=structure → mode=full), four practical workflow modes, sync discipline rule; lists marked as working draft pending regular review.
- Full passport resync via mode=full: rewrote §2.2 (added missing Merge node b7bd055f, removed 3 phantom nodes), rewrote §2.3 (window-based approach never existed in live — replaced with Читать все строки листа + Loop Over Items + No Operation), updated §5 Skeleton to match live topology, updated §1/§4 to reflect active=false status.
- Added §6 Node Registry: IDs for all 33 operational nodes.
- Added §7 Code Snapshots: all 11 Code nodes fully populated from mode=full.
- Added §8 Key Expressions: all HTTP nodes and key params fully populated.
- Added §9 Connection Index Table: 5 non-standard connections.

## 2026-04-30

- Implemented strict computed-window processing in live `WB Flow`: old full-sheet read is replaced by `Читать границы окна` (`A2:A3`), `Построить диапазон окна`, and `Читать строки окна`; row detection now resolves `SKU`, `Ссылка`, `Фото`, `Название` by header names to support a leading `ФОРМУЛЫ` column. No fallback/full-scan guard is used; missing `A3` on `Ковры` was observed as execution errors `2575`/`2576`.
- Switched the computed-window contract in live `WB Flow` from `A2:A3` to packed `A1=[start;end]`. `Построить диапазон окна` now parses the packed string and normalizes boundary order with `min/max`, so `[4;3]` is treated as rows `3..4`. Transition error `2614` still reflected the old `A2:A3` expectation; after the update, executions `2615` and `2616` completed successfully.
- Synchronized Wildberries repo artifacts with live n8n as source of truth: refreshed `wb-flow.mcp-export.latest.json` to active `WB Flow` structure (38 nodes, 33 simplified connections), updated README/flow-doc active schedule state (20-second trigger), current validation (`valid=false`, one validator error on `Фильтр конфликтов имён`, 33 warnings), and latest observed executions/errors including Google Sheets `ReadRequestsPerMinutePerUser` quota failures on `Получить список листов`.
- Three fixes to `WB Flow` from review: (1) `Собрать батч строк` now filters items with empty `Название` before writing — failed card.json fetches are silently skipped and retried next run instead of writing blank data; (2) removed dead `writeHeaders` field from `Нормализовать карточку WB` output; (3) `Читать все строки листа` range extended from `A1:ZZ1000` to `A1:ZZ30000`. Updated `wb-flow.md` §2.3.
- Replaced per-row writes with batch write in `WB Flow`: added `Собрать батч строк` (Code node) between `Объединить строку и карточку` and `Записать строку в лист`. `Собрать батч строк` aggregates all items into a single `batchData` array; `Записать строку в лист` changed from PUT `values/{range}` (1 call per row, up to 50/run) to POST `values:batchUpdate` (1 call per run). Eliminates Google Sheets "too many requests" errors under the 20-second schedule. Updated `wb-flow.md` §2.3 and skeleton §5.
- Added `Лимит батча` (n8n-nodes-base.limit, maxItems=50) to `WB Flow` after `Найти незаполненные строки`. Each run now processes at most 50 unfilled rows; Schedule Trigger iterates through the full sheet over subsequent runs. Updated `wb-flow.md` §2.3 and skeleton §5.
- Renamed all 30 technical nodes in `WB Flow` to meaningful Russian names, synchronized with `wb-flow.md` passport. Updated code cross-references in 3 nodes: `Собрать заголовки из карточки` (`$items("Построить URL card.json")`), `Первая строка на лист` (`$('Только листы "Лист..."')`), `Фильтр конфликтов имён` (`$('Разобрать список листов')`). Added missing `Первая строка на лист` and `Фильтр конфликтов имён` nodes to Mermaid skeleton §5. Removed obsolete "node naming временный" remark from §4. Saved pre-rename backup to `flows/backups/wb-flow.before-node-rename.20260430.json`.
- Fixed column desync bug in `WB Flow` (final): reverted to always using `$json.headers` in `Append or update row in sheet1`. The intermediate `headers.length > 3` conditional reintroduced misalignment for new multi-row sheets — different cards in the same sheet have attributes in different orders, so per-card `writeHeaders` is never safe. For new sheets where `Code in JavaScript6` reads before `HTTP Request4` writes full headers (race condition), the write harmlessly reproduces the existing 3 values; full attributes are written on the second pass. Single-run fill for new sheets is not achievable without rearchitecting the parallel branches — deferred as out of scope.
- Fixed rename path bugs in `WB Flow`: (1) `Get row(s) in sheet2` returns all rows per sheet — added `Deduplicate sheets` Code node that keeps first row per sheet using `pairedItem` tracing to `Filter1`, propagates `sheetName`; (2) `Merge3` changed from `combineByPosition` to `combineByFields` on `sheetName` — previously mismapped sheetId to wrong category when multiple rows existed per sheet; (3) added `Skip existing sheet names` Code node before `HTTP Request7` to prevent Google Sheets `_conflict{id}` suffixed tab names when target name already exists. Updated `wb-flow.md` §2.5.
- Canonicalized canvas/passport rules in `DESIGN.md` §9 and `flow-doc-template.md`: sticky-подложки → подзаголовки Steps, имена нод синхронны с canvas, Mermaid skeleton = один блок/нода + subgraph/подложка, пустая подложка = пустой subgraph.
- Applied corrections to `WB Flow` passport: removed local `Canvas Documentation Rules` section (правила теперь в DESIGN.md), перенумерованы секции (2→Steps, 3→Contracts, 4→Validation Notes, 5→Skeleton), убраны строки `Sticky-подложка canvas:` (имя подложки = заголовок), в skeleton удалён псевдо-нод `NOTE2` из пустого subgraph SN2 и связь `CJ8 -.-> NOTE2`.
- Documented Wildberries canvas/passport synchronization rules and reorganized the `WB Flow` passport around canvas sticky-note sections with one Mermaid block per n8n node.
- Fixed `WB Flow` all-sheets fill path: removed the repeated Google Sheets read node that reused the first sheet, connected row candidates directly to card URL generation, and changed the merge before final write to combine by position.
- Fixed `WB Flow` header/row alignment for new Wildberries sheets: backed up the previous MCP export, generated per-item headers, carried `writeHeaders` into row normalization, changed final row writes to raw Google Sheets `values.update`, connected existing trigger nodes to the main start, and removed the unreachable self-call node.
- Bound the `wildberries` project documentation strictly to the single n8n workflow `WB Flow` (`dM0BgWX6GtyGLPFw`) and removed secondary flow references.
- Created the `WildBerries` project scaffold from the project README template.
- Replaced invented WildBerries documentation with TBD placeholders pending MCP workflow export.
- Added a documentation discipline rule: no invented docs, only user requirements or observed workflow/artifact facts.

## 2026-05-01

- Documented the Wildberries template-sheet fix: a Google Sheets tab with only three seed headers (`SKU`, `Ссылка`, `Фото`) and no data rows must not be classified as `new`. Updated `projects/wildberries/flow-docs/wb-flow.md` and `projects/wildberries/README.md` to require `Получить заголовки листа` reading `!1:2` and `Определить тип листа` returning `template` when row 2 is empty.

## 2026-04-29

- Migrated the git repository root from nested `repo/` to the workspace root and created the target project structure.
- Removed empty cookbook and shared project placeholders from the target structure.
- Collapsed per-project `design`, `dashboards`, and ADR files into the project README.
- Reworked Job Searcher README as a project passport with business value, As Is/To Be maps, contracts, and flow passport links.
- Restored the RemoteOK Pipeline flow passport from AI-generated inbox into project flow-docs and updated the project passport from it.
- Added a reusable project README template based on the Job Searcher passport.
- Made `DESIGN.md` the current practice design document and cleaned it around project sections.
- Reframed `docs/AI-generated/` as a short-lived inbox.
- Softened golden-test requirements and deferred external-service specifics.
- Made `CLAUDE.md` the main workspace rules file.
- Reduced `AGENTS.md` to a thin Codex-specific layer that points to `CLAUDE.md`.
- Moved the engineering practice design document to the workspace root for review.
- Added node naming and shell UTF-8 rules to the shared `CLAUDE.md` rules.
