import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

class CalculadoraTrabalhista:
    """Encapsula a lógica de negócio dos cálculos de rescisão."""
    
    def __init__(self, nome, salario, saldo_fgts, admissao, demissao):
        self.nome = nome
        self.salario = salario
        self.saldo_fgts = saldo_fgts
        self.admissao = admissao
        self.demissao = demissao

    def calcular_rescisao(self):
        # 1. Saldo de Salário (Dias trabalhados no mês de saída)
        dias_mes_saida = self.demissao.day
        saldo_salario = (self.salario / 30) * dias_mes_saida

        # 2. 13º Proporcional (Considera meses cheios e fração >= 15 dias)
        meses_13 = self.demissao.month - 1
        if self.demissao.day >= 15:
            meses_13 += 1
        valor_13 = (self.salario / 12) * meses_13

        # 3. Férias Proporcionais + 1/3 (Uso do relativedelta)
        delta = relativedelta(self.demissao, self.admissao)
        total_meses_trabalhados = (delta.years * 12) + delta.months
        
        # Regra de 1/12 (fração superior a 14 dias)
        if delta.days >= 15:
            total_meses_trabalhados += 1
        
        valor_ferias = (self.salario / 12) * total_meses_trabalhados
        terco_ferias = valor_ferias / 3

        # 4. Multa FGTS (40%)
        multa_fgts = self.saldo_fgts * 0.40

        total_bruto = saldo_salario + valor_13 + valor_ferias + terco_ferias + multa_fgts

        return {
            "Funcionário": self.nome,
            "Saldo Salário": round(saldo_salario, 2),
            "13º Proporcional": round(valor_13, 2),
            "Férias + 1/3": round(valor_ferias + terco_ferias, 2),
            "Multa FGTS (40%)": round(multa_fgts, 2),
            "TOTAL A RECEBER": round(total_bruto, 2)
        }

def capturar_data(rotulo):
    """Função auxiliar para validar entradas de data e evitar repetição de código."""
    print(f"\n--- {rotulo} ---")
    try:
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        return date(ano, mes, dia)
    except ValueError:
        print("❌ Erro: Data inválida. Use apenas números.")
        return None

if __name__ == "__main__":
    print("="*40)
    print(f"{'SISTEMA DE RESCISÃO JÚNIOR':^40}")
    print("="*40)

    try:
        nome = input("1. Nome do funcionário: ").strip()
        salario = float(input("2. Salário base (R$): "))
        fgts = float(input("3. Saldo FGTS (R$): "))

        dt_adm = capturar_data("DATA DE ADMISSÃO")
        dt_dem = capturar_data("DATA DE DEMISSÃO")

        if dt_adm and dt_dem:

            calculadora = CalculadoraTrabalhista(nome, salario, fgts, dt_adm, dt_dem)
            resumo = calculadora.calcular_rescisao()

            # Exibição profissional dos dados
            print("\n" + "-"*40)
            print(f"{'EXTRATO RESCISÓRIO':^40}")
            print("-"*40)
            for campo, valor in resumo.items():
                if campo == "Funcionário":
                    print(f"{campo:.<25}: {valor}")
                else:
                    print(f"{campo:.<25}: R$ {valor:>10}")
            print("-"*40)

    except ValueError:
        print("\n❌ Erro: Insira valores numéricos válidos (ex: 1618,00).")
    except Exception as e:
        print(f"\n⚠️ Ocorreu um erro inesperado: {e}")