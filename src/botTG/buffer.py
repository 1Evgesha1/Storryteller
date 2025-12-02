


dialog_history={}
max_history= 10

def add_to_history(user_id: int, role:int, content:int):
    if user_id not in dialog_history:
        dialog_history[user_id]=[]

    dialog_history[user_id].append({'role':role, 'content':content})
    dialog_history[user_id] = dialog_history[user_id][-max_history]

