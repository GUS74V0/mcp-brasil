# TECH_DEBT.md — Interactive TODO for Technical Debt

> Track bugs, incompatibilities, mocks, and incomplete implementations.
> Update this file whenever you find something that needs attention later.

## Legend

- `[ ]` — Open (needs work)
- `[~]` — In progress
- `[x]` — Resolved

---

## Bootstrap Phase

- [x] **mount() API mismatch** — `feature.py` used `mount("/path", server)` instead of FastMCP v3's `mount(server, namespace=name)`. Fixed.
- [x] **list_tools() accessed private API** — `_tool_manager._tools` is private FastMCP internals. Removed method to avoid mypy strict failures.
- [x] **_shared/http_client.py** — Implemented with `create_client()` factory + `http_get()` with retry + exponential backoff + 429/5xx handling.
- [x] **_shared/formatting.py** — Implemented: `markdown_table`, `format_brl`, `format_number_br`, `format_percent`, `truncate_list`.
- [x] **settings.py** — Implemented with env var overrides: `HTTP_TIMEOUT`, `HTTP_MAX_RETRIES`, `HTTP_BACKOFF_BASE`, `USER_AGENT`.

## Core — Open

- [ ] **_shared/cache.py not implemented** — LRU cache with TTL mentioned in ADR-001. Planned for Semana 2.
- [ ] **justfile still exists** — Replaced by Makefile but justfile not removed. Keep or delete?

## Known Limitations

- [ ] **No CONTRIBUTING.md** — Mentioned in roadmap Semana 0 but not yet created.
- [ ] **No GitHub Actions CI** — `ruff → mypy → pytest` pipeline not configured yet.
- [ ] **pyproject.toml uses optional-dependencies instead of dependency-groups** — `uv sync --group dev` fails, must use `uv sync --extra dev`.

---

*Last updated: 2026-03-22*
