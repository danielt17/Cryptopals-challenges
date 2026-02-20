import json
import py_compile
import sys
from pathlib import Path

ROOT = Path('.')
SRC = ROOT / 'src'
SCRIPTS = ROOT / 'scripts'

payload = json.loads((SCRIPTS / 'challenge_map.json').read_text(encoding='utf-8'))
set_info = payload['set_info']
challenges = payload['challenges']

errors = []

for num_str, info in challenges.items():
    num = int(num_str)
    set_slug = set_info[str(info['set'])]['slug']
    base = SRC / 'sets' / f"set_{info['set']:02d}_{set_slug}" / f"challenge_{num:02d}_{info['slug']}"
    if not base.exists():
        errors.append(f"Missing challenge directory: {base}")
        continue
    writeup = base / 'writeup.md'
    if not writeup.exists():
        errors.append(f"Missing writeup: {writeup}")
    for script in info.get('scripts', []):
        script_path = base / script['file']
        if not script_path.exists():
            errors.append(f"Missing script: {script_path}")
    for data_file in info.get('data_files', []):
        data_path = base / data_file
        if not data_path.exists():
            errors.append(f"Missing data file: {data_path}")

# Compile all Python files
for path in list(SRC.rglob('*.py')) + list(SCRIPTS.rglob('*.py')):
    try:
        py_compile.compile(str(path), doraise=True)
    except Exception as exc:
        errors.append(f"PyCompile failed: {path} -> {exc}")

# Scan for old Q imports
for path in SRC.rglob('*.py'):
    text = path.read_text(encoding='utf-8')
    if 'from Q' in text or 'import Q' in text:
        errors.append(f"Legacy Q import found: {path}")

if errors:
    print('Verification failed:')
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print('Verification passed: structure, writeups, data files, and syntax checks are OK.')
