# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć

elements = [1, 'allo', 123, 1.34, {00}, (1-2), [12], 12, 0, 'error']

for elem in elements:
    try:
        result = 10 /elem
    except (TypeError, ZeroDivisionError):
        print(f'{elem} - nie może być dzielnikiem')
    except:
        print('Nie spodziewany bład')

    print ('Koniec')

