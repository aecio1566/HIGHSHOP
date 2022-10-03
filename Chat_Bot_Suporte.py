import os


def processarR(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Insira sua reclamação.{os.linesep}')
        print(input('Avaliação: '))
        print(input('\nAvaliação computada com sucesso! Obrigado por ajudar no atendimento da HighShop. '))
    elif resposta == '2':
        print(f'{os.linesep}{nome} Descreva seu problema.{os.linesep}')
        print(input('Problema com compra ou devolução: '))
        print(input('\nProblema computado com sucesso! Aguarde, nossa equipe entrará em contato em breve para solucionar seu problema.'))
    elif resposta == '3':
        print(f'{os.linesep}{nome} Descreva seu problema.{os.linesep}')
        print(input('Problema com Pagamento: '))
        print(input('\nProblema computado com sucesso! Aguarde, nossa equipe entrará em contato em breve para solucionar seu problema.'))
    elif resposta == '4':
        print(f'{os.linesep}{nome} Aguarde. Nossa equipe já vai te atender!{os.linesep}')
    else:
        print('Digite 1, 2, 3 ou 4')


def start():

    print('Olá! Bem-vindo ao chat de atendimento ao cliente HighShop.')
    
    nome = input('Digite seu nome: ')
    
    email = input('Digite seu e-mail de login: ')
    while True:
        
        resposta = input(
            f'\nEstá precisando de suporte em: {os.linesep}[1] - Gostaria de fazer uma reclamação sobre um vendedor.{os.linesep}[2] - Problemas com compra ou devolulção de um produto.{os.linesep}[3] - Problemas com pagamento de uma compra.{os.linesep}[4] - Entrar em contato com um atendente online.{os.linesep}')
        
        processarR(resposta, nome)


if __name__ == '__main__':
    start()
