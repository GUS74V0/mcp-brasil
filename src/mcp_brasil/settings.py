"""Configuração global do mcp-brasil.

Valores podem ser sobrescritos via variáveis de ambiente.
"""

from __future__ import annotations

import os

# --- HTTP Client ---
HTTP_TIMEOUT: float = float(os.environ.get("MCP_BRASIL_HTTP_TIMEOUT", "30.0"))
HTTP_MAX_RETRIES: int = int(os.environ.get("MCP_BRASIL_HTTP_MAX_RETRIES", "3"))
HTTP_BACKOFF_BASE: float = float(os.environ.get("MCP_BRASIL_HTTP_BACKOFF_BASE", "1.0"))
USER_AGENT: str = os.environ.get("MCP_BRASIL_USER_AGENT", "mcp-brasil/0.1.0")
