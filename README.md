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


#Para rodar do Zero
 - Instale o comando git na sua máquina (ou gitbash se tiver usando windows);
 - Instale o docker, eu estou usando a versão 27.3.1;
 - Comando para baixar : git clone https://github.com/spedison/servico_nlp_python_pt-br.git
 - Vá na pasta do projeto : cd servico_nlp_python_pt-br
 - Levante o projeto no docker : docker compose up -d  --build --scale app=2 
 - faça o teste do "Alô Mundo" citado anteriormente
 - faça os testes com as URLs dos comandos usando ferramentas como curl ou Postman

#Referências
 - https://spacy.io
 - https://www.nltk.org
 - https://fastapi.tiangolo.com/tutorial/
 - https://docs.docker.com/reference/cli/docker/compose/
 - https://curl.se/docs/manpage.html
 - https://curl.se/docs/tutorial.html
 - https://www.postman.com
 - https://www.ibm.com/topics/stemming-lemmatization
 - https://www.analyticsvidhya.com/blog/2022/06/stemming-vs-lemmatization-in-nlp-must-know-differences/

#Coisas para fazer:

   - [ ] - Colocar um sistema de autenticação;
   - [ ] - Rodar em um servidor com http habilitado;
   - [ ] - Avaliar a performance no java.
