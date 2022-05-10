from flask import Flask, request, render_template, Response

app = Flask(__name__)

'''
O que deve ser feito?

Na url /todo/nome_empresa/nome_lista (por exemplo, /todo/bradesco/ia)
vamos guardar um todo.

Tomemos como exemplo /todo/bradesco/ia
Ao fazemos um envio de formulário, com GET, nessa URL, devemos salvar esse
item na lista de TODOs, de forma a ele ser exibido toda vez que nós acessarmos essa URL
(testes 1, 2a, 2b, 2c)

Também podemos enviar o formulário através do verbo POST
(teste 3)

A lista de empresas que pode salvar TODOs é a seguinte:  ["bancodobrasil","impacta","bradesco"]
Qualquer empresa fora dessa lista deve ser recusada, seus TODOs nao 
devem ser salvos, e retornamos um cod status 400
(teste 4)
'''
mensagens = {
     
}

@app.route("/todo/<instituicao>/<sala>", methods=["GET","POST"])
def chat(instituicao, sala):
    instituicaos = ["bancodobrasil","impacta","bradesco"]
    dic_via_get = request.args
    dic_via_post = request.form
    if instituicao not in instituicaos:  
        return Response(status=400)   
    
    if sala not in mensagens.keys(): 
        mensagens[sala] = []                      

    if "item" in dic_via_get:
        mensagens[sala].append(dic_via_get['item']) 

    if "item" in dic_via_post:
        mensagens[sala].append(dic_via_post['item']) 
    return render_template("template_todo.html", msgs = mensagens[sala], instituicao = instituicao, nome_sala = sala)

app.run(debug=True)
