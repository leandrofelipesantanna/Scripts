import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_image_to_pdf(image_files):
    for image_file in image_files:
        if not os.path.isfile(image_file):
            print(f"Arquivo {image_file} não encontrado!")
            continue

        # Define o nome do arquivo PDF
        pdf_file = os.path.splitext(image_file)[0] + ".pdf"

        try:
            # Abre a imagem com PIL
            with Image.open(image_file) as img:
                # Calcula o tamanho da página do PDF baseado no tamanho da imagem
                width, height = img.size
                c = canvas.Canvas(pdf_file, pagesize=(width, height))
                c.drawImage(image_file, 0, 0, width, height)
                c.save()
                print(f"Conversão de {image_file} para {pdf_file} concluída com sucesso.")

                # Abre o arquivo PDF convertido
                os.startfile(pdf_file)
        except Exception as e:
            print(f"Falha na conversão de {image_file} para {pdf_file}: {e}")
        finally:
            try:
                # Fecha o arquivo PDF se estiver aberto
                if os.path.exists(pdf_file):
                    os.close(pdf_file)
            except Exception as e:
                print(f"Falha ao fechar o arquivo PDF {pdf_file}: {e}")

def select_files():
    filetypes = [("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.tiff"), ("All files", "*.*")]
    files = filedialog.askopenfilenames(title="Escolha os arquivos de imagem", filetypes=filetypes)
    if files:
        convert_image_to_pdf(files)
        messagebox.showinfo("Conversão Concluída", "Os arquivos foram convertidos com sucesso. Os PDFs serão abertos em seguida.")

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Função para verificar se a mensagem de boas-vindas foi fechada
    def show_welcome_message():
        try:
            messagebox.showinfo("Bem-vindo", "Olá! Selecione os arquivos de imagem que deseja converter para PDF.")
            return True
        except tk.TclError:
            return False

    # Mostrar mensagem de boas-vindas
    if show_welcome_message():
        while True:
            # Selecionar arquivos para conversão
            select_files()
            
            # Perguntar ao usuário se deseja realizar outra conversão
            if not messagebox.askyesno("Continuar", "Deseja converter mais arquivos?"):
                break

    root.destroy()  # Fechar a aplicação

if __name__ == "__main__":
    main()
