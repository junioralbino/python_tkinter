# Calculadora de Idade

Aplicativo gráfico simples, feito em Python com Tkinter, para calcular a diferença entre duas datas e exibi-la em anos, meses e dias.

## Funcionalidades

- Seleção de duas datas por meio de calendários.
- Cálculo da diferença entre as datas em anos, meses e dias.
- Interface desktop com rótulos em português.

## Requisitos

- Python 3 instalado.
- Tkinter, incluído na maioria das instalações do Python. Em algumas distribuições Linux, ele precisa ser instalado separadamente.
- Bibliotecas Python:
  - `tkcalendar`
  - `python-dateutil`

## Instalação

Abra um terminal na pasta do projeto. Opcionalmente, crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install tkcalendar python-dateutil
```

No Linux ou macOS, a ativação do ambiente virtual é:

```bash
source .venv/bin/activate
```

Se o Tkinter não estiver disponível no Linux, instale o pacote correspondente à sua distribuição (por exemplo, `python3-tk` em distribuições baseadas em Debian/Ubuntu).

## Como executar

Na pasta do projeto, execute:

```powershell
python main.py
```

O comando também é o mesmo em Linux e macOS:

```bash
python main.py
```

## Como usar

1. Abra o aplicativo.
2. Escolha uma data no campo **Data Atual**.
3. Escolha outra data no campo **Data aniversario**.
4. Clique em **Calcular Idade**.
5. Consulte os valores exibidos em anos, meses e dias.

O cálculo só é atualizado quando o botão é pressionado.

## Como o cálculo funciona

O programa obtém as duas datas selecionadas e usa `dateutil.relativedelta` para calcular a diferença entre a mais recente e a mais antiga. Por isso, o resultado é sempre uma duração não negativa: a ordem das datas não altera o sinal.

Embora a interface use os nomes **Data Atual** e **Data aniversario**, o código não valida qual data representa o nascimento nem impede datas futuras. Para calcular a idade de uma pessoa, selecione a data de nascimento em um campo e a data de referência no outro; o resultado será a diferença entre elas.

## Estrutura do projeto

```text
.
├── main.py      # Interface Tkinter e lógica de cálculo
└── README.md    # Documentação do projeto
```

## Tecnologias e dependências

- **Tkinter / ttk**: janela, campos, botões e rótulos.
- **tkcalendar**: campos de seleção de data (`DateEntry`).
- **python-dateutil**: cálculo de intervalos de calendário com `relativedelta`.
- **datetime**: tipos e operações de data da biblioteca padrão do Python.

## Observação sobre a inicialização

No código atual, os dois campos `DateEntry` recebem o argumento `data_pattern`. A opção documentada pelo `tkcalendar` é `date_pattern`. Se o aplicativo apresentar erro de opção desconhecida ao iniciar, substitua `data_pattern` por `date_pattern` nas duas instanciações de `DateEntry` em `main.py`.
