# AED3_TP04
# Trabalho Prático AEDS III

## Nome dos integrantes

 - Antônio Drumond Cota de Sousa
 - Laura Menezes Heráclito Alves
 - Davi Ferreira Puddo
 - Raquel de Parde Motta
   
## Links dos trabalhos anteriores
- [TP1](https://github.com/AntonioDrumond/AED3_TP01/)
- [TP2](https://github.com/AntonioDrumond/AED3_TP02/)
- [TP3](https://github.com/davipuddo/AED3_TP03)

## Introdução

O hash extensível é uma estrutura de dados dinâmica e eficiente, ideal para sistemas que exigem armazenamento e recuperação rápida de informações. Este projeto visa não apenas implementar esse algoritmo em Python, mas também desenvolver uma interface visual interativa usando Tkinter, tornando seu funcionamento acessível e didático. Ao integrar a lógica do hash extensível com uma GUI intuitiva, permitimos que usuários insiram, busquem e visualizem as operações em tempo real — incluindo a expansão do diretório e a divisão de buckets.

## Experiência

A experiência adquirida durante o desenvolvimento deste projeto foi extremamente enriquecedora, tanto no aspecto técnico quanto no aprendizado colaborativo. Ao trabalharmos com o Tkinter, superamos a curva inicial de adaptação à biblioteca e passamos a dominar conceitos essenciais de interfaces gráficas, como a criação de componentes dinâmicos e a gestão de eventos interativos. O maior desafio — traduzir a lógica interna do hash extensível para uma representação visual clara — nos forçou a pensar criativamente, resultando na solução de mapear os buckets para uma lista de listas de tuplas, o que reforçou nossa compreensão sobre estruturas de dados aninhadas e manipulação eficiente de informações. Além disso, o projeto nos mostrou a importância do planejamento e da iteração constante, já que cada obstáculo exigiu ajustes no código e na interface para garantir precisão e usabilidade. No final, não apenas consolidamos nosso conhecimento sobre hashing extensível e GUIs, mas também desenvolvemos habilidades valiosas em resolução de problemas e trabalho em equipe, percebendo como a persistência e a colaboração são fundamentais para transformar conceitos abstratos em aplicações funcionais e didáticas.

## Desafios

Um dos principais desafios enfrentados durante o desenvolvimento do projeto foi a curva de aprendizado da biblioteca **Tkinter**, que, apesar de simples, exigiu um tempo considerável para nos familiarizarmos com seus componentes e métodos, especialmente na renderização dinâmica de tabelas e na sincronização de eventos. Outra dificuldade significativa foi a transferência dos dados da tabela hash—estruturada em buckets com registros—para a tabela interativa da interface gráfica. Inicialmente, não estava claro como mapear essa estrutura complexa para uma representação visual intuitiva, mas a solução surgiu ao transformarmos os buckets em **uma lista de listas de tuplas**. Essa abordagem permitiu que os dados fossem exibidos de forma organizada na interface, embora tenha demandado ajustes manuais para garantir que a visualização refletisse com precisão o estado interno do hash extensível após cada operação. 

## Visualização
[**Tkinter**](https://docs.python.org/pt-br/3.13/library/tkinter.html) é a biblioteca padrão do Python para desenvolvimento de interfaces gráficas (GUI), oferecendo uma maneira simples e eficiente de criar aplicações com elementos visuais como janelas, botões, menus e tabelas. Por ser nativa do Python, ela não requer instalações adicionais e é amplamente utilizada para prototipagem rápida e projetos educacionais, graças à sua sintaxe intuitiva e documentação acessível. Embora não seja a ferramenta mais moderna para GUIs, sua simplicidade a torna ideal para demonstrar conceitos de programação de forma interativa, como no caso de estruturas de dados.  

No projeto da **hash extensível**, o Tkinter foi empregado para construir uma interface que torna o algoritmo mais tangível e didático. Ele permite visualizar em tempo real a inserção, busca e remoção de valores, exibindo o diretório e os *buckets* em tabelas dinâmicas (como as geradas pela classe **Table**). Além disso, a interação do usuário é facilitada por campos de entrada e botões, transformando operações abstratas do hash em ações visíveis e intuitivas. Essa abordagem não só ilustra o funcionamento interno da estrutura, mas também reforça seu aprendizado através da experiência prática.

## Como funciona?
### Tabela Hash ( ExtendibleHash.py )
O código implementa um **hash extensível**, uma tabela hash dinâmica que cresce conforme novos dados são inseridos. A função **insert** adiciona valores e, se um *bucket* estiver cheio, chama **dupBucket** para dividi-lo e atualizar o diretório. Quando necessário, **dupDir** dobra o tamanho do diretório. A função **hash** calcula a posição no diretório, **find** busca valores e **delete** remove. As funções **getRefs** e **formatedRefs** ajudam a visualizar a estrutura. Assim, o hash extensível mantém buscas rápidas mesmo com muitos dados, expandindo-se dinamicamente.

### Bucket ( Bucket.py )
**Bucket** representa um balde em um hash extensível, gerenciando seus registros de forma eficiente. Seu construtor (__init__) define o tamanho máximo, a profundidade local (usada no controle de divisão) e inicializa a lista de registros. O método **insert** adiciona novos registros ordenados por ID (se houver espaço), enquanto **find** realiza buscas por ID. Além disso, **isFull** verifica se o bucket está cheio, **isEmpty** confere se está vazio, e **__repr__** gera uma representação textual do bucket, mostrando seus registros e profundidade local. Dessa forma, a classe assegura o armazenamento organizado e o acesso rápido aos dados dentro do hash extensível.

### Registro individual ( register.py )
**Register** representa um registro individual armazenado em um bucket do hash extensível, tendo como principal atributo o **ID**, que identifica unicamente cada registro. Seu construtor (__init__) recebe e define esse valor, enquanto o método __repr__ retorna o ID em formato de string para facilitar a visualização e depuração. Em resumo, cada objeto **Register** corresponde a um valor específico dentro da estrutura, sendo a unidade básica de armazenamento gerenciada pelos buckets no hash extensível.

### Tabela ( table.py )
A classe **Table** cria e gerencia uma tabela visual interativa usando Tkinter, permitindo a exibição e edição dinâmica de dados em uma interface gráfica. Seu construtor (__init__) recebe um container (master) e os cabeçalhos das colunas (headers), inicializando a estrutura e chamando create_table para renderizar a tabela na tela. O método update_data substitui todo o conteúdo da tabela por novos dados, enquanto add_row insere uma nova linha, set_value modifica células específicas e highlight_row/remove_highlight controlam o destaque temporário de linhas (útil para realçar resultados de buscas). Em resumo, essa classe facilita a manipulação e visualização de dados tabulares de forma flexível e integrada à interface do projeto.

### Principal ( main.py )
O arquivo **main.py** serve como núcleo do visualizador de hash extensível, integrando a lógica da estrutura de dados com a interface gráfica desenvolvida em Tkinter. Ele cria três janelas interativas: uma para inserção e busca de valores, outra para exibir o diretório e uma terceira para visualizar os buckets, utilizando a classe **ExtendibleHash** como base para as operações. Conforme o usuário insere ou busca valores, o sistema atualiza dinamicamente as tabelas e rótulos, ilustrando em tempo real as mudanças no diretório e nos buckets durante cada operação. Dessa forma, o arquivo funciona como ponto de entrada do programa, transformando conceitos abstratos do hash extensível em uma representação visual clara e interativa.

## Resultados

O seu projeto demonstrou com sucesso a implementação e visualização interativa de um **hash extensível**, combinando eficientemente a estrutura de dados com uma interface gráfica intuitiva em Tkinter. Os resultados mostram que o algoritmo funciona corretamente, expandindo dinamicamente o diretório e redistribuindo os registros entre os buckets conforme novos valores são inseridos, mantendo a complexidade média de busca em *O(1)*. A visualização em tempo real das operações—como divisão de buckets e duplicação do diretório—torna o processo mais tangível, destacando como o hash extensível equilibra desempenho e uso de memória. A integração entre a lógica (**ExtendibleHash**) e a interface (**Table**) permite que usuários entendam não apenas o resultado das operações, mas também seu funcionamento interno.  

Além disso, a interface gráfica cumpre um papel didático, facilitando a compreensão de conceitos complexos, como **profundidade global/local** e **redimensionamento dinâmico**. A capacidade de inserir, buscar e visualizar mudanças instantaneamente reforça a eficácia da estrutura em cenários reais, como bancos de dados ou sistemas de armazenamento. O projeto também evidenciou desafios comuns, como a necessidade de sincronização entre a representação visual e o estado interno do hash, resolvidos através de atualizações automáticas das tabelas. No geral, os resultados validam não apenas a corretude da implementação, mas também a utilidade de ferramentas visuais para o ensino de estruturas de dados, sugerindo possíveis melhorias, como animações para ilustrar divisões de buckets ou suporte a operações em lote.

## Vídeo demonstrativo



## Checklist

- [x] A visualização interativa da Tabela Hash Extensível foi criada? **SIM**.

- [x] Há um vídeo de até 2 minutos demonstrando o uso da visualização? **SIM**.

- [x] O trabalho está funcionando corretamente? **SIM**.

- [x] O trabalho está completo? **SIM**

- [x] O trabalho é original e não a cópia de um trabalho de outro grupo? **SIM**

