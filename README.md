# Primeiro Passo — Assistente Digital de Orientação para o Primeiro Emprego

## 1. Integrantes

- **Thiago Calazans Luz Nakano** — RM: 569151
- **Leticia Aiko Okano** — RM: 571988

## 2. Público-alvo e problema escolhido

O **Primeiro Passo** é um assistente digital desenvolvido para jovens que estão procurando o primeiro emprego e ainda não possuem experiência profissional.

Muitos jovens encontram dificuldades para elaborar um currículo, identificar suas habilidades, procurar oportunidades, compreender os tipos de contratação e se preparar para entrevistas de emprego.

O objetivo do projeto é oferecer orientações simples e organizadas, ajudando esse público a compreender melhor as etapas necessárias para ingressar no mercado de trabalho.

## 3. Objetivos de Desenvolvimento Sustentável (ODS)

O projeto está relacionado aos seguintes Objetivos de Desenvolvimento Sustentável da ONU:

- **ODS 4 — Educação de Qualidade:** incentivo à aprendizagem, à qualificação e à preparação dos jovens para o mercado de trabalho.
- **ODS 8 — Trabalho Decente e Crescimento Econômico:** incentivo ao acesso de jovens a oportunidades profissionais e ao trabalho digno.
- **ODS 10 — Redução das Desigualdades:** contribuição para democratizar o acesso a informações sobre oportunidades de emprego.

## 4. Funcionalidades do assistente

O Primeiro Passo possui as seguintes funcionalidades:

- Busca de orientações por meio de perguntas digitadas pelo usuário.
- Consulta de orientações organizadas por categorias.
- Apresentação de respostas, documentos necessários, locais de atendimento, fontes e datas de verificação.
- Exibição de até duas orientações alternativas relacionadas à pergunta.
- Registro dos atendimentos em arquivo JSON.
- Cálculo de indicadores de utilização.
- Exportação dos atendimentos para arquivo CSV.
- Bloqueio de perguntas que contenham possíveis dados pessoais, como endereços de e-mail ou sequências de oito ou mais números.

### Categorias disponíveis

**1. Preparação para o primeiro emprego**
- Como montar um currículo sem ter experiência profissional?
- O que colocar no currículo quando ainda não trabalhei?
- Como identificar minhas habilidades e escolher uma área profissional?
- Qual é a diferença entre Jovem Aprendiz, estágio e emprego formal?

**2. Busca por oportunidades**
- Onde encontrar vagas de primeiro emprego?
- Como cadastrar meu currículo no SINE e no Emprega Brasil?
- Como encontrar vagas de Jovem Aprendiz e estágio?

**3. Entrevistas e processos seletivos**
- Como me preparar para uma entrevista de emprego?
- Como responder às perguntas de uma entrevista quando não tenho experiência?
- Como identificar falsas vagas de emprego e evitar golpes?

## 5. Organização dos arquivos

O projeto foi desenvolvido em Python e organizado da seguinte maneira:

```text
citizen-assist-ai/
│
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
│
└── data/
    ├── base_conhecimento.json
    ├── historico.json
    └── atendimentos.csv
```

**Responsabilidade de cada arquivo:**

- `main.py`: inicia o programa e conecta as classes.
- `orientacao.py`: contém a classe Orientacao, responsável por armazenar e exibir os dados de cada orientação.
- `base_conhecimento.py`: carrega o arquivo JSON, organiza as categorias, normaliza textos e realiza a busca com pontuação.
- `assistente.py`: controla a interação com o usuário, a navegação, o histórico, os indicadores e a exportação CSV.
- `base_conhecimento.json`: armazena as orientações cadastradas.
- `historico.json`: registra os atendimentos realizados.
- `atendimentos.csv`: armazena os dados exportados para análise.

Os arquivos de histórico e CSV são gerados pelo próprio programa durante sua utilização.

## 6. Tecnologias e conceitos utilizados

- **Python:** linguagem utilizada no desenvolvimento.
- **JSON:** armazenamento das orientações e do histórico.
- **CSV:** exportação dos atendimentos.
- **Programação orientada a objetos:** organização do sistema por meio das classes Orientacao, BaseConhecimento e Assistente.
- **Expressões regulares:** identificação de possíveis dados pessoais.
- **Bibliotecas padrão do Python:** `json`, `csv`, `re`, `time`, `os`, `datetime` e `unicodedata`.

Não são necessárias bibliotecas externas para executar o projeto.

## 7. Regra de pontuação da busca

O assistente utiliza um sistema de pontuação para identificar as orientações mais relacionadas à pergunta do usuário.

Antes da comparação, os textos são normalizados: ficam em letras minúsculas, sem acentos e sem pontuação.

A pontuação funciona da seguinte maneira:

| Critério | Pontuação |
|---|---:|
| Palavra-chave encontrada na pergunta | +3 pontos |
| Palavra com pelo menos 4 letras encontrada no título | +1 ponto |

A classificação dos resultados é:

- **6 pontos ou mais:** confiança alta.
- **De 3 a 5 pontos:** confiança média.
- **Menos de 3 pontos:** orientação não encontrada.

Os resultados são organizados em ordem decrescente de pontuação. O assistente apresenta a melhor orientação encontrada e até duas alternativas.

