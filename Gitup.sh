#!/bin/bash
# Descrizione:
# File che permette il caricamento su GitHub di tutti i file in questa cartella.
echo 'Adding..'
git add *
echo 'Commit message:'
read text
git commit -m "$text"
echo 'pushing files..'
git push origin master
