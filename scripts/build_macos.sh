#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${ROOT_DIR}/.venv-gui"
APP_NAME="OpenFilters"
ARTIFACT_DIR="${ROOT_DIR}/build_artifacts"
DIST_DIR="${ARTIFACT_DIR}/dist"
WORK_DIR="${ARTIFACT_DIR}/build"
SPEC_DIR="${ARTIFACT_DIR}"
DMG_ROOT="${ARTIFACT_DIR}/dmg_root"
DMG_PATH="${ARTIFACT_DIR}/${APP_NAME}-macOS-arm64.dmg"

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "Missing virtualenv: ${VENV_DIR}"
  exit 1
fi

source "${VENV_DIR}/bin/activate"
python -m pip install --upgrade pyinstaller

export PYINSTALLER_CONFIG_DIR="/tmp/pyinstaller_config"

pyinstaller \
  --noconfirm \
  --windowed \
  --name "${APP_NAME}" \
  --icon "${ROOT_DIR}/OpenFilters.icns" \
  --paths "${ROOT_DIR}" \
  --distpath "${DIST_DIR}" \
  --workpath "${WORK_DIR}" \
  --specpath "${SPEC_DIR}" \
  --add-data "${ROOT_DIR}/color/illuminants:color/illuminants" \
  --add-data "${ROOT_DIR}/color/observers:color/observers" \
  --add-data "${ROOT_DIR}/materials:materials" \
  --add-data "${ROOT_DIR}/examples:examples" \
  --add-data "${ROOT_DIR}/config:config" \
  --add-data "${ROOT_DIR}/modules:modules" \
  "${ROOT_DIR}/Filters.py"

rm -rf "${DMG_ROOT}"
mkdir -p "${DMG_ROOT}"
cp -R "${DIST_DIR}/${APP_NAME}.app" "${DMG_ROOT}/"
ln -s /Applications "${DMG_ROOT}/Applications"

hdiutil create \
  -volname "${APP_NAME}" \
  -srcfolder "${DMG_ROOT}" \
  -ov \
  -format UDZO \
  "${DMG_PATH}"

echo "macOS package ready:"
echo "  ${DMG_PATH}"
