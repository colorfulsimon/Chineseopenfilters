# Packaging Guide

## macOS (Apple Silicon)

Run:

```bash
cd "/Users/simonzhang/Documents/New project/OpenFilters"
chmod +x scripts/build_macos.sh
./scripts/build_macos.sh
```

Output:

- `build_artifacts/OpenFilters-macOS-arm64.dmg`

## Windows 10 x64

Local build on Windows PowerShell:

```powershell
cd "C:\path\to\OpenFilters"
.\scripts\build_windows.ps1
```

Output:

- `build_artifacts/OpenFilters-windows-x64.zip` (contains `OpenFilters.exe`)

## Build Windows EXE via GitHub Actions

Workflow file:

- `.github/workflows/build-windows-exe.yml`

How to run:

1. Open repository Actions page.
2. Select `Build Windows EXE`.
3. Click `Run workflow`.
4. Download artifact `OpenFilters-windows-x64`.

