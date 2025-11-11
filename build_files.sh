#!/usr/bin/env bash

echo "Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput
