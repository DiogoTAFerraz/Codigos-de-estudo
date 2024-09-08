from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Dados do aplicativo
funcionarios = {
    "1": "Sergio",
    "2": "Felipe",
    "3": "Roberval",
    "4": "Diogo",
    "5": "Matheus",
    "6": "Bruno",
    "7": "Caio",
    "8": "Gustavo",
    "9": "Maurizete"
}

while True:
    numero = input("\nInforme o número do funcionário (ou 'sair' para encerrar): ")
    if numero.lower() == 'sair':
        break

    nome_do_funcionario = funcionarios.get(numero, "Funcionário não encontrado")
    valor_do_vale = float(input("Informe o valor do vale: R$ "))

    # Obtendo a data atual
    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Criando o PDF
    c = canvas.Canvas(f"vale_{numero}.pdf", pagesize=letter)
    width, height = letter

    c.drawString(100, height - 50, "Posto Estação BH")
    c.drawString(100, height - 100, f"Vale preenchido em nome de {nome_do_funcionario}")
    c.drawString(100, height - 120, f"Valor do vale: R$ {valor_do_vale:.2f}")
    c.drawString(100, height - 140, f"Data: {data_atual} Belo Horizonte, Minas Gerais")
    c.drawString(100, height - 180, "Assinatura do funcionário:")
    c.line(100, height - 200, 300, height - 200)

    c.save()

    print("\nPDF gerado com sucesso!")

print("Programa encerrado.")