# CityOps Copilot Instructions

## Project purpose

CityOps is a small Python application for recording and classifying
city operations incidents.

## Engineering principles

- Keep the application simple.
- Prefer Python standard library.
- Do not introduce dependencies without justification.
- Preserve existing public function signatures unless explicitly requested.
- Every behavior change must have tests.
- Never invent external APIs or infrastructure.
- Do not expose secrets or credentials.
- Prefer readable code over clever code.

## Incident classification

Severity must be one of:

- critical
- high
- medium
- low

## Testing

Use Python unittest.

Tests must cover:

- normal behavior
- edge cases
- invalid or unexpected input where relevant

## Security

Never place credentials, API keys, tokens, or connection strings
in source code.

## AI-generated code

Treat Copilot output as a proposal.

Review:
- correctness
- security
- maintainability
- edge cases
- tests