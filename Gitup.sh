#!/bin/bash
echo 'Adding..'
git add *
echo 'Commit message:'
read text
git commit -m "$text"
echo 'pushing files..'
git push origin master
