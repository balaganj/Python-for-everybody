def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40:
        regular = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = regular + otp
    else:
        pay = hours * rate
    # print("Returning",pay)
    return pay

hrs = input("Enter Hours: ")
rte = input("Enter Rate: ")
fh = float(hrs)
fr = float(rte)

py = computepay(fh, fr)

print("Pay:", py)
