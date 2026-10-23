# CityOps Copilot Lab

A deliberately small application used to explore GitHub Copilot.

## Scenario

City operations teams receive incident reports from citizens.

The application:

- creates incidents
- classifies severity
- stores incidents in memory
- lists incidents

## Run

```powershell
python app.py
```

## Tests

Run the unit tests from the repository root using Python's built-in test runner
(no extra dependencies):

```powershell
python -m unittest discover -s tests -t . -v
```

The `tests` package also supports default discovery from the repository root:

```powershell
python -m unittest discover -v
```

VS Code workspace settings use the repository root as the test working directory
and import root. After changing test settings, run **Test: Refresh Tests** in the
Command Palette. Running discovery from inside `tests` without specifying the
repository as the top-level directory can cause `ModuleNotFoundError: No module
named 'app'`.

## Line coverage

Latest verified result: **10 tests passed**, with **100% line coverage** for
`app.py`.

| File | Executable statements | Missed statements | Line coverage |
| --- | --- | --- | --- |
| `app.py` | 26 | 0 | 100% |

This is a snapshot of the latest local run, not an automatically updated result.
Rerun the commands below after code or test changes.

Install the development dependencies, then run the tests with coverage:

```powershell
python -m pip install -r requirements-dev.txt
python -m coverage run -m unittest discover -s tests -v
python -m coverage report
```

The report measures `app.py` and lists any uncovered lines. To generate a
browsable report:

```powershell
python -m coverage html
```

Open `htmlcov/index.html` in a browser. Generated coverage files are ignored by Git.