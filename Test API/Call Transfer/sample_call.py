import sys
from pycall import CallFile, Call, Application

def call(number):
        c = Call('SIP/flowroute/%s' % number)
        a = Application('Playback', 'hello-world')
        cf = CallFile(c, a)
        cf.spool()

if __name__ == '__main__':
        call(sys.argv[1])