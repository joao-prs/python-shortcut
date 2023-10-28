import os

# checa 
caminho_pasta = "/backup_automatic"

# Verifica se a pasta existe
if not os.path.exists(caminho_pasta):
  # Se não existir, cria
  os.makedirs(caminho_pasta)
  print(f"A pasta '{caminho_pasta}' foi criada com sucesso!")
else:
  # ja tinha, bobo
  print(f"A pasta '{caminho_pasta}' já existe.")