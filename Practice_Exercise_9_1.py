def ask():
    ins = input("Hoeveel personen? ")
    try:
        i = int(ins)
        if i < 0:
            print('Negatieve getallen mag niet')
            return
        print(4356/i)
        return
    except ZeroDivisionError:
        print('Delen door 0 mag niet')
        return
    except ValueError:
        print('Gebruik cijfers geen letters')
        return
    except Exception:
        print('probeer opnieuw, de invoer is niet juist')
        return

ask()