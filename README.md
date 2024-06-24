# FrotZ Interpreter With ChatGPT API



How to install and play:

- Download all the files on a Linux system;
- Extract the frotz-master.zip folder;
- Open the frotz-master folder and open a terminal in it;
- The "dumb" version, a more basic version of the interpreter without a user interface, will be installed;
- To do this, execute the command "make dumb" in the terminal (install any necessary packages);
- After successfully running make, execute the command "sudo make install_dumb". This will install Dumb FrotZ on your machine;
- After successful installation, you can now run games in the Z-Machine format;
- This project was built around the game Zork1, which is inside the frotz-master folder with the .z3 extension;
- To run any game in Dumb FrotZ, execute the command "dfrotz [game name + extension]";
- In this case, type the command "dfrotz zork1-r119-s880429.z3" still in the terminal within this same folder;
- The game will start running. DO NOT PLAY YET!
- Open a new terminal in the directory containing "server.py";
- Execute the command "python3 server.py";
- Now the server will be open and waiting for commands;
- Go back to the FrotZ terminal and start playing. You will see the information in the server terminal to follow the command interpretation process;

The files "dinput.c" and "doutput.c" are only for viewing the socket adjustments within the code. They are already included and adjusted within the frotz-master.zip.









Como instalar e jogar:
- Baixe todos os arquivos em um sistema Linux;
- Extraia a pasta frotz-master.zip;
- Abra a pasta do frotz-master e abra um terminal nela;
- Será instalada a versão "dumb", versão sem interface e mais crua do interpretador;
- Para isso, no terminal execute o comando "make dumb" (instale quaisquer pacotes que sejam necessários);
- Após sucesso na criação do make, realize o comando "sudo make install_dumb". Ele instalará o Dumb FrotZ em sua máquina;
- Após sucesso de instalação, agora é possível executar jogos no formato Z-Machine;
- Este projeto foi feito em torno do jogo Zork1, o qual está dentro da pasta frotz-master na extensão .z3;
- Para executar qualquer jogo no Dumb FrotZ, realize o comando "dfrotz [nome do jogo + extensão]";
- Neste caso, escreva o comando "dfrotz zork1-r119-s880429.z3" ainda no terminal desta mesma pasta;
- O jogo começará a rodar. NÃO JOGUE AINDA!;
- Abra um novo terminal no diretório que contenha o "server.py";
- Realize o comando "python3 server.py";
- Agora o servidor estará aberto e esperando por comandos;
- Volte ao terminal do FrotZ e comece a jogar. Veja que no terminal do servidor aparecerão as informações para acompanhar o procedimento de interpretação dos comandos;

Os arquivos "dinput.c" e "doutput.c" são apenas para visualização dos ajustes da socket dentro do código. Eles já estão inclusos e ajustados dentro do .zip do frotz-master.
