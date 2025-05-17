#main program
import Reloadingmodule
import time
import importlib
def disp(d):
    print("="*50)
    print("\tShare Name\tValue")
    print("=" * 50)
    for sv,sn in d.items():
        print("\t{}\t\t:{}".format(sv,sn))
    else:
        print("="*50)
# main program
d=Reloadingmodule.sharesinfo() #previously imported module
disp(d)
time.sleep(20)
importlib.reload(Reloadingmodule) # re loading previously imported module
d=Reloadingmodule.sharesinfo()    # obtaing changed/ new values of previously imported module
disp(d)