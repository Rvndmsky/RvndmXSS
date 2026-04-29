import argparse
from core.banner import show_banner
from core.exploit import safe_run
def load_list(f): return [x.strip() for x in open(f) if x.strip()]
def main():
    p=argparse.ArgumentParser(); p.add_argument('-u'); p.add_argument('-l'); p.add_argument('-p','--payload'); a=p.parse_args()
    target=a.u if a.u else (a.l if a.l else None); show_banner(target)
    eps=[]; 
    if a.u: eps=[a.u]
    elif a.l: eps=load_list(a.l)
    safe_run(eps,a.payload)
if __name__=='__main__': main()
