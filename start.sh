#!/bin/bash
echo ">> Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo ">> Criando tabelas no banco de dados..."
python3 <<EOF
from src.main import db, app
with app.app_context():
    db.create_all()
EOF

echo ">> Concluído."