# Copyright 2018 Gang Wei wg0502@bu.edu

'''
In this main.py, we choose to use Wenjie Luo's Alert module,. Kainan Liu's Input module, Xiang Li's AI Module,
Shilu Wu's User Interface module and my Storage module.

AI and Alert_module is getting data from storage, storage is getting data from Input_module, Input_module is getting
data from three txt file. UI is getting data from Alert & AI.
'''
import storage
import AiModule
import Alert_module
import Input_module
import UI
import threading
from queue import Queue
import time

bo_path = "/Users/gangwei/Desktop/bo.txt"
bp_path = "/Users/gangwei/Desktop/bp.txt"
pul_path = "/Users/gangwei/Desktop/pul.txt"

Bo = []
Bp = []
Pul = []

#input
OutInputBo = Input_module.read_data(bo_path)
OutInputBp = Input_module.read_data(bp_path)
OutInputPul = Input_module.read_data(pul_path)

#storage
for i in range(len(OutInputBo)):
    s = storage.storage(OutInputBo[i],OutInputBp[i],OutInputPul[i])
    Bo.append(s.read('bo'))
    Bp.append(s.read('bp'))
    Pul.append(s.read('pul'))

def process1(p1):
    #alert
    alert = Alert_module.Alert()
    for i in range(len(Bo)):
        alert.Alert_for_three_categories_input([Bo[i],0])
    for i in range(len(Bp)):
        alert.Alert_for_three_categories_input([Bp[i],1])
    for i in range(len(Pul)):
        alert.Alert_for_three_categories_input([Pul[i],2])
    UI.alert_out(alert.Alert_Output())

def process2(p2):
    #AIprediction
    AI = AiModule.AiModule()
    AI.input_check(Bo,Bp,Pul)
    predBo, predBp, predPul = AI.predict()
    UI.ai_output(predBo,predBp,predPul)

if __name__ == '__main__':
    p1 = Queue()
    p2 = Queue()
    t1 = threading.Thread(target=process1, args=(p1,))
    t2 = threading.Thread(target=process2, args=(p2,))
    t1.start()
    t2.start()




