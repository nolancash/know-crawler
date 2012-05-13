'''
Created on May 9, 2012

@author: Nolan
'''

class Utilities(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Utilities, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1=Utilities()
    s2=Utilities()
    if(id(s1)==id(s2)):
        print "Same"
    else:
        print "Different"