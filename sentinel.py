import re
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import atheris
import os
import magic
import subprocess

supported_extensions = ['.py', '.java', '.c', '.cpp', '.rb', '.js', '.html', '.php']

path = "/caminho/do/diretorio"

supported_files = []
for dirpath, _, filenames in os.walk(path):
    for filename in filenames:
        file_ext = os.path.splitext(filename)[1]
        if file_ext in supported_extensions:
            supported_files.append(os.path.join(dirpath, filename))

if not supported_files:
    print("Nenhum arquivo encontrado para escanear.")
else:
    for file in supported_files:
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file)

        if file_type.startswith('text/'):
            subprocess.run(['bandit', '-r', '-ll', '-ii', '-s', 'B104', file])
        else:
            print(f"Não é possível escanear o arquivo {file}, pois não é um arquivo de texto.")

def find_code_injection_vulnerabilities(code):
    pattern = r'eval\s*\(|exec\s*\(|os\.system\s*\(|subprocess\.run\s*\(|\$\(|`.*`'

    matches = re.finditer(pattern, code)

    vulnerabilities = []

    for match in matches:
        vulnerability = {
            'type': 'Code Injection',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)

    return vulnerabilities


def find_xss_vulnerabilities(code):
    pattern = r'<script>.*</script>|<img.*src=.*onerror=.*>'

    matches = re.finditer(pattern, code)

    vulnerabilities = []

    for match in matches:
        vulnerability = {
            'type': 'XSS (Cross-Site Scripting)',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)

    return vulnerabilities

def find_sql_injection_vulnerabilities(code):
    pattern = r'SELECT\s+\*|DROP\s+TABLE|DELETE\s+FROM'

    matches = re.finditer(pattern, code, re.IGNORECASE)

    vulnerabilities = []

    for match in matches:
        vulnerability = {
            'type': 'SQL Injection',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)

    return vulnerabilities

def find_vulnerabilities(code):
    vulnerabilities = []

    vulnerabilities += find_code_injection_vulnerabilities(code)

    vulnerabilities += find_xss_vulnerabilities(code)

    vulnerabilities += find_sql_injection_vulnerabilities(code)

    return vulnerabilities

def fuzz_code(code):

    for _ in range(10):  
        with atheris.Mutator() as mutator:
            test_case = mutator.fuzz()
            vulnerabilities = find_vulnerabilities(test_case)
            if vulnerabilities:
                print("Vulnerabilidades encontradas:")
                for vulnerability in vulnerabilities:
                    print("- Tipo:", vulnerability['type'])
                    print("- Padrão:", vulnerability['pattern'])
                    print("- Linha:", vulnerability['line_number'])
                print("----------------------------------------")
            else:
                print("Nenhuma vulnerabilidade encontrada.")
            print("----------------------------------------")

def open_file():

    option = simpledialog.askstring("Escolha uma opção", "1 - Analisar arquivo\n2 - Analisar programa digitado")

    if option == '1':
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                code = f.read()
                vulnerabilities = find_vulnerabilities(code)
                if vulnerabilities:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"Vulnerabilidades encontradas no arquivo: {file_path}\n")
                    for vulnerability in vulnerabilities:
                        result_text.insert(tk.END, f"- Tipo: {vulnerability['type']}\n")
                        result_text.insert(tk.END, f"- Padrão: {vulnerability['pattern']}\n")
                        result_text.insert(tk.END, f"- Linha: {vulnerability['line_number']}\n")
                    result_text.insert(tk.END, "----------------------------------------\n")
                else:
                    result_text.delete(1.0, tk.END)
                    result_text.insert(tk.END, f"Nenhuma vulnerabilidade encontrada no arquivo: {file_path}\n")
                    result_text.insert(tk.END, "----------------------------------------\n")
    elif option == '2':
        code = simpledialog.askstring("Analisar programa digitado", "Digite o programa:")
        if code:
            vulnerabilities = find_vulnerabilities(code)
            if vulnerabilities:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Vulnerabilidades encontradas no programa:\n")
                for vulnerability in vulnerabilities:
                    result_text.insert(tk.END, f"- Tipo: {vulnerability['type']}\n")
                    result_text.insert(tk.END, f"- Padrão: {vulnerability['pattern']}\n")
                    result_text.insert(tk.END, f"- Linha: {vulnerability['line_number']}\n")
                result_text.insert(tk.END, "----------------------------------------\n")
            else:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Nenhuma vulnerabilidade encontrada no programa.\n")
                result_text.insert(tk.END, "----------------------------------------\n")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Opção inválida.\n")


window = tk.Tk()
window.title("Code Sentinel")
window.geometry("500x500")
window.configure(bg="#1c2936")  

image = Image.open("img/sentinela.png")
image = image.convert("RGBA")
data = image.getdata()
new_data = []
for item in data:

    if item[:3] == (255, 255, 255):
        new_data.append((255, 255, 255, 0))  
    else:
        new_data.append(item)
image.putdata(new_data)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(window, image=photo, bg="#1c2936")
image_label.image = photo
image_label.pack(pady=10)  

style = ThemedStyle(window)
style.set_theme("clam")

style = ttk.Style(window)
style.configure("TButton",
                background="black",
                foreground="white",
)

file_button = ttk.Button(window, text="Anexar Arquivo", command=open_file, style="TButton")
file_button.pack()

result_text = tk.Text(window)
result_text.pack()

window.mainloop()