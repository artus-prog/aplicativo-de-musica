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
   
   break