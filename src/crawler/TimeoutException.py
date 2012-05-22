'''
Created on May 21, 2012

@author: Tyler, Nolan
'''
import signal

"""
This class provides the functionality that we need to timeout certain
functions in our web crawler.
"""
class TimeoutException(Exception): 
    pass 

"""
Creates a decorator that takes the duration of the timeout and errors
if execution runs longer than that duration.
"""
def timeout(timeout_time):
    def timeout_function(f):
        def f2(*args):
            def timeout_handler(signum, frame):
                raise TimeoutException()
 
            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
            # Triggers alarm in timeout_time seconds.
            signal.alarm(timeout_time)
            try: 
                retval = f(*args)
#            except TimeoutException:
#                return default
            finally:
                signal.signal(signal.SIGALRM, old_handler) 
            signal.alarm(0)
            return retval
        return f2
    return timeout_function