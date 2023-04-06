def criptografar(frase):
  mensagem = ""

  for i in frase:
    mensagem = mensagem + chr(ord(i) + 5)
  return mensagem


def descriptografar(mensagem):
  frase = ""

  for i in mensagem:
    frase = frase + chr(ord(i) - 5)
  return frase


print("eu gosto de voce")
palavra = criptografar("eu gosto de voce")
print(palavra)
print(descriptografar(palavra))
