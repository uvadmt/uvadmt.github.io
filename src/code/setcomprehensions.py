k = 23
fizzbuzz = [ print(s + " ") for s in [ "fizzbuzz" if n % 15 == 0 else "buzz" if n % 5 == 0 else "fizz" if n % 3 == 0 else str(n) 
                        for n in range(k) ]]