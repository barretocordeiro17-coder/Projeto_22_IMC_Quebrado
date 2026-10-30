# 🐞 Caça aos Bugs: Calculadora de IMC com Streamlit

> **Situação de aprendizagem** para a prática de leitura de erros, depuração (*debugging*) e
> boas práticas em Python + Streamlit.

---

## 1. Contexto

Você acaba de entrar para a equipe de desenvolvimento de uma pequena startup de saúde digital.
Um colega, que estava com muita pressa, deixou um aplicativo de **Calculadora de IMC** quase pronto,
mas saiu de férias sem testar nada. O gestor do projeto precisa apresentar o app **amanhã** para um cliente.

Ao abrir o código, você descobre que ele está **cheio de problemas**: o app nem sobe, as contas estão
erradas, os textos têm erros de português e alguns recursos do Streamlit foram usados do jeito errado.

## 2. Desafio

> **Sua missão:** encontrar e corrigir **todos os erros** do projeto até que o aplicativo
> rode sem falhas, calcule o IMC corretamente e apresente textos revisados e profissionais.

O app possui **duas páginas**:

| Página | Arquivo | O que deve fazer |
|---|---|---|
| 📚 Entendendo o IMC | `app.py` | Explicar o que é o IMC, como se calcula e por que ele é importante |
| 🧮 Calculadora | `pages/1_Calculadora.py` | Receber nome, peso e altura e exibir o IMC e a classificação |

## 3. Objetivos de aprendizagem

Ao final da atividade, você será capaz de:

- Interpretar mensagens de erro (*traceback*) do Python e do Streamlit.
- Diferenciar erros de **sintaxe**, de **execução** e de **lógica**.
- Aplicar corretamente funções básicas do Streamlit (`st.title`, `st.number_input`, `st.columns`, etc.).
- Trabalhar com tipos de dados (`int`, `float`, `str`) e formatação de texto com *f-strings*.
- Revisar textos e interfaces, garantindo qualidade e clareza para o usuário final.
- Usar Git e GitHub para versionar o seu trabalho.

## 4. Conhecimentos necessários

- Python básico: variáveis, `if / elif / else`, operadores e *f-strings*.
- Noções de Streamlit: `st.write`, `st.button`, `st.columns` e entradas de dados.
- Noções de Git: `clone`/`fork`, `commit` e `push`.

## 5. Como executar o projeto

```bash
# 1. Clone (ou faça fork e clone) o repositório
git clone <URL-DO-REPOSITORIO>
cd imc-debug-streamlit

# 2. (Opcional, recomendado) crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode o aplicativo
streamlit run app.py
```

O navegador abrirá em `http://localhost:8501`. Se o app não abrir, **comece pelo terminal**:
a primeira pista sempre está lá. 😉

## 6. Estrutura do projeto

```
imc-debug-streamlit/
├── app.py                  # Página 1: o que é o IMC e sua importância
├── pages/
│   └── 1_Calculadora.py    # Página 2: calculadora de IMC
├── requirements.txt        # Dependências
└── README.md               # Este arquivo
```

## 7. Roteiro sugerido

1. **Reconheça o terreno:** leia os dois arquivos sem executar nada e anote o que parece estranho.
2. **Execute e leia o erro:** rode `streamlit run app.py` e leia a mensagem de cima para baixo.
3. **Corrija um erro por vez:** salve, rode de novo e veja se surgiu outro. Erros costumam aparecer em cascata.
4. **Registre cada correção** na tabela do relatório de bugs (item 9).
5. **Teste a calculadora** com valores conhecidos (veja a dica de testes abaixo).
6. **Revise todos os textos** em voz alta, como se fossem ser lidos por um cliente.
7. **Faça commits pequenos** e com mensagens claras, por exemplo: `fix: corrige fórmula do IMC`.

## 8. Dicas (sem spoilers!)

**Tipos de problema que você vai encontrar:**

| Tipo | Como se manifesta |
|---|---|
| 🧱 Sintaxe | O Python nem consegue começar a executar o arquivo |
| 💥 Execução | O app abre, mas quebra com uma mensagem vermelha |
| 🧠 Lógica | O app roda sem quebrar, porém **o resultado está errado** |
| 🎨 Interface | Algo aparece torto, faltando ou com rótulo incoerente |
| ✍️ Português | Acentos, ortografia, pontuação e concordância |

**Perguntas que ajudam:**

- Esse nome de função existe mesmo? Como está escrito na documentação do Streamlit?
- Toda biblioteca que estou usando foi importada?
- Os tipos dos valores são compatíveis entre si? (O que acontece ao somar texto com número?)
- A unidade que o usuário vê (cm, m, kg) é a mesma que a conta usa?
- A fórmula bate com a que está escrita na página de explicação?
- Os intervalos de classificação cobrem **todos** os valores possíveis, sem se repetirem?
- Todos os arquivos e caminhos citados no código existem de verdade?

**Teste de mesa para validar a calculadora:**

| Peso (kg) | Altura (m) | IMC esperado | Classificação esperada |
|---|---|---|---|
| 50 | 1,70 | ≈ 17,3 | Abaixo do peso |
| 70 | 1,75 | ≈ 22,9 | Peso normal |
| 85 | 1,75 | ≈ 27,8 | Sobrepeso |
| 110 | 1,75 | ≈ 35,9 | Obesidade |

**Links úteis:**

- Documentação do Streamlit: <https://docs.streamlit.io>
- Referência da API: <https://docs.streamlit.io/develop/api-reference>
- Como ler um traceback em Python: <https://docs.python.org/pt-br/3/tutorial/errors.html>

## 9. Entrega: Relatório de bugs

Ao terminar, crie um arquivo `RELATORIO.md` na raiz do seu repositório com uma tabela neste formato:

| # | Arquivo | Linha | Tipo de erro | O que estava errado | Como corrigi |
|---|---|---|---|---|---|
| 1 | `app.py` | 6 | Sintaxe | (exemplo) | (exemplo) |

Depois, envie o link do seu repositório (ou do *pull request*) ao professor.

## 10. Critérios de avaliação

| Critério | Pontos |
|---|---|
| O aplicativo executa sem nenhum erro nas duas páginas | 3 |
| O cálculo e a classificação do IMC estão corretos nos testes de mesa | 2 |
| Textos revisados (ortografia, acentuação e pontuação) | 2 |
| Relatório de bugs claro e completo | 2 |
| Histórico de *commits* organizado | 1 |
| **Total** | **10** |

### ⭐ Desafios extras (opcionais)

- Impedir o cálculo quando o campo de nome estiver vazio.
- Mudar a cor da mensagem conforme a classificação (`st.success`, `st.warning`, `st.error`).
- Exibir a faixa de peso ideal para a altura informada.
- Adicionar uma imagem com a tabela de IMC na página explicativa.
- Publicar o app no [Streamlit Community Cloud](https://streamlit.io/cloud).

## 11. Aviso

Projeto com fins **exclusivamente educacionais**. O IMC é apenas um indicador de triagem e
**não substitui a avaliação de um profissional de saúde**.

---

*Boa caçada! 🔎🐛*
