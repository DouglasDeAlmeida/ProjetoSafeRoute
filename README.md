# ProjetoSaferRoute


![GifProjeto](https://github.com/DouglasDeAlmeida/ProjetoSafeRoute/blob/master/saferRoute.gif)

### 1.	Introdução e Justificativa:

 Nesse contexto atual de Pandemia do Coronavírus, o avanço das novas tecnologias é primordial para prevenção dos riscos de transmissão. Nossa solução visa trazer maior recuperação em termos de saúde para a sociedade civil e recuperação econômica. Quanto ao aspecto social, não só garantirá acesso das pessoas ao bem do livre exercício, quanto ao direto de ir e vir com segurança e conforto, que por meio da solução possa frequentar os lugares públicos ou privados sem medo e desconforto diante do risco de contaminação, bem como potencializará o fluxo normal para o retorno das famílias aos seus postos de trabalhos, levando à normalização da geração da renda. No caso das empresas, gerará a receita advindo das atividades empresariais, por meio da prestação dos seus serviços à sociedade considerando o controle de fluxo para o retorno das atividades levando em conta a melhor forma, consequentemente, gerando obtenção de renda ao Estado. 
 
 Para tal momento, o sentimento de segurança para o retorno da normalidade tratará benefícios para todos e gerará grande expectativas as pessoas para um sentimento de esperança quando se tratar de avanços em aspetos de solução para prevenção de acometimento do vírus, principalmente para áreas destinadas a grande circulação de usuários, onde podemos observar intenso fluxo de pessoas em espaços comerciais, em especial em Shopping Centers.
 
 Portanto, estes espaços se destacam em relação aos demais espaços comerciais, pois está inserido no contexto de serviços essenciais à sociedades pela sua diversidade funcional atendendo serviços comerciais e lazer, sendo grande atrativo para circulação de pessoas com fluxos intenso em todo decorrer do dia, gerando assim, alta aglomeração de pessoas, devido aproximação e contatos entre elas. Este cenário é ideal para transmissão e contágio do vírus.  

### 2.	Objetivo:

Nosso objetivo e idealização da solução ”Safer-Route”, usamos de tecnologia para agregar valores ao cidadão e sociedade, tanto referente ao sentimento de segurança e comodidade, onde visamos manter o uso do direito de ir e vir informando a rota mais segura ao usuário, quanto à economia de tempo e controle de fluxo em comércios diante do cenário atual. Trazemos como resultado para usuário a sensação de mais conforto, segurança e melhor caminho para o retorno das atividades no quesito sociedade.

### 3.	Uso da tecnologia:

  Identificamos os índices de aglomeração em espaços comerciais como foco central da nossa solução, trabalho este bastante complexo por conta da escassez dos dados. Em especial, a falta de informações com relação a contagem de fluxo e contagem de pessoas para determinados dias e picos de horários que transitam em espaços privados.
 
  Nossa idealização e desafio quanto ao propósito do projeto é evidenciado no uso da Ciência de dados a fim de dispor de uma ferramenta tecnológica aos usuários para que informe dos possíveis horários programados com métricas que evidenciam o cenário com menor aglomeração segundo levantamento de fluxo a partir de determinados dados, como dia da semana e horário, para qual o usuário tem a pretensão de visitar um case comercial específico.
 
 Assim, demos evidência para o menor potencial de contágio diante do cenário apresentado, com menores níveis de fluxo que estejam em trânsito no interior do estabelecimento comercial pretendido, dando a confiabilidade para uma visita tranquila e menor possibilidade de contrair o vírus.
 
 ### 4.	Case observado e problema:
 
 A partir de métricas observadas para um case comercial específico: SHOPPING IGUATEMI, situado na cidade de São Paulo – SP, analisamos o comportamento empírico no que tange os níveis de aglomeração de pessoas que transitam no interior da área deste estabelecimento comercial e observamos os níveis de aglomeração no decorrer do dia para determinados picos de horários.

É evidente que em um maior numero de pessoas, o contato físico é inevitável, o que pode aumentar as chances de contágio, cenário este perfeito para incidência e proliferação do vírus entre os que circulam. Consequentemente, surge um sentimento de insegurança entre os clientes, o que faz com que estes indivíduos restrinjam suas visitas à estes espaços. Logo, as famílias e empresas que obtêm receitas advindas desse segmento acabam encontrando sérios prejuízos econômicos.

### 5.	Coleta de Dados:

 Para coleta dos dados foi utilizado para apuração das métricas por meio de pesquisas, observações empíricas de comportamento e fatos constatados no case o Shopping Iguatemi São Paulo. Os quais foram extraídos  através de pesquisas disponíveis na internet e manipulando os referidos dados para constituição de dataset não estruturado compilados em uma dicionário com uso da linguagem Python.

### 6.	Metodologia operacional:

A simulação foi criada a partir do Turtle, utilizando a biblioteca gráfica Lib/turtle.py que por sua vez é baseada na linguagem de programação Logo. 
 
As informações referentes à aglomeração foram obtidas através de uma inspeção 
dos dados disponibilizados pelo google maps. 
 
As movimentações dos agentes ocorrem por meio de 3 algoritmos:

- DFS (Depth First Search).
	
	- Este algoritmo tem como objetivo percorrer todos os componentes de uma ramificação da matriz antes de voltar para o ponto inicial. Ele permite que o agente ande por todas as celulas do mapa.
	
 
- A*.
	
	- O algoritmo AStar é utilizado para encontrar o menor caminho entre dois pontos. No nosso projeto foi ele foi utilizado para o “Pacman” ir da entrada do shopping até a entrada de uma loja. 
	  

- Vaguear.
	
	- A finalidade deste algoritmo é movimentar os “fantasmas”. O vaguear faz com que os agentes andem aleatoreamente pelo mapa.
    
### 7.	Limitações da Solução:

Inicialmente,encontramos algumas restrições que apresentamos a seguir em termos de limitações de tecnologias operacionais, nas quais valem citar: 

1.	Territorialidade Geográfica – Dado, que foi estabelecido como case comercial, Shopping Iguatemi, situado na Cidade São Paulo – SP, a limitação está configurada quanto à possiblidade de expansão para outros novos cases comerciais, haja vista que abordagem da solução contempla apenas único case comercial com grande potencial de solução tecnológica; 

2.	Aglomeração Tempo Real – Outro ponto se encontra na métrica que observamos quando manipulamos os dados estatísticos dos níveis de aglomeração em tempo real sobre os picos de horários com contagem de fluxo dos usuários que transitam pelo interior do case comercial para um dado tempo, desejado por eles para um possível cenário imediato de hora atual. Por ora, ficamos limitados sem a criação e aplicação tecnológica e operacional da referida ferramenta que poderia agregar valor ao usuário com um simples retorno a título de informação textual instruindo o atual cenário quanto aos níveis de aglomeração para uma intenção de uma visita tranquila ao estabelecimento com menos risco transmissão do vírus por aglomeração;

 
3.	Layout Gráfico – Outro ponto que tivemos limitação foi no uso gráfico Turtlle, para criação e aplicações gráficas mais intuitiva em termos de chamar atenção dos usuários com mais riquezas design com possíveis aplicações em 3D, de certa forma trará um benefício no efeito visual e com aparência mais similar ao real dos cenários existentes no interior do case comercial proporcionando imagens mais intuitivas e atrativas aos olhos dos usuários.

### 8.	 Conclusão:

 Diante do exposto, aqui trazidos em termo de fatos, problemas e solução, pode-se dizer que o maior risco de contaminação se dá por meio de aglomeração em espaços de acesso ao público, sejam eles em estabelecimentos públicos ou privados. Partindo desta visão, estudamos e concluímos que o maior fluxo em grandes metrópoles se dá grandes aglomerações comerciais, sendo os Shopping Centers o de maior fluxo. Utilizamos o Shopping Iguatemi para estudo de case e apresentamos uma solução para auxiliar o usuário que deseja/necessita circular neste ambiente.
 
 A solução criada e apresentada tem como objetivo trazer economia de tempo e a maior segurança para o usuário, eludindo a aglomeração em Shoppings por meio de uma aplicação visual. 
 
 Os fantasmas representando a aglomeração dão um indicativo do quão seguro é percorrer o caminho escolhido, ao mesmo tempo que a aplicação informa se o horário de visita ao Shopping é recomendado ou não baseado nos horários de maior circulação do local. O que também pode ocasionar em uma economia de tempo se a solução for consultada pelo usuário antes da visita.



