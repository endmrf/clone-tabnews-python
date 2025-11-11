#!/usr/bin/env bash

echo "Coletando arquivos estáticos..."
python3 clone_tabnews_python/manage.py collectstatic --noinput
