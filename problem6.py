for i in range(0,24):
    if i==0:
        print("12Am Midnight")
    elif i<12:
        print(f"{i}Am")
    elif i==12:
        print("12Pm Noon")
    elif 12<i<24:
        print(f"{i}Pm")
    
