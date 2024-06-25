import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import img2pdf

def convert_jpg_to_pdf(jpg_files):
    for jpg_file in jpg_files:
        if not os.path.isfile(jpg_file):
            print(f"Arquivo {jpg_file} não encontrado!")
            continue

        # Define o nome do arquivo PDF
        pdf_file = os.path.splitext(jpg_file)[0] + ".pdf"

        try:
            # Abre a imagem JPG
            image = Image.open(jpg_file)
            # Converte a imagem para RGB (necessário para alguns formatos)
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            
            # Salva a imagem como PDF
            with open(pdf_file, "wb") as f:
                f.write(img2pdf.convert(image.filename))
            print(f"Conversão de {jpg_file} para {pdf_file} concluída com sucesso.")
            
            # Abre o arquivo PDF convertido
            os.startfile(pdf_file)
        except Exception as e:
            print(f"Falha na conversão de {jpg_file} para {pdf_file}: {e}")

def select_files():
    filetypes = [("JPEG files", "*.jpg"), ("All files", "*.*")]
    files = filedialog.askopenfilenames(title="Escolha os arquivos JPEG", filetypes=filetypes)
    if files:
        convert_jpg_to_pdf(files)
        messagebox.showinfo("Conversão Concluída", "Os arquivos foram convertidos com sucesso. Os PDFs serão abertos em seguida.")

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    
    # Mensagem de boas-vindas
    messagebox.showinfo("Bem-vindo", "Olá! Selecione os arquivos JPEG que deseja converter para PDF.")
    
    while True:
        # Selecionar arquivos para conversão
        select_files()
        
        # Perguntar ao usuário se deseja realizar outra conversão
        if not messagebox.askyesno("Continuar", "Deseja converter mais arquivos?"):
            break

    root.destroy()  # Fechar a aplicação

if __name__ == "__main__":
    main()
