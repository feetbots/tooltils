# v1.4.4-1

## 1.4.4-1 (7/9/2023)

Forgot to change some things bruh<br><br>

**Additions:**
- Version release date in `info.py`
- `info` section in the API
- `str()` method on each `info.py` property so that pylance (python linter for vsc) doesn't recognise them as direct literals

<br>

**Removals:**
- Build system as setuptools in `pyproject.toml` as having `setup.py` wouldn't work regardless

<br>

**Changes:**
- Updated README.md file request `__str__()` method variable to return the correct string
- Made sure the correct release date was present on every file
- Replaced '(c)' with '©' in license property in `info.py`
- Rename `setup.py` to `!setup.py` to avoid backend subprocess error when building package binaries