## 8. Fontes consultadas

Foram utilizados materiais institucionais e informativos para elaborar as orientações sobre primeiro emprego, procura de vagas, qualificação profissional e prevenção de golpes.

1. **SINE Paraíba — Informações relevantes para o trabalhador:**  
   https://sine.pb.gov.br/informacoes/documentos/informacoes-relevantes-para-o-trabalhador

2. **SINE Distrito Federal — Cartilha de atendimento aos trabalhadores jovens:**  
   https://sedet.df.gov.br/documents/9170759/10185778/CARTILHA_ATENDIMENTO_TRABALHADORES_JOVENS_SINE.pdf

3. **Governo Federal — Buscar emprego no Sistema Nacional de Emprego (SINE):**  
   https://www.gov.br/pt-br/servicos/buscar-emprego-no-sistema-nacional-de-emprego-sine

4. **Ministério do Trabalho e Emprego:**  
   https://www.gov.br/trabalho-e-emprego/pt-br

5. **Ministério do Trabalho e Emprego — Sistema Nacional de Emprego (SINE):**  
   https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/sistema-nacional-de-emprego-sine

6. **Polícia Civil de Santa Catarina — Cartilha de prevenção a golpes:**  
   https://pc.sc.gov.br/wp-content/uploads/2024/04/Cartilha-Prevencao-Golpes-1.pdf

7. **SINE Paraíba — Modelo de currículo:**  
   https://sine.pb.gov.br/informacoes/documentos/modelo-de-curriculo-01.docx/view

8. **Ministério da Educação — Projovem e formação profissional:**  
   https://www.gov.br/mec/pt-br/projovem/formacao-profissional

9. **Ministério do Trabalho e Emprego — Aprendizagem profissional:**  
   https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/aprendizagem-profissional

As informações cadastradas na base de conhecimento possuem indicação de fonte e data de verificação.

## 9. Testes com usuários

O assistente foi testado por **3 pessoas externas à equipe**, totalizando **10 testes**.

Os testes foram realizados para verificar se o sistema conseguia encontrar orientações adequadas para diferentes dúvidas relacionadas ao primeiro emprego.

### Resultados dos testes

| Participante | Quantidade de testes | Orientações encontradas | Não encontradas |
|---|---:|---:|---:|
| Pessoa 1 | 3 | 2 | 1 |
| Pessoa 2 | 3 | 3 | 0 |
| Pessoa 3 | 4 | 2 | 2 |
| **Total** | **10** | **7** | **3** |

Os participantes foram identificados apenas por números, sem registro de nomes ou dados pessoais.

### Indicadores iniciais dos testes

- **Total de testes:** 10.
- **Perguntas com orientação encontrada:** 7 (70%).
- **Perguntas sem orientação encontrada:** 3 (30%).

Outros indicadores obtidos pelo programa:

- Percentual de atendimentos que ajudaram: [PREENCHER].
- Tempo médio de atendimento: [PREENCHER] segundos.
- Média de tentativas: [PREENCHER].
- Avaliação média de facilidade de uso: [PREENCHER]/5.

### Dúvidas que não foram solucionadas inicialmente

Durante os testes, três perguntas não foram reconhecidas pela busca:

1. "Como faço um currículo?"
2. "O que fazer antes de uma entrevista?"
3. "Como fazer meu currículo pela primeira vez?"

Esses resultados demonstraram que algumas formas de formular as perguntas não estavam suficientemente contempladas pelas palavras-chave cadastradas.

### Melhorias realizadas a partir dos testes

Para melhorar a capacidade de reconhecimento das perguntas, foram identificadas e adicionadas novas palavras-chave ao arquivo `base_conhecimento.json`:

- **ID 1 — Currículo:** inclusão da palavra-chave `curriculo`.
- **Orientação sobre entrevista:** inclusão de `antes de entrevista`.
- **Orientação sobre currículo:** inclusão de `curriculo primeira vez`.

Essas alterações foram feitas para ampliar as possibilidades de reconhecimento das dúvidas dos usuários.

[Após repetir as perguntas com as novas palavras-chave, registrar aqui quais passaram a ser encontradas.]

## 10. Limitações do projeto

O Primeiro Passo utiliza uma base de conhecimento previamente cadastrada em um arquivo JSON. Por isso, não consegue responder livremente a qualquer pergunta.

A busca depende das palavras-chave e dos títulos cadastrados. Perguntas formuladas de maneira muito diferente das informações disponíveis podem não ser reconhecidas.

O assistente não consulta automaticamente vagas de emprego em tempo real e não realiza inscrições em processos seletivos.

As informações apresentadas são orientativas e devem ser conferidas nas fontes oficiais. O assistente não substitui órgãos públicos, empresas ou profissionais especializados.

O sistema também não deve receber dados pessoais dos usuários, como CPF, telefone ou endereço de e-mail.

## 11. Vídeo técnico

O vídeo apresenta a estrutura do código, as classes utilizadas, o funcionamento da busca, a demonstração das funcionalidades, os testes realizados e as decisões técnicas do projeto.

**Link do vídeo no YouTube (não listado):** [INSERIR LINK]

---

**Projeto desenvolvido em Python — Citizen Assist AI / Primeiro Passo.**
