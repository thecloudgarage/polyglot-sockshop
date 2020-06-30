#!/bin/bash
git init
git remote add polyglot-sockshop  https://github.com/thecloudgarage/polyglot-sockshop.git
git add .
git commit -m 'new commit'
git push -f polyglot-sockshop master
