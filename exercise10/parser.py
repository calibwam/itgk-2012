from skumleskogen import *

def main():
    memory = {}
    keys = 0
    while True:
        n = nummer()
        if n not in memory:
            memory[n] = {"venstre": False, "høyre": False}
            if er_nokkel():
                plukk_opp()
                keys += 1
                memory = {}
            elif er_stank():
                gaa_tilbake()
                print("it stinks")
                continue
            elif er_laas():
                if er_superlaas():
                    if keys >= 2:
                        laas_opp()
                        keys -= 2
                if laas_opp():
                    keys -= 1
                else:
                    print("locked and has no key")
                    gaa_tilbake()
                    continue
            if er_utgang():
                gaa_ut()
                print("we're out!")
                return
        else:
            gaa_tilbake()
            continue
        if not memory[n]["venstre"]:
            left = gaa_venstre()
            if left:
                memory[n]["venstre"] = True
                continue
        if not memory[n]["høyre"]:
            right = gaa_hoyre()
            if right:
                memory[n]["høyre"] = True
                continue

if __name__ == "__main__":
    main()
