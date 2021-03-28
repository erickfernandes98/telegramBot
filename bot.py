import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '1792779904:AAGUZmoiEGTc-B6jiCKH-9NWobY2Km3ZpNU'
        self.url_base = f'https://api.telegram.org/bot{token}/'
    # Iniciar o Bot
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem.lower() == 'lojas':
            return f'''Olá bem vindo ao Yummy! Digite a loja que deseja ver o cardápio:{os.linesep}1 - Império Doces{os.linesep}2 - Vida Doce{os.linesep}3 - Doce Magia{os.linesep}4 - Central Doces{os.linesep}5 - Doces Vaz'''
        if mensagem == '1':
            return f'''Aqui está o cardápio da loja, para comprar basta acessar www.yummy.com.br! Aproveite :){os.linesep}- Bolo de leite ninho com chocolate - R$15,00{os.linesep}- Bolo de morango - R$ 15,00{os.linesep}- Mousse de chocolate - R$ 10,00{os.linesep}- Torta de limão - R$ 13,00{os.linesep}- Pudim - R$ 8,00'''
        elif mensagem == '2':
            return f'''Aqui está o cardápio da loja, para comprar basta acessar www.yummy.com.br! Aproveite :){os.linesep}- Mousse de Nutella - R$15,00{os.linesep}- Mousse de limão - R$ 12,00{os.linesep}- Sorvete de morango - R$ 6,00{os.linesep}- Bolo prestígio - R$ 10,00{os.linesep}- Torta de frutas vermelhas - R$ 8,00'''
        elif mensagem == '3':
            return f'''Aqui está o cardápio da loja, para comprar basta acessar www.yummy.com.br! Aproveite :){os.linesep}- Torta de chocolate vegana - R$15,00{os.linesep}- Torta de chocolate - R$ 12,00{os.linesep}- Torta Oreo - R$ 12,00{os.linesep}- Cheesecake de doce de leite - R$ 10,00{os.linesep}- Cheesecake de chocolate - R$ 10,00'''
        elif mensagem == '4':
            return f'''Aqui está o cardápio da loja, para comprar basta acessar www.yummy.com.br! Aproveite :){os.linesep}- Cheesecake de maracujá - R$10,00{os.linesep}- Verrine de framboesa - R$ 13,00{os.linesep}- Docinho de Leite Ninho - R$ 12,00{os.linesep}- Cheesecake de doce de leite - R$ 10,00{os.linesep}- Cheesecake de chocolate - R$ 10,00'''
        elif mensagem == '5':
            return f'''Aqui está o cardápio da loja, para comprar basta acessar www.yummy.com.br! Aproveite :){os.linesep}- Beijinho - R$5,00{os.linesep}- Paleta Mexicana - R$ 7,00{os.linesep}- Sorvete de Nutella - R$ 9,00{os.linesep}- Pavê de chocolate e morango - R$ 10,00{os.linesep}- Pavê trufado - R$ 10,00'''
        else:
            return 'Gostaria de verificar o cardápio das lojas? Digite "lojas"'
    # Enviar Mensangem(responder)
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)

bot = TelegramBot() #Inicializando o bot
bot.Iniciar() # Chamando a função Iniciar