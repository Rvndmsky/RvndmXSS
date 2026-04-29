import argparse
import asyncio
from core.banner import show_banner
from core.exploit import scan

def load_list(f):
    return [x.strip() for x in open(f) if x.strip()]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('-u')
    p.add_argument('-l')
    p.add_argument('-p', '--payload')
    a = p.parse_args()

    target = a.u if a.u else (a.l if a.l else None)
    show_banner(target)

    eps = []
    if a.u:
        eps = [a.u]
    elif a.l:
        eps = load_list(a.l)

    try:
        asyncio.run(scan(eps, a.payload))
    except KeyboardInterrupt:
        print("\n[KOK UDAH SELESAI BANG]\n")
    except:
        print("\n[KOK UDAH SELESAI BANG]\n")

if __name__ == '__main__':
    main()
