def division (a,b):      #TryERROR
    try:
        if b==0:
            raise ZeroDivisionError('division by zero is not allowed')
        return a / b
    except ZeroDivisionError as e:
        print("exception is caught",e)
        raise
    except TypeError as f:
        print("exception is now caught",f)
    else:
        print("No Exceptions are caught")
    finally:
        print("Finally")

division(5,2)
print(division(5,2))
print(division(10,"ab"))
#TypeError