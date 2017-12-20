'''
Mst=>libs=>color
'''
from os import name

if name == 'nt':
    '''windows color table'''
    # global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = 0x0
    BLUE = 0x01
    GREEN = 0x02
    CYAN = 0x03
    RED = 0x04
    PURPLE = 0x05
    YELLOW = 0x06
    WHITE = 0x07
    GREY = 0x08
else:
    '''other os color table'''
    # global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = '\033[0m'
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    RED = '\033[31m'
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    WHITE = '\033[37m'
    GREY = '\033[38m'


class Logger:

    def __init__(self):
        self.result = []
        wincode = """
class ntcolor:
    '''windows cmd color'''
    try:
        STD_INPUT_HANDLE = -10
        STD_OUTPUT_HANDLE= -11
        STD_ERROR_HANDLE = -12
        import ctypes
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        def set_cmd_text_color(self,color, handle=std_out_handle):
            '''set color'''
            bool = self.ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
            return bool
        def resetColor(self):
            '''reset color'''
            self.set_cmd_text_color(RED|GREEN|BLUE)
        def cprint(self,msg,color=BLACK,enter=1):
            '''print color message'''
            self.set_cmd_text_color(color|color|color)
            if enter == 1:
                print msg
            else:
                print msg,
            self.resetColor()
    except:
        pass
        """
        otcode = """
class otcolor:
    '''other os terminal color'''
    def cprint(self,msg,color=BLACK,enter=1):
        '''print color message'''
        if enter == 1:
            print color+msg+BLACK
        else:
            print color+msg+BLACK
        """

        if name == 'nt':
            exec(wincode)
            self.color = ntcolor()
        else:
            exec(otcode)
            self.color = otcolor()

    def _print(self,msg,color):
        self.color.cprint(msg, color, 0)

    def info(self,msg):
        self.color.cprint(msg, GREEN, 0)

    def critical(self,msg):
        self.color.cprint(msg, RED, 0)
    
    def security_note(self,msg):
        self.result.append("[Note] " + msg)
        self.color.cprint(msg, CYAN, 0)
    
    def security_warning(self,msg):
        self.result.append("[Warning] " + msg)
        self.color.cprint(msg, YELLOW, 0)
    
    def security_hole(self,msg):
        self.result.append("[Hole] " + msg)
        self.color.cprint(msg, RED, 0)
    
    def security_info(self,msg):
        self.result.append("[Info] " + msg)
        self.color.cprint(msg, GREEN, 0)

    def report(self):
        import os
        print os.linesep
        self.info("[***] Scan report:" + os.linesep)

        for item in self.result:
            self.info('      ' + item + os.linesep)
        self.info("[***] Report end")

logger = Logger()