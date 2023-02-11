"""
Certify the developer has input all requirements for PR.

Situations tested:

* additions are reported in CHANGELOG.rst
"""
import os
import sys
from pathlib import Path

folder = Path(__file__).resolve().parents[1]
changelog = Path(folder, 'CHANGELOG.rst')


class ChangelogError(Exception):
    pass


with open(changelog, 'r') as fin:
    for line in fin:
        if line.startswith('v'):
            msg = [
                '',
                'CHANGELOG.rst not updated:',
                'Please add a summary of your additions as described in:',
                'https://python-project-skeleton.readthedocs.io'
                '/en/latest/contributing.html#update-changelog.',
                '',
                ]
            sys.exit(os.linesep.join(msg))

        elif line.startswith('*'):
            break
