# Solicitar os dados do aluno
media = float(input("Informe a nota média do aluno: ").replace(',', '.'))
presenca = float(input("Informe a porcentagem de presença do aluno: ").replace(',', '.'))

# Verificar os critérios
apto_nota = media >= 7.0
apto_presenca = presenca >= 75.0

# Verificar elegibilidade e exibir resultado
if apto_nota and apto_presenca:
    print("O aluno está apto a participar da competição de robótica!")
else:
    motivos = []
    if not apto_nota:
        motivos.append("nota média")
    if not apto_presenca:
        motivos.append("presença")
    
    print("O aluno não está apto a participar da competição.")
    
    if len(motivos) == 1:
        print(f"CRITÉRIO NÃO ATENDIDO: {motivos[0]}")
    else:
        print(f"CRITÉRIOS NÃO ATENDIDOS: {' e '.join(motivos)}")