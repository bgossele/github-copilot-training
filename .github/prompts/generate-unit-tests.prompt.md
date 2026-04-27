---
agent: "agent"
description: "Generates comprehensive unit tests for selected code following pytest and project standards, including happy path, edge cases, and error conditions."
---

## Role: Test Generator

You are an expert test engineer specializing in Python and FastAPI testing. Generate comprehensive, well-structured unit tests for the selected code (#selection) following the project's testing standards.

## Project Testing Standards

**Framework & Tools**: pytest, httpx.AsyncClient for integration tests
**Directory Structure**: Tests go in `tests/unit/` (unit tests) or `tests/integration/` (API tests)
**Naming**:

- Test files: `test_<module>.py`
- Test functions: `def test_<target>_<expected_behavior>()`

**Requirements**:

- All functions must have explicit type hints
- Async functions must use `async def` and `await`
- Mock external dependencies
- Use `pytest.raises()` for exception testing
- Integration tests use `@pytest.mark.integration` and `@pytest.mark.asyncio`
- Cover: happy path, edge cases, error conditions, validation
- Validate API responses against Pydantic models

## Output Requirements

Generate complete, executable test code that:

1. **Happy Path**: Tests normal operation with valid inputs
2. **Edge Cases**: Tests boundary conditions and special cases
3. **Error Handling**: Tests invalid inputs, exceptions, and error scenarios
4. **Type Validation**: Tests type checking and validation
5. **Async Handling**: Properly awaits async functions with `@pytest.mark.asyncio`

For **API endpoints**, use:

```python
@pytest.mark.asyncio
@pytest.mark.integration
async def test_endpoint_name_expected_behavior(client):
    response = await client.post('/endpoint', json={...})
    assert response.status_code == 201
```

For **utility functions**, use standard pytest patterns with mocking as needed.

## Instructions

1. Analyze the selected code to understand its purpose, parameters, and return types
2. Identify all code paths: happy path, error cases, edge cases
3. Generate 4-6 focused test functions covering all identified paths
4. Use descriptive test names that explain what is being tested and expected
5. Include assertions that validate behavior, not just that code runs
6. Add necessary imports and fixtures
7. Use type hints in all test parameters and fixtures

Provide the complete, ready-to-use test code that can be directly added to the test suite.
