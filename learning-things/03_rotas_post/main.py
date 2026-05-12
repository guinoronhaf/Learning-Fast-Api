from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str # obrigatório
    descricao: str # obrigatório
    concluida: bool = False # opcional. Por padrão, False

app = FastAPI()

tarefas_repo = {}
id = 0

@app.get("/tarefas")
def listar_tarefas():
    tarefas = [tarefa["titulo"] for tarefa in tarefas_repo.values() if tarefa]
    return {
            "tarefas": tarefas
    }

# ou seja, o que se passa no json não é um objeto Tarefa, mas um json com seus atributos
"""
Como dá pra perceber, o parâmetro status_code define qual é o status_code em caso de sucesso da operação.

Note que status_code é um parâmetro de método "decorador" (get, post, etc.) e não da função de operação da rota.
"""
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
    global id, tarefas_repo
    # com tarefa: Tarefa, FastAPI valida automaticamente o JSON recebido
    nova_tarefa = tarefa.model_dump() # Converte para dict

    id += 1
    tarefas_repo[id] = nova_tarefa

    return {"mensagem": "Criado!", "tarefa": nova_tarefa}


"""
É possível, naturalmente, definir um código de status alternativo a depender do fluxo da operação. Para isso, basta adicionar o parâmetro response, do tipo Response.
"""
@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa, response: Response):
    global id, tarefas_repo
    if tarefas_repo.get(tarefa_id) is not None:
        tarefas_repo[tarefa_id] = tarefa_atualizada.model_dump()
        return {
                "mensagem": "Tarefa atualizada!"
        }
        print(tarefas_repo)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
                "mensagem": "Erro! Tarefa não encontrada."

        }


@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, response: Response):
    global id, tarefas_repo
    if tarefas_repo.get(tarefa_id) is not None:
        tarefas_repo[tarefa_id] = None
        return {
                "mensagem": "Tarefa deletada!"
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
                "mensagem": "Tarefa não encontrada!"
        }

