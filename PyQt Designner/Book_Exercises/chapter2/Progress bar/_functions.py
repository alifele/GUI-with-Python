import time

def start_download(self):
    x = 0
    T = int(self.ui.time.text())
    step = T/100

    while x<101:
        self.ui.progress.setValue(x)
        time.sleep(step)    
        x += 1
