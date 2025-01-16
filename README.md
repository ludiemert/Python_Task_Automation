# Automate Tasks with PyAutoGUI 🚀

Welcome to **Automate Tasks with PyAutoGUI**, a powerful Python script designed to streamline repetitive tasks and boost productivity. With this script, you can automate actions such as navigating websites, logging in, and handling data with ease.

---

## 🌟 Features

- **Open and Navigate Systems**: Automates browser navigation to specified URLs.
- **Perform Automated Logins**: Handles email and password inputs.
- **Data Integration**: Reads and processes CSV files using Pandas.
- **Dynamic Automation**: Iteratively fills forms with data from a database.
- **User-Friendly Adjustments**: Includes delays to handle loading times effectively.

---

## 📂 How It Works

This script leverages the capabilities of:
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)**: For screen automation (mouse clicks, typing, and more).
- **[Pandas](https://pandas.pydata.org/)**: To handle and process CSV data files.

### Workflow Overview:
1. **Access the System**:
   - Opens a browser and navigates to the desired website.
2. **Automate Login**:
   - Automatically inputs credentials and logs into the system.
3. **Data Processing**:
   - Reads product data from a CSV file.
4. **Form Filling**:
   - Iterates through each product and fills the corresponding form fields.
5. **Submission**:
   - Submits the data and scrolls to refresh the interface for the next entry.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Installed libraries:
  ```bash
  pip install pyautogui pandas openpyxl
  ```

---

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ludiemert/Python_Task_Automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd automate-tasks-pyautogui
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

### Running the Script
1. Make sure you have a CSV file named `produtos.csv` in the same directory as the script.
2. Execute the script:
   ```bash
   python automate_tasks.py
   ```

### CSV File Format
Ensure your `produtos.csv` includes the following columns:
- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

### Example CSV:
```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
12345,BrandX,Electronics,Accessories,99.99,60.00,Special offer
...
```

---

## ⚙️ Configuration

- **Adjust Mouse Coordinates**:
   Update the `x` and `y` positions in the script to match your screen layout.
- **Custom Delays**:
   Modify the `time.sleep()` values to suit your internet or system speed.

---

### Portugues
# 🛠️ Automação com PyAutoGUI

Bem-vindo ao repositório **Automação com PyAutoGUI**, onde a magia da automação transforma tarefas manuais em processos rápidos e eficientes! Este projeto foi desenvolvido para automatizar interações com sistemas baseados em interface gráfica, usando o poder do Python e da biblioteca PyAutoGUI.

---

## 🚀 Funcionalidades

- **Automatização de login:** Efetue login automaticamente em sistemas e sites com credenciais pré-definidas.
- **Importação de dados:** Integre e manipule arquivos CSV utilizando a biblioteca `pandas`.
- **Cadastro automatizado:** Insira dados em sistemas com base em arquivos de entrada, simulando interações humanas precisas.

---

## 🧰 Pré-requisitos

Certifique-se de que você tenha os seguintes itens instalados no seu ambiente:

- Python 3.x
- Biblioteca PyAutoGUI
- Biblioteca pandas (`pip install pandas openpyxl`)

---

## 🛠️ Como usar

1. Clone o repositório:
   ```bash
    git clone https://github.com/ludiemert/Python_Task_Automation.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python automacao.py
   ```
4. Certifique-se de ajustar as coordenadas de clique e o caminho dos arquivos CSV no código conforme necessário.


---

- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

## 🌐 **Contact**
<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

---
Developed with ❤ by [ludiemert](https://github.com/ludiemert).

🎉 Happy automating!

