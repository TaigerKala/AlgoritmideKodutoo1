def fibonacci_rida(taisarv):
    if taisarv <= 1:
        return taisarv
    else:
        return fibonacci_rida(taisarv-1) + fibonacci_rida(taisarv-2)

print("Antud programm tagastab sinu valitud jarjekorra numbilise arvu Fibonacci reas")
taisarv = int(input("Sisesta 0-st suurem taisarv: "))

print(fibonacci_rida(taisarv))
