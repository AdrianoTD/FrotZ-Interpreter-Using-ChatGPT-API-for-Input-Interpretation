# TCC

Como instalar e jogar:
- Baixe todos os arquivos em um sistema Linux;
- Extraia a pasta frotz-master.zip
- Abra a pasta do frotz-master e abra um terminal nela
- Será instalada a versão "dumb", versão sem interface e mais crua do interpretador
- Para isso, no terminal execute o comando "make dumb" (instale quaisquer pacotes que sejam necessários)
- Após sucesso na criação do make, realize o comando "sudo make install_dumb". Ele instalará o Dumb FrotZ em sua máquina
- Após sucesso de instalação, agora é possível executar jogos no formato Z-Machine
- Este projeto foi feito em torno do jogo Zork1, o qual está dentro da pasta frotz-master na extensão .z3
- Para executar qualquer jogo no Dumb FrotZ, realize o comando "dfrotz [nome do jogo + extensão]"
- Neste caso, escreva o comando "dfrotz zork1-r119-s880429.z3" ainda no terminal desta mesma pasta
- O jogo começará a rodar. NÃO JOGUE AINDA!
- Abra um novo terminal no diretório que contenha o "server.py"
- Realize o comando "python3 server.py"
- Agora o servidor estará aberto e esperando por comandos
- Volte ao terminal do FrotZ e comece a jogar. Veja que no terminal do servidor aparecerão as informações para acompanhar o procedimento de interpretação dos comandos
