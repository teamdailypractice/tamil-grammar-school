# Agent Instructions

You are contributing to a professional Python codebase.
Follow all rules strictly.

## Python Version
- Python 3.11+

## Code Style
- Follow PEP 8
- Use type hints everywhere
- Prefer clarity over cleverness
- Use pathlib instead of os
- No wildcard imports
- Max function length ~30 lines

## Architecture
- Use src/ layout
- No business logic in __init__.py
- Separate:
  - domain (pure logic)
  - services (use cases)
  - infrastructure (IO, logging, persistence)

## Error Handling
- No bare except
- Raise domain-specific exceptions
- Never silently ignore errors

## Logging
- No print()
- Use logging module

## Testing
- Use pytest
- Every public function must have tests

## Forbidden
- No TODO placeholders
- No commented-out code