import funçoes

funçoes.login()
while True:
   print("Bem vindo a sla aplicativo de música")
   print("""___MENU___
1. Acessar músicas salvas
2. Acessar suas playlists 
""")
   acesso_menu = int(input("O que deseja fazer: "))
   if acesso_menu == 1:
      funçoes.acesso_musicas_salvas()
   elif acesso_menu == 2:
      funçoes.acesso_playlists()
   sair = input("Você deseja sair? (sim/não) ")
   if sair == "sim":
      break