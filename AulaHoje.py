def criptografar_arquivo(nome_arquivo_entrada, deslocamento, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r', encoding='latin-1') as arquivo_entrada:
        texto = arquivo_entrada.read()
    texto_criptografado = ''
    for letra in texto:
        nova_letra = chr((ord(letra) + deslocamento) % 256)
        texto_criptografado += nova_letra
    with open(nome_arquivo_saida, 'w', encoding='latin-1') as arquivo_saida:
        arquivo_saida.write(texto_criptografado)

def descriptografar_arquivo(nome_arquivo_entrada, deslocamento, nome_arquivo_saida):
    with open(nome_arquivo_entrada, 'r', encoding='latin-1') as arquivo_entrada:
        texto = arquivo_entrada.read()
    texto_descriptografado = ''
    for letra in texto:
        nova_letra = chr((ord(letra) - deslocamento) % 256)
        texto_descriptografado += nova_letra
    with open(nome_arquivo_saida, 'w', encoding='latin-1') as arquivo_saida:
        arquivo_saida.write(texto_descriptografado)

criptografar_arquivo('arquivo.txt', 5, 'arquivo_criptografado.txt')
descriptografar_arquivo('arquivo_criptografado.txt', 5, 'arquivo_descriptografado.txt')