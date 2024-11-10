#O que esse projeto?

   Esse projeto Python tem como base uso inicial para processamento de strings em nlp em português.
   Ele tem tem 3 comandos executados por serviço web com uma com um proxy nginx:
      * Tokenização
      * Steam
      * Lemanização
   Pode ser executado em diversas instâncias para montar um cluster de disponibilidade e/ou performance para fazer os processamentos de texto.

#Qual o histórico?

   Eu sou um programador que adora Java e estamos estudando entre amigos para montar um sistema de busca semelhante (ou quase) ao que o google utiliza.
   Quando precisei de bibliotecas Java para fazer esses processamentos em português tivemos dificuldades, assim, ao menos por enquanto, para não prejudicar a data da apresentação do projeto, vamos fazer a chamadas rest a partir do java para esse serviço. 
   Assim, podemos realizar os processamento que desejamos.

#A quem se destina?
  Qualquer pessoa que deseja fazer processamentos básicos de NLP em português. 
  Esse projeto tem 3 serviços, além de um "Alô mundo."

#Como instalar?
  Ele foi feito em Python 3.9, mas você não precisa instalar toda a estrutura que ele usa. 
  Se você tiver docker com o plugin de docker compose, é muito simples.
  
#Como testar?

  * Levantando o serviço com 2 instâncias da aplicação:
    - docker compose up -d  --build --scale app=2
    
  * Para terminar a aplicação o comando docker é:
    - docker compose down
    
  * Chamando o Hello Word:
    - curl http://localhost:80/ 
    - Ele responderá: {"message":"Hello, World!","date_time":"2024-11-10 20:04:35.496043","hostname":"3a6265e4b2fd"}
    
  * Os outros comandos usam post com um corpo padrão.
    - /token/copia=(True|False)
    - /lemmatize/copia=(True|False)
    - /stem/copia=(True|False)
    
  * O parâmetro "copia" significa que você além de receber o resultado, você pode receber o que foi enviado, caso precise.
  * Corpo enviado no post:
    -  {
         "text" : "Este é o texto que desejo processar."
       }

#Coisas para fazer:
   [ ] - Colocar um sistema de autenticação;
   [ ] - Rodar em um servidor com http habilitado.