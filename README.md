# Calculadora-de-rescis-es
Criei uma calculadora de rescisão de acordo com as Leis Trabalhistas do Brasil

    Título e Descrição
Calculadora de Rescisão Trabalhista (CLT)

Este script em Python automatiza o cálculo de verbas rescisórias e multa do FGTS. Ele recebe dados de entrada via terminal, processa as regras de datas da CLT e retorna um relatório financeiro.

    O que o código faz... (Explicação Técnica)
O script utiliza a biblioteca Pandas para estruturação dos dados e Dateutil para cálculos precisos de datas. O fluxo de execução é:

  Entrada de Dados: Coleta nome, salário base, saldo do FGTS e as datas de admissão/demissão.

Cálculo de Prazos (Dateutil): Utiliza relativedelta para determinar a diferença exata de meses entre a admissão e a demissão, fundamental para calcular os "avos" de férias.

Regras de Negócio (CLT):

Saldo de Salário: Proporcional aos dias trabalhados no último mês.

13º Salário: Considera meses trabalhados no ano corrente (fração igual ou superior a 15 dias conta como mês cheio).

Férias + 1/3: Calcula férias proporcionais baseadas no tempo de serviço e adiciona o terço constitucional.

Multa FGTS: Aplica 40% sobre o saldo informado.

Processamento e Saída:

Os dados são organizados em um DataFrame do Pandas.

A função calcular_tudo é aplicada linha a linha (axis=1).

O resultado final é transposto (.T) para melhor visualização vertical no terminal.
