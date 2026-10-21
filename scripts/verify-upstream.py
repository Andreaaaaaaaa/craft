#!/usr/bin/env python3
"""Verify the pinned upstream snapshots without executing their code."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
upstream = root / 'upstream'
manifest = json.loads((upstream / 'manifest.json').read_text())
errors = []
for source in manifest['sources']:
    base = upstream / source['name']
    for name, expected in source['files'].items():
        path = base / name
        if isinstance(expected, dict):
            valid = path.is_symlink() and str(path.readlink()) == expected['symlink']
        else:
            valid = path.is_file() and not path.is_symlink() and hashlib.sha256(path.read_bytes()).hexdigest() == expected
        if not valid:
            errors.append(f'{source["name"]}/{name}')
    print(f'{source["name"]}: checked {len(source["files"])} pinned files at {source["commit"][:12]}')
if errors:
    raise SystemExit('Snapshot mismatch:\n' + '\n'.join(errors))
print('All pinned upstream files match the manifest.')
