# signl_util.py
# 2021/09/26
###################################################
#!/use/bin/env python
import signal

fint_func=None

signals=[ signal.SIGTERM, signal.SIGINT, signal.SIGSEGV]


def sig_handler(signum, msg):
    """
    Signal Handler
    """

    print(f'Received signal [{signum}]')

    if signum in signals:
        if fint_func is not None:
            fint_func()


def add_signal(fintfunc):

    global fint_func
    fint_func=fintfunc

    for sig in signals:
        signal.signal(sig, sig_handler)
