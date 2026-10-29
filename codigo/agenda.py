import calendar
from datetime import datetime
import os
import json
class agenda():
    def __init__(self,hoje=None,ano=2026,mes=9,semanas=None,ARQUIVO=None):
        self.hoje = hoje
        self.ano = ano
        self.mes = mes
        self.semanas = calendar.monthcalendar(ano,mes)
        self.ARQUIVO = 'Lifedesk_e_funcionalidade/data/agenda.json'
    def mostrar_calendario(self):
                dias_com_compromisso = []
                os.system('cls' if os.name == 'nt' else 'clear')
                self.semanas = calendar.monthcalendar(self.ano, self.mes)
                try:
                    with open(self.ARQUIVO, 'r', encoding='utf-8') as arquivo:
                        self.compromissos = json.load(arquivo)
                except (FileNotFoundError, json.JSONDecodeError):
                    self.compromissos = []
                for compromisso in self.compromissos:
                    data = datetime.strptime(
                    compromisso['data'],
                    '%d/%m/%Y'
                    )
                    if data.month == self.mes and data.year == self.ano:
                        dias_com_compromisso.append(data.day)
                print(f'\n        📅 {calendar.month_name[self.mes]} {self.ano}\n')
                print('SEG  TER  QUA  QUI  SEX  SAB  DOM')
                for semana in self.semanas:
                    for dia in semana:
                        if dia == 0:
                            print('    ', end=' ')
                        elif dia in dias_com_compromisso:
                            print(' X  ', end=' ')
                        else:
                            print(f'{dia:02}  ', end=' ')
                    print()

    def marcar_compromisso(self):
        self.nome = input('Qual é o compromisso:  ')
        print()
        self.dia = int(input('Escolha o dia: '))
        print()
        self.semanas = calendar.monthcalendar(
        self.ano, self.mes
    )    
        for semana in self.semanas:
            for dia in semana:
                if dia == self.dia:
                    print(' X ', end=' ')
                elif dia == 0:
                    print('    ', end=' ')
                else:
                    print(f'{dia:02}', end='   ')
            print()
        self.data = (
        f'{self.dia:02}/{self.mes:02}/{self.ano}'
    )
        while True:
            self.horario = input('Horário (HH:MM): ')
            try:
                datetime.strptime(self.horario, '%H:%M')
                break
            except ValueError:
                print('❌ Digite o horário no formato HH:MM!')
                print()
        self.local = input('Local: ')
        self.compromisso = {
        'nome': self.nome,
        'data': self.data,
        'horario': self.horario,
        'local': self.local
    }
        with open(self.ARQUIVO, 'r', encoding='utf-8') as arquivos:
            self.compromissos = json.load(arquivos)
        self.compromissos.append(self.compromisso)
        with open(self.ARQUIVO, 'w', encoding='utf-8') as arquivos:
            json.dump(
            self.compromissos,
            arquivos,
            ensure_ascii=False,
            indent=4
        )
        print('✅ Compromisso cadastrado!')

    def excluir_compromisso(self):
        with open(self.ARQUIVO,'r',encoding='utf-8') as arquivos:
            self.compromissos = json.load(arquivos)
        for numero, compromisso in enumerate(self.compromissos, start=1):
            print(f"[{numero}] {compromisso['nome']}")
            print()
        self.sorn = str(input('Você deseja excluir alguma dessas tarefas [S/N]  '))
        print()
        if self.sorn.lower() == 's':
            print()
            self.opcao = int(input('Qual tarefa você deseja excluir? '))
            print()
            compromisso = self.compromissos[self.opcao -1]
            self.compromissos.pop(self.opcao - 1)
            with open(self.ARQUIVO,'w',encoding='utf-8') as arquivos:
                json.dump(self.compromissos,arquivos,indent=4,ensure_ascii=False)
                print()
                print(f'Tarefa {compromisso["nome"]} excluído com sucesso!')
                print()
                input('\nPressione ENTER para continuar...')
    def mostrar(self):
        with open(self.ARQUIVO, 'r', encoding='utf-8') as arquivo:
            self.compromissos = json.load(arquivo)
        if not self.compromissos:
            print("Nenhum compromisso cadastrado.")
            return
        for numero, compromisso in enumerate(self.compromissos, start=1):
            print(f"[{numero}] {compromisso['nome']}")
        self.opcao = input("Qual compromisso deseja ver completo: ")
        if not self.opcao.isdigit():
            print("Digite um número válido!")
            return
        self.opcao = int(self.opcao)
        if self.opcao < 1 or self.opcao > len(self.compromissos):
            print("Opção inválida!")
            return
        compromisso = self.compromissos[self.opcao - 1]
        print("\n===== COMPROMISSO =====")
        print()
        print(f"Nome: {compromisso['nome']}")
        print(f"Data: {compromisso['data']}")
        print(f"Horário: {compromisso['horario']}")
        print(f"Local: {compromisso['local']}")
        print(f"Descrição: {compromisso['descricao']}")


    def interface(self):
        print()
        print('[1] Próximo mês')
        print('[2] Mês anterior')
        print('[3] Escolher dia')
        print('[4] Excluir compromisso')
        print('[5] mostrar compromissos')
        print('[0] Voltar')
        print()

    def calendario(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.mostrar_calendario()
            print()
            self.interface()
            self.opcao =int(input(': '))
            if self.opcao == 1:
                self.mes += 1
                if self.mes > 12:
                   self.mes =1
                   self.ano +=1

            elif self.opcao == 2:
                self.mes -= 1                                
                if self.mes > 12:
                    self.mes =1
                    self.ano +=1
            elif self.opcao == 3:
                self.marcar_compromisso()
            elif self.opcao == 4:
                self.excluir_compromisso()
            elif self.opcao == 5:
                self.mostrar()
                input('\nPressione ENTER para continuar...')
            else:
                print("❌ Opção inválida! Tente novamente.")

app = agenda(hoje=None,ano=2026,mes=9,semanas=52)
app.calendario()