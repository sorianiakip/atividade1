# Exercício 08 - Repetição com while em Python
senha_correta = "python123"
limite_tentativas = 3
tentativas = 0
acesso_liberado = False

while tentativas < limite_tentativas and not acesso_liberado:
   senha = input(f"Digite a senha ({tentativas + 1}/{limite_tentativas}): ")

   if senha == senha_correta:
       acesso_liberado = True
   else:
      tentativas += 1
      restantes = limite_tentativas - tentativas

      if restantes > 0:
          print(f"Senha incorreta. Restam {restantes} tentativa(s).")

if acesso_liberado:
    print("Acesso liberado!")
else:
    print("Acesso bloqueado: limite de tentativas atingido.")