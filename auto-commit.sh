#!/bin/bash
cd "$HOME/git-experiment" || exit 1
./job.sh
git add job.sh job.log
git diff --cached --quiet || git commit -m "Automatic job update"
