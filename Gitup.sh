#!/bin/bash
echo 'Adding..'
git add *
git commit -m "$1"
echo 'pushing'
git push origin master
