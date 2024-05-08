hora = float (input("quanto você ganha por hora:"))
horaD = float(input("quantas horas você trabalha por dia:"))

salarioD = hora * horaD
salarioM = salarioD * 30
horaRD = 24 - horaD
horaRM = horaRD * 30
print("O seu salário diário é:", salarioD)
print("O seu salário mensal é aproximadamente:",salarioM)
print("Suas horas de sobra diárias são:",horaRD)
print("Suas horas de sobra mensais são:",horaRM)
