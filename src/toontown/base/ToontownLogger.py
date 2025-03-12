import sys, time, os

class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()
		
class LogWriter:

    def __init__(self):
        self.logPrefix = 'geargrind-'
        logSuffix = time.strftime('%m-%d-%Y-%H-%M-%S')
        if not os.path.exists('user/logs/'):
            os.mkdir('user/')
            os.mkdir('user/logs/')
        logfile = os.path.join('user/logs', self.logPrefix + logSuffix + '.log')
        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.stdout, log)
        logErr = LogAndOutput(sys.stderr, log)
        sys.stdout = logOut
        sys.stderr = logErr