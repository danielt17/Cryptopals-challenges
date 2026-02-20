# Cryptopals Challenges Docs

This folder collects project-facing documentation and pointers into the challenge writeups.

## Quick links
- Challenge index: docs/challenges.md
- Legacy writeup index: docs/legacy_writeup.md
- Challenge launcher: scripts/run_challenge.py
- Verification script: scripts/verify_project.py

## Layout
- src/sets/ holds the per-set, per-challenge directories.
- Each challenge directory includes the script(s), data files, and writeup.md.
- docs/ collects indexes and additional notes.
- scripts/ provides the launcher and verification helpers.

## Running
List challenges:
```powershell
python scripts/run_challenge.py --list
```

Run a challenge:
```powershell
python scripts/run_challenge.py 34
```

Run a specific script when a challenge has multiple steps:
```powershell
python scripts/run_challenge.py 34 --script server.py
```
