import os
import re

# Caminho da sua pasta
pasta = "/home/ivaldo/Documentos/biblia"

# Percorrer todos os arquivos .html
for raiz, dirs, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if arquivo.endswith('.html'):
            caminho = os.path.join(raiz, arquivo)
            
            print(f"Processando: {arquivo}")
            
            # Ler o arquivo
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Contar antes
            antes = len(re.findall(r'\.html', conteudo))
            
            # Fazer substituições
            novo_conteudo = conteudo.replace('.html"', '"')
            novo_conteudo = novo_conteudo.replace(".html'", "'")
            novo_conteudo = novo_conteudo.replace('.html?', '?')
            novo_conteudo = re.sub(r'href="([^"]+?)\.html"', r'href="\1"', novo_conteudo)
            novo_conteudo = re.sub(r"href='([^']+?)\.html'", r"href='\1'", novo_conteudo)
            
            # Contar depois
            depois = len(re.findall(r'\.html', novo_conteudo))
            
            # Salvar
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(novo_conteudo)
            
            print(f"  Removidos: {antes - depois} ocorrências")

print("Concluído!")