hrs = input("Enter Hours: ")
rte = input("Enter Rate: ")
fh = float(hrs)
fr = float(rte)

if fh > 40 :
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    py = reg + otp
    print("Pay:",py)
else:
    print("Regular")
    py = fh * fr
    print("Pay:",py)