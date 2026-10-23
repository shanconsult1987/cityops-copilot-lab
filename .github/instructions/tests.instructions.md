---
applyTo: "tests/**/*.py"
---

# Test Instructions

When modifying files under tests/:

- Use unittest.
- Do not use pytest.
- Keep tests independent.
- Reset global state in setUp.
- Test both expected behavior and important edge cases.
- Test behavior rather than implementation details.
- Do not modify production code merely to make a test pass.