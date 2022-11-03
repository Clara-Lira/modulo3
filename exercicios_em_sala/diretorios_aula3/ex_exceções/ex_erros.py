try:
    print(100/1)
except Exception as error:
    print(error)

except FileNotFoundError as error:
    print(error)

except ZeroDivisionError as error:
    print(error)

else:
    print("execute o programa novamente")