import re
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import atheris
import os
import logging
import time

logging.basicConfig(level=logging.INFO)

supported_extensions = ['.py', '.java', '.js', '.c', '.cpp', '.rb', '.js', '.html', '.php']

class CodeSentinel:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Code Sentinel")
        self.window.geometry("700x650")
        self.window.configure(bg="#1c2936")

        self.result_text = tk.Text(self.window)
        self.result_text.pack(padx=10, pady=10)

        self.style = ThemedStyle(self.window)
        self.style.set_theme("clam")
        self.style = ttk.Style(self.window)
        self.style.configure("TButton",
                             background="black",
                             foreground="white",
                             )
        self.file_button = ttk.Button(self.window, text="Anexar Arquivo", command=self.analyze_file, style="TButton")
        self.file_button.pack(pady=10)

        self.loading_label = tk.Label(self.window, text="", fg="white", bg="#1c2936")
        self.loading_label.pack()

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

    def analyze_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            if self.validate_file(file_path):
                self.show_loading()
                self.window.update()

                time.sleep(2)

                with open(file_path, "r") as f:
                    code = f.read()
                    vulnerabilities = self.find_vulnerabilities(code)
                    if vulnerabilities:
                        self.display_vulnerabilities(file_path, vulnerabilities)
                    else:
                        self.display_no_vulnerabilities(file_path)

                self.hide_loading()
            else:
                self.display_error("Arquivo inválido")

    def validate_file(self, file_path):
        if os.path.isfile(file_path) and file_path.lower().endswith(tuple(supported_extensions)):
            return True
        return False

    def display_vulnerabilities(self, file_path, vulnerabilities):
        self.result_text.insert(tk.END, f"Vulnerabilidades encontradas no arquivo: {file_path}\n")
        for vulnerability in vulnerabilities:
            self.result_text.insert(tk.END, f"- Tipo: {vulnerability['type']}\n")
            self.result_text.insert(tk.END, f"- Padrão: {vulnerability['pattern']}\n")
            self.result_text.insert(tk.END, f"- Linha: {vulnerability['line_number']}\n")
        self.result_text.insert(tk.END, "----------------------------------------\n")

    def display_no_vulnerabilities(self, file_path):
        self.result_text.insert(tk.END, f"Nenhuma vulnerabilidade encontrada no arquivo: {file_path}\n")
        self.result_text.insert(tk.END, "----------------------------------------\n")

    def display_error(self, message):
        self.result_text.insert(tk.END, message, "error")
        self.result_text.insert(tk.END, "\n")

    def show_loading(self):
        self.loading_label.config(text="Analisando arquivo")
        self.window.update()
        time.sleep(0.5)

        self.loading_label.config(text="Analisando arquivo .")
        self.window.update()
        time.sleep(0.5)

        self.loading_label.config(text="Analisando arquivo . .")
        self.window.update()
        time.sleep(0.5)

        self.loading_label.config(text="Analisando arquivo . . .")
        self.window.update()
        time.sleep(0.5)


    def hide_loading(self):
        self.loading_label.config(text="")

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

    def find_csrf_vulnerabilities(self, code):
        # Implemente a detecção de vulnerabilidades CSRF aqui
        return []

    def find_ssrf_vulnerabilities(self, code):
        # Implemente a detecção de vulnerabilidades SSRF aqui
        return []

    def find_vulnerabilities(self, code):
        vulnerabilities = []
        vulnerabilities += self.find_code_injection_vulnerabilities(code)
        vulnerabilities += self.find_xss_vulnerabilities(code)
        vulnerabilities += self.find_sql_injection_vulnerabilities(code)
        vulnerabilities += self.find_csrf_vulnerabilities(code)
        vulnerabilities += self.find_ssrf_vulnerabilities(code)
        return vulnerabilities

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    sentinel = CodeSentinel()
    sentinel.run()
