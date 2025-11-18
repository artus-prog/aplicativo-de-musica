arquivo = open("arquivos_salvos.txt", "a")

nome_playlists = []
playlists = []
musicas_salvas=[]
usuario = ""
senha = ""

#Está função tem relações com as funções login_entrar e primeiro_acesso
#A função desta é organizar os protocolos de login
def login():
   login_inicial=input("Você está acessando este aplicativo pela primeira vez? (sim/não)").strip().lower()

   if login_inicial == "sim":
      primeiro_acesso()
      return False

   elif login_inicial in ("não,nao"):
      login_entrar()
   else:
      print("Resposta inválida!")
      return False

#A seguinte função serve para o caso de
#o usuario estar fazendo seu primeiro acesso
def primeiro_acesso():
   usuario=input("Qual nome de usúario você deseja? ")
   senha=input("Digite a senha desejada: ")
   print(f"Seu nome de usuário é: {usuario} e sua senha é: {senha}")
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
def salvar_musica():
   escolha = input("Você deseja adicionar uma música a sua lista de músicas salvas? ").strip().lower()
   if escolha == "sim":
      musica_nova = input("Digite o nome da sua música nova e o autor seguindo o seguinte modelo: Amor Bandido-Oruam. ")
      musicas_salvas.append(musica_nova)
      print(f"Você adicionou: {musica_nova} as suas músicas salvas")
   elif escolha == "nao" or escolha == "não":
      print("Ok")
   else:
      ("Opção inválida")
   print(f"Suas músicas salvas são: {musicas_salvas}")
def nova_playlist():
      nova_playlist=bool(input("Você deseja adicionar uma nova playlist?"))
      
      if nova_playlist==True:
         nome_playlist=input("Digite o nome da sua nova playlist: ")
         playlists.append(nome_playlist)

def main_site():
   login()
   print("""___MENU___
1. Acessar músicas salvas
2. Acessar suas playlists 
""")
   escolha = int(input("O que deseja fazer: "))
   if escolha == 1:
      if len(musicas_salvas) == 0:
         print("Você não possui músicas salvas")
         salvar_musica()



while True:
   print("Bem vindo a sla aplicativo de música")
   main_site()
   break