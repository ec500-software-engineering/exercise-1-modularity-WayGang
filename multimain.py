# Copyright 2018 Gang Wei wg0502@bu.edu
'''
In this prototype.py, we choose to use Wenjie Luo's Alert module,. Kainan Liu's Input module, Xiang Li's AI Module,
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



def process1(p1):
    # Alert
    print('\n-------Start Processing Alert system......')
    time.sleep(1)
    alert = Alert_module.Alert()
    for i in range(len(Bo)):
        alert.Alert_for_three_categories_input([Bo[i],0])
    for i in range(len(Bp)):
        alert.Alert_for_three_categories_input([Bp[i],1])
    for i in range(len(Pul)):
        alert.Alert_for_three_categories_input([Pul[i],2])
    UI.alert_out(alert.Alert_Output())
    print('-------Finished Processing Alert system-------')


def process2(p2):
    # AIprediction
    print('-------Start Processing AI predicting model......')
    time.sleep(3)
    AI = AiModule.AiModule()
    AI.input_check(Bo,Bp,Pul)
    predBo, predBp, predPul = AI.predict()
    UI.ai_output(predBo,predBp,predPul)
    print('-------Finished Processing AI predicting model-------')


def process3(p3):
    # Storage
    print('-------Start Processing Storage system......')
    for i in range(len(OutInputBo)):
        storage.storage(OutInputBo[i], OutInputBp[i], OutInputPul[i]).store()
    print('-------Finished Processing Storage model-------')


if __name__ == '__main__':
    bo_path = "./bo.txt"
    bp_path = "./bp.txt"
    pul_path = "./pul.txt"

    Bo = []
    Bp = []
    Pul = []

    # input
    OutInputBo = Input_module.read_data(bo_path)
    OutInputBp = Input_module.read_data(bp_path)
    OutInputPul = Input_module.read_data(pul_path)

    for i in range(len(OutInputBo)):
        s = storage.storage(OutInputBo[i], OutInputBp[i], OutInputPul[i])
        Bo.append(s.read('bo'))
        Bp.append(s.read('bp'))
        Pul.append(s.read('pul'))

    p1 = Queue()
    p2 = Queue()
    p3 = Queue()

    t1 = threading.Thread(target=process1, args=(p1,))
    t2 = threading.Thread(target=process2, args=(p2,))
    t3 = threading.Thread(target=process3, args=(p3,))

    t1.start()
    t2.start()
    t3.start()





