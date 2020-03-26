import json
def upd(str):
    ls = json.load(open("bd.json", "r", encoding="utf-8"))
    ls.update(str)
    with open('bd.json', 'w', encoding="utf-8") as f:
        json.dump( ls, f, indent=4, ensure_ascii = False)
        f.close()
rr = 111111

for i in range(0,5):
    ls = json.load(open("bd.json", "r", encoding="utf-8"))
    status = 1
    #for i in range(0,len(ls)):
    if (str(rr) in ls) == True :
        status = 0
    if status == 1:
        ids = {"{}".format(rr):{}}
        upd(ids)

def zerol(event,ls):
    if 'conv' in ls[str(event.obj.from_id)]:
        if str(event.obj.peer_id) in ls[str(event.obj.from_id)]['conv']:
            if 'role' not in ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)]:
                ls[str(event.obj.from_id)]['conv'][str(event.obj.peer_id)].update({'role':0})
        else: 
            ls[str(event.obj.from_id)]['conv'].update({str(event.obj.peer_id):{'role':0}})
    else:
        ls[str(event.obj.from_id)].update({'conv':{str(event.obj.peer_id):{'role':0}}})
        


