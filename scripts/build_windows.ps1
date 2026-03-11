Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ArtifactDir = Join-Path $Root "build_artifacts"
$DistDir = Join-Path $ArtifactDir "dist"
$WorkDir = Join-Path $ArtifactDir "build"
$SpecDir = $ArtifactDir
$AppName = "OpenFilters"

python -m pip install --upgrade pip pyinstaller

pyinstaller `
  --noconfirm `
  --windowed `
  --name $AppName `
  --icon (Join-Path $Root "OpenFilters.ico") `
  --distpath $DistDir `
  --workpath $WorkDir `
  --specpath $SpecDir `
  --add-data "$Root\color\illuminants;color/illuminants" `
  --add-data "$Root\color\observers;color/observers" `
  --add-data "$Root\materials;materials" `
  --add-data "$Root\examples;examples" `
  --add-data "$Root\config;config" `
  --add-data "$Root\modules;modules" `
  (Join-Path $Root "Filters.py")

$ZipPath = Join-Path $ArtifactDir "OpenFilters-windows-x64.zip"
if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
Compress-Archive -Path (Join-Path $DistDir "$AppName\*") -DestinationPath $ZipPath

Write-Host "Windows package ready:"
Write-Host "  $ZipPath"

