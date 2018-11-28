import sumavg

name, num1, num2, num3 = sumavg.load()
sum, avg = sumavg.calc(num1, num2, num3)
sumavg.output(name, num1, num2, num3, sum, avg)
