# OpenFilters Project Snapshot (2026-03-11)

## Repository
- Remote: `https://github.com/colorfulsimon/Chineseopenfilters.git`
- Branch: `main`
- Snapshot date: 2026-03-11

## Current Status
- Python 3 + wxPython Phoenix migration baseline is usable on macOS (Apple Silicon).
- Chinese localization is in active use and main UI is functionally available.
- Core runtime issues from previous rounds have been fixed (startup crashes, wx API incompatibilities, plotting/legend regressions, optimization overflow crash).

## Recent Stability Fixes (already in `main`)
- Optimizer overflow protection in derivative trig calculations.
- wx notebook compatibility (`FindPage` replacing unavailable API path).
- Plot legend height guard to prevent axis-label disappearance in multi-curve scenarios.
- PyInstaller startup path compatibility (`main_directory.py`) for frozen app.
- macOS icon warning fix: skip manual icon loading on macOS and rely on app bundle icon.

## Packaging

### macOS
- Packaging script: `scripts/build_macos.sh`
- Artifact (latest local build):
  - `build_artifacts/OpenFilters-macOS-arm64.dmg`
- Current behavior: launches successfully in latest test.

### Windows
- Packaging script: `scripts/build_windows.ps1`
- CI workflow: `.github/workflows/build-windows-exe.yml`
- Output artifact from workflow:
  - `OpenFilters-windows-x64.zip` (contains `OpenFilters.exe`)

## Key Commands

### Run app locally
```bash
cd "/Users/simonzhang/Documents/New project/OpenFilters"
source .venv-gui/bin/activate
python Filters.py
```

### Build macOS package
```bash
cd "/Users/simonzhang/Documents/New project/OpenFilters"
./scripts/build_macos.sh
```

## Known Non-Blocking Warnings
- `wxPyDeprecationWarning` messages are still present in terminal output.
- These warnings are not currently blocking use or packaging.

## Next Planned Phase
1. Continue real design/testing in macOS production usage.
2. Collect any residual localization/interaction defects.
3. If stable, finalize Windows artifact release workflow run and publish both platform packages.

