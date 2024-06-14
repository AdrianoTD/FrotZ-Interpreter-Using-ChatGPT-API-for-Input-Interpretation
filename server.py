import socket
import openai
import time
from ctypes import *

class Payload(Structure):
    _fields_ = [("id", c_int),
                ("counter", c_int),
                ("msg", c_char * 256),  # Ajustando o tamanho da mensagem
                ("temp", c_float)]
                
def gptResponse(game_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
	messages=[{"role":"user", "content": game_input}]
    )
    
    reply = completion.choices[0].message.content
    
    return reply.lower()
    
    
                         

def gptPrompt(command):
    openai.api_key = "SUA CHAVE API DO CHAT GPT AQUI"
    
    #Primeira instância de chamada
    game_input0 = "Se a frase conter alguma palavra do seguinte conjunto de palavras: (\"odysseus\", \"inventory\", \"look\", \"quit\", \"restore\", \"restart\", \"save\", \"time\", \"wait\"), retorne escrito para mim apenas a primeira palavra deste conjunto que aparecer, sem explicações ou comentários. Caso a frase não contenha nenhuma das palavras do conjunto, retorne para mim apenas a palavra \"action\". A frase é: " + command + "."
    
    replyInput0 = gptResponse(game_input0) 
    
    if replyInput0 != "action":
        reply = replyInput0
        return reply
    
    
    
    #Segunda instância de chamada
    game_input1 = "Tenho a seguinte frase: " + command + ". Identifique apenas o primeiro verbo de ação em inglês que representa uma ação direta (como por exemplo, 'open', 'go', 'get', 'grab', 'climb', entre outros) e retorne para mim, sem realizar nenhuma explicação ou comentário sobre, apenas a palavra sem ponto final."

    replyInput1 = gptResponse(game_input1) 
    print (replyInput1)




    #Terceira instância de chamada
    game_input2 = "Tenho a seguinte frase: " + command + ". Dentro do contexto da mensagem, caso esta contenha uma palavra que remeta a um objeto ou lugar ou direção ou inimigo (como spider, troll, entre outros), retorne para mim apenas a primeira dessas palavras que aparecer na sentença, sem realizar nenhuma explicação ou comentário sobre, apenas a palavra."


    replyInput2 = gptResponse(game_input2)
    print (replyInput2)
    
    #Tratamento da lanterna (utiliza 3 palavras na sintaxe)
    game_input3 = "Se a frase conter a palavra \"lamp\", verifique se existe a palavra \"on\" ou a palavra \"off\". Retorne escrito para mim apenas primeira delas que aparecer, sem comentários ou explicações. Caso a frase não tenha nenhuma das duas palavras, me avise. A frase é: " + command + "."
    
    replyInput3 = gptResponse(game_input3)
    print (replyInput3)
    
    #Tratamento do combate (utiliza 4 palavras na sintaxe)
    game_input4 = "Se a frase conter palavras de ação de combate como \"attack\" ou \"kill\" e um inimigo como \"spider\", \"troll\", entre outros, junto de uma arma de combate como por exemplo \"sword\", retorne escrito para mim apenas a arma de combate, sem comentários ou explicações. Caso a frase não tenha nenhuma arma de combate, me avise. A frase é: " + command + "."
    
    replyInput4 = gptResponse(game_input4)
    print (replyInput4)
    
    
    #Retorno do comando
    if replyInput4 == "sword":
        reply = replyInput1 + ' ' + replyInput2 + ' with ' + replyInput4
         
    elif replyInput3 == "on" or replyInput3 == "off":
        reply = replyInput1 + ' ' + replyInput2 + ' ' + replyInput3
        
    else:
        reply = replyInput1 + ' ' + replyInput2
    
    

    print(reply)
    return reply


def main():
    PORT = 2300
    server_addr = ('localhost', PORT)

    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    try:
        ssock.bind(server_addr)
        print("Bind done")
        ssock.listen(3)
        print("Server listening on port {:d}".format(PORT))

        while True:
            csock, client_address = ssock.accept()
            print("Accepted connection from {:s}".format(client_address[0]))
            
            try:
                expected_size = sizeof(Payload)
                buffer = b''
                while len(buffer) < expected_size:
                    packet = csock.recv(expected_size - len(buffer))
                    if not packet:
                        break
                    buffer += packet

                if len(buffer) < expected_size:
                    print(f"Received incomplete buffer of size {len(buffer)}")
                    continue

                print("Received {:d} bytes".format(len(buffer)))

                payload = Payload.from_buffer_copy(buffer)
                msg_str = payload.msg.decode('utf-8').rstrip('\x00')  # Decodificar e remover null terminator
                print(f"Received content: id={payload.id}, counter={payload.counter}, msg={msg_str}, temp={payload.temp}")
                
                gptReply = gptPrompt(msg_str) + "\n"
                
                new_message = gptReply.lower()
                payload.msg = new_message.encode('utf-8')

                # Echo the received message back to the client
                buffer = bytes(payload)
                csock.sendall(buffer)
                print("Comando retornado: " + new_message)
                print("Sent {:d} bytes back".format(len(buffer)))
                
            except Exception as e:
                print(f"Exception on socket: {e}")

            finally:
                print("Closing connection to client")
                print("----------------------------")
                csock.close()
                
                
    except Exception as e:
        print(f"Exception on socket setup: {e}")

    finally:
        ssock.close()
        print("Closing server socket")
        
        
if __name__ == "__main__":
    main()           
