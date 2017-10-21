if __name__=='__main__':
    import math
    ab=int(raw_input())
    bc=int(raw_input())
    print str(int(round(math.degrees(math.atan2(ab,bc)))))+'°'    