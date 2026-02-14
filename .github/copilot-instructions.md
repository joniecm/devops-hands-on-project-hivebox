# Copilot Project Rules

## Source Structure (src)

- Keep `src/app.py` focused on app setup, middleware, and blueprint registration only.
- Place each HTTP endpoint in its own module under `src/routes/` using a Flask `Blueprint`.
- Keep business logic in `src/services/` modules; routes should only orchestrate calls and format responses.
- Services may be classes or functions, but avoid mixing HTTP concerns into services.
- Prefer explicit dependencies passed to services or pulled from a service that owns configuration.

## Tests Structure (tests)

- Split tests by area and layer.
- Unit tests live in `tests/unit/` and use `unittest` unless the file already uses `pytest`.
- Integration tests live in `tests/integration/` and use `pytest`.
- Use `conftest.py` for shared pytest fixtures (for example, Flask test client).
- Name test files as `test_<area>_<layer>.py` and keep each file focused on a single area.

## General

- Keep test imports aligned with the module under test.
- Do not add new endpoints in `src/app.py`.
- Update tests when moving code between modules.
