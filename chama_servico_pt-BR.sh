cd $HOME/git/servico_tratamento_palavras/
mkdir $HOME/git/servico_tratamento_palavras/log
docker compose up -d  --build --scale app=10
