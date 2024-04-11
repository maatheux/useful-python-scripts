
import time
from threading import Thread, Event
import win32gui
import win32con


class MsgBoxListener(Thread):

    def __init__(self, title:str, interval:int):
        Thread.__init__(self)
        self._title = title 
        self._interval = interval 
        self._stop_event = Event()

    def stop(self): self._stop_event.set()

    @property
    def is_running(self): return not self._stop_event.is_set()

    def run(self):
        while self.is_running:
            try:
                time.sleep(self._interval)
                self._close_msgbox()
            except Exception as e:
                print(e, flush=True)


    def _close_msgbox(self):
        # find the top window by title
        hwnd = win32gui.FindWindow(None, self._title)
        if not hwnd: return

        # find child button
        h_btn = win32gui.FindWindowEx(hwnd, None,'Button', None)
        if not h_btn: return

        # show text
        text = win32gui.GetWindowText(h_btn)
        print(text)

        # click button        
        win32gui.PostMessage(h_btn, win32con.WM_LBUTTONDOWN, None, None)
        time.sleep(0.2)
        win32gui.PostMessage(h_btn, win32con.WM_LBUTTONUP, None, None)
        time.sleep(0.2)


if __name__=='__main__':
    t = MsgBoxListener('Microsoft Excel', 1)
    t.start()
    time.sleep(10)
    t.stop()