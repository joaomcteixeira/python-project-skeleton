"""
Certify the developer has input all requirements for PR.

Situations tested:

* additions are reported in CHANGELOG.rst
"""
from pathlib import Path

folder = Path(__file__).resolve().parents[1]
changelog = Path(folder, 'docs', 'CHANGELOG.rst')

with open(changelog, 'r') as fin:
    for line in fin:
        if line.startswith('v'):
            raise ValueError
        elif line.startswith('*'):
            break
