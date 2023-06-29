import re
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import atheris
import os
import logging

logging.basicConfig(level=logging.INFO)

supported_extensions = ['.py', '.java', '.javascript', '.c', '.cpp', '.rb', '.js', '.html', '.php']

class CodeSentinel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Code Sentinel")
        self.window.geometry("700x650")
        self.window.configure(bg="#1c2936")
        self.result_text = tk.Text(self.window)
        self.result_text.pack()

        self.style = ThemedStyle(self.window)
        self.style.set_theme("clam")
        self.style = ttk.Style(self.window)
        self.style.configure("TButton",
                             background="black",
                             foreground="white",
                             )
        self.file_button = ttk.Button(self.window, text="Anexar Arquivo", command=self.open_file, style="TButton")
        self.file_button.pack()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "img/sentinela.png")
        self.image = Image.open(image_path)
        self.image = self.image.convert("RGBA")
        data = self.image.getdata()
        new_data = []
        for item in data:
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        self.image.putdata(new_data)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = tk.Label(self.window, image=self.photo, bg="#1c2936")
        self.image_label.image = self.photo
        self.image_label.pack(pady=10)

    def open_file(self):
        option = simpledialog.askstring("Escolha uma opção", "1 - Analisar arquivo")
        if option == '1':
            file_path = filedialog.askopenfilename()
            if file_path:
                with open(file_path, "r") as f:
                    code = f.read()
                    vulnerabilities = self.find_vulnerabilities(code)
                    if vulnerabilities:
                        self.display_vulnerabilities(file_path, vulnerabilities)
                    else:
                        self.display_no_vulnerabilities(file_path)

    def display_vulnerabilities(self, file_path, vulnerabilities):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Vulnerabilidades encontradas no arquivo: {file_path}\n")
        for vulnerability in vulnerabilities:
            self.result_text.insert(tk.END, f"- Tipo: {vulnerability['type']}\n")
            self.result_text.insert(tk.END, f"- Padrão: {vulnerability['pattern']}\n")
            self.result_text.insert(tk.END, f"- Linha: {vulnerability['line_number']}\n")
        self.result_text.insert(tk.END, "----------------------------------------\n")

    def display_no_vulnerabilities(self, file_path):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Nenhuma vulnerabilidade encontrada no arquivo: {file_path}\n")
        self.result_text.insert(tk.END, "----------------------------------------\n")

    def find_code_injection_vulnerabilities(self, code):
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

    def find_xss_vulnerabilities(self, code):
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

    def find_sql_injection_vulnerabilities(self, code):
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

    def find_vulnerabilities(self, code):
        vulnerabilities = []
        vulnerabilities += self.find_code_injection_vulnerabilities(code)
        vulnerabilities += self.find_xss_vulnerabilities(code)
        vulnerabilities += self.find_sql_injection_vulnerabilities(code)
        return vulnerabilities

    def fuzz_code(self, code):
        for _ in range(10):
            with atheris.Mutator() as mutator:
                test_case = mutator.fuzz()
                vulnerabilities = self.find_vulnerabilities(test_case)
                if vulnerabilities:
                    logging.info("Vulnerabilidades encontradas:")
                    for vulnerability in vulnerabilities:
                        logging.info("- Tipo:", vulnerability['type'])
                        logging.info("- Padrão:", vulnerability['pattern'])
                        logging.info("- Linha:", vulnerability['line_number'])
                    logging.info("----------------------------------------")
                else:
                    logging.info("Nenhuma vulnerabilidade encontrada.")
                logging.info("----------------------------------------")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    sentinel = CodeSentinel()
    sentinel.run()
