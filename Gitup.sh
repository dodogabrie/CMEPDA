#!/bin/bash
echo 'Adding..'
git add *
echo 'Tell me what to commit'
git commit -m "$1"
echo 'pushing'
git push origin master
