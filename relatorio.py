import tkinter as Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def exportar_para_pdf():
    pdf_file = "conteudo_exportado.pdf"

    with PdfPages(pdf_file) as pdf:

        fig,ax = plt.subplots()
        ax.plot( [1,2,3,4] , [1,4,2,3])
        ax.set_xlabel('X')
        ax.set_ylabel('y')
        ax.set_title('gráfico de exemplo')
        pdf.savefig(fig)
        plt.close(fig)

    print("PDF exportado com sucesso.")

root = Tk.Tk()
root.title("exportar para PDF")

botao_exportar = Tk.Button(root,text = "exportar grafico para PDF", command=exportar_para_pdf)
botao_exportar.pack()

root.mainloop()