
def how_to_pay(amount, currency:list):

    currency.sort(reverse = True)
    left = amount
    c = 0
    result = dict()
    while left:

        delene, zvysok = divmod(left,currency[c])
        if zvysok==0: # and delene==1:
            result[currency[c]] = delene
            left = left - currency[c]*delene
            # break

        else:
            result[currency[c]] = delene
            left = left - currency[c]*delene
            c += 1

    return result
