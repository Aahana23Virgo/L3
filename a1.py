def prints(n):
    if n<= 0:
        return
    
    print("Codingal")
    prints(n // 2)
    prints(n // 2)

prints(4)
#Time complexity=T(n/2)+T(n/2)+T(n)