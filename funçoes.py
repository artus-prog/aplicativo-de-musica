nome_playlists = []
playlists = []
musicas_salvas=[]
usuario = None
senha = None

#Está função tem relações com as funções login_entrar e primeiro_acesso
#A função desta é organizar os protocolos de login
def login():
   while True:
      login_inicial=input("Você está acessando este aplicativo pela primeira vez? (sim/não)").strip().lower()
      if login_inicial == "sim":
         primeiro_acesso()
         break

      elif login_inicial in ("não","nao"):
         login_entrar()
         break
      else:
         print("Resposta inválida!")

#A seguinte função serve para o caso de
#o usuario estar fazendo seu primeiro acesso
def primeiro_acesso():
   usuario=input("Qual nome de usúario você deseja? ")
   senha=input("Digite a senha desejada: ")
   print(f"Seu nome de usuário é: {usuario} e sua senha é: {senha}")
   with open("login", "w", encoding="utf-8") as arquivo:
      arquivo.write(f"Usuário: {usuario}\n")
      arquivo.write(f"Senha: {senha}")
   return True

#Esta função serve para os acessos 
#seguintes do usuario que ja possui conta
def login_entrar ():
   while True:
      usuário_tentativa = input("Digite seu login: ")
      senha_tentativa = input("Digite sua senha: ")
      if usuário_tentativa == usuario and senha_tentativa == senha:
         print("Login aceito")
         return True
         break
      else: 
         print("Tente novamente")

#Função a ser utilizada para salvar musicas fora de playlists
def salvar_musica(música):
   musicas_salvas.append(música)
   escolha = input("Pressione enter para sair ou digite o nome de outra música: ")
   if escolha == "":
      print(f"Ok, Suas músicas salvas agora são: {musicas_salvas}")
   else:
      salvar_musica(escolha)

#Esta função lê todos elementos de uma playlist um por um
def escutarPlaylist(Playlist):
   for i in Playlist:
      input(f"Tocando: {i}, para pular pressione enter!")


def acesso_musicas_salvas():
   while True:
         #O seguinte caso só ocorrerá caso não haja músicas salvas
         if len(musicas_salvas) == 0:
            print("Você não possui músicas salvas")
            primeira_musica = input("Caso deseje adicionar uma música nova escreva o nome da múscia caso contrario pressione enter: ")
            if primeira_musica != "":
               salvar_musica(primeira_musica)
         else:
            print(f"Suas músicas salvas são: {musicas_salvas}")
            ouvir = input("Você deseja ouvir suas músicas salvas? ")
            if ouvir == "sim":
               escutarPlaylist(musicas_salvas)
         break
   
def criar_playlists(nome_playlist):
   playlists.append(nome_playlist)
   nome_playlists.append(nome_playlist)
   print(f"Playlist {nome_playlist} adicionada com sucesso.")

def adicionar_musica(nome_musica, nome_playlist):
   for playlist in playlists:
         if playlist[0] == nome_playlist:
            playlist[1].append(nome_musica) 
            print(f"Música '{nome_musica}' adicionada à playlist '{nome_playlist}'.")

def acesso_playlists():
   while True:
      if len(playlists) == 0:
         playlists0 = input("Você não possui playlists, deseja adicionar? (sim/não) ")
         if playlists0 == "sim":
            primeira_playlist = input("Digite sua primeira playlist: ")
            criar_playlists(primeira_playlist)
         
         print(f"Suas playlists são: {nome_playlists}")
         menu_playlists = int(input("""O que você deseja fazer:
1.Criar uma nova playlist
2.Escutar uma playlist
3.Sair"""))
         if menu_playlists == 1:
            nova_play = input("Digite sua nova playlist: ")
            criar_playlists(nova_play)
         elif menu_playlists == 2:
            playlist_escutar = input("Digite o nome da playlist a ser escutada: ")
            escutarPlaylist(playlist_escutar)
         elif menu_playlists == 3:
            sair = input("Você tem certeza que deseja sair? (sim/não) ")
            if sair == "sim":
               break