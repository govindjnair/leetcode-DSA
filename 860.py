bills = [5, 5, 5, 10, 20]


def lemonade(bills):
    price = 5
    counter = {
        "five": 0,
        "ten": 0,
        "twenty": 0
    }
    status = False
    for bill in bills:
        if bill == 5:
            counter["five"] += 5
            status = True
            print(status)
        elif bill == 10:
            change = bill - price
            if counter["five"] >= change:
                counter["five"] -= change
                counter["ten"] += 10
                status = True
                print(status)
            else:
                return False
        else:
            change = bill - price
            if counter["ten"] > 0:
                if counter["five"] >= 5:
                    counter["ten"] -= 10
                    counter["five"] -= 5
                    counter["twenty"] += 20
                    status = True
                    print(status)
                else:
                    return False

            elif counter["five"] >= change:
                counter["five"] -= change
                counter["twenty"] += 20
                status = True
                print(status)
            else:
                return False

    return status


print(lemonade(bills))
