hrs = input("Enter Hours: ")
rte = input("Enter Rate: ")
try:
    fh = float(hrs)
    fr = float(rte)
except:
    print("Error, please enter numeric input")
    quit()
print(fh, fr)

if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    py = reg + otp
else:
    py = fh * fr
    print("Pay:",py)