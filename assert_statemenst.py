# method that receives an int and returns a list
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    # while True:
    #     try:
    #         num = int(input('Ingresa un número: '))
    #         if num < 0 or num == 0:
    #             raise ValueError
    #         print(divisors(num))
    #         print("Terminó mi programa")
    #         break
    #     except ValueError:
    #         print("Debes ingresar un entero positivo")

    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))   
    print("Terminó mi programa")


if __name__ == '__main__':
    run()
