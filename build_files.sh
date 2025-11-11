#!/usr/bin/env bash

echo "Criando e ativando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# echo "Coletando arquivos estáticos..."
# python3 clone_tabnews_python/manage.py collectstatic --noinput
