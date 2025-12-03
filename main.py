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
      while True:
         print("""___músicas salvas___
1. Ouvir múscicas salvas
2. Acessar músicas salvas""")
         if len(funçoes.musicas_salvas) == 0:
            print("Você não possui músicas salvas")
         else:
            print(f"Suas músicas salvas são: {funçoes.musicas_salvas}")
         break
      

   break