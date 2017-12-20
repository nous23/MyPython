from itertools import permutations
from fractions import Fraction
from scipy.special import perm, comb
from math import factorial

NotSatisfied = 'not satisfied'
AllMutualExchange = 'all mutual exchange'
PartialMutualExchange = 'partial mutual exchange'
NoneMutualExchange = 'none mutual exchange'


def main():
    tests = list(range(4, 5))
    print('simulation\n')
    for test in tests:
        result, n_arrangements = traverse_arrangements(test)
        if not result:
            print('error when traverse_arrangements')
            return
        n_not_satisfied = len(result[NotSatisfied])
        n_all_mutual_exchange = len(result[AllMutualExchange])
        n_partial_mutual_exchange = len(result[PartialMutualExchange])
        n_none_mutual_exchange = len(result[NoneMutualExchange])
        print('n_arrangements: ', n_arrangements, '\nsum: ', n_not_satisfied + n_all_mutual_exchange +
              n_partial_mutual_exchange + n_none_mutual_exchange)
        print('n_none_mutual_exchange: ', repr(n_none_mutual_exchange))

    print('\n\nanalysis\n')
    for test in tests:
        analysis_result = analysis(test)
        print('n_none_mutual_exchange_analysis: ', repr(analysis_result[1]))


def traverse_arrangements(n_child):
    number = n_child
    gift_list = list(range(number))

    arrangements = permutations(gift_list, number)
    arrangements_list = list(arrangements)

    result_dic = {NotSatisfied: [],
                  AllMutualExchange: [],
                  PartialMutualExchange: [],
                  NoneMutualExchange: []}
    for arrangement in arrangements_list:
        if not is_satisfied(arrangement):
            result_dic[NotSatisfied].append(arrangement)
        else:
            if is_all_mutual_exchange(arrangement):
                result_dic[AllMutualExchange].append(arrangement)
            if is_partially_mutual_exchange(arrangement):
                result_dic[PartialMutualExchange].append(arrangement)
            if is_none_mutual_exchange(arrangement):
                result_dic[NoneMutualExchange].append(arrangement)

    for k, v in result_dic.items():
        if k == NoneMutualExchange:
            print(k + '\n')
            for arr in v:
                print(arr)
            print('\n')

    return result_dic, len(arrangements_list)


def is_satisfied(arrangements_tuple):
    for child, gift in enumerate(arrangements_tuple):
        if child == gift:
            return False
    return True


def is_all_mutual_exchange(arrangements_tuple):
    if len(arrangements_tuple) % 2 == 1:
        return False
    for child, gift in enumerate(arrangements_tuple):
        if arrangements_tuple[gift] != child:
            return False
    return True


def is_partially_mutual_exchange(arrangements_tuple):
    not_mutual_exchange = False
    mutual_exchange = False
    for child, gift in enumerate(arrangements_tuple):
        if not mutual_exchange and arrangements_tuple[gift] == child:
            mutual_exchange = True
        if not not_mutual_exchange and arrangements_tuple[gift] != child:
            not_mutual_exchange = True
        if not_mutual_exchange and mutual_exchange:
            return True
    return False


def is_none_mutual_exchange(arrangements_tuple):
    for child, gift in enumerate(arrangements_tuple):
        if arrangements_tuple[gift] == child:
            return False
    return True


def analysis(n_child):
    n_all_mutual_exchange = calc_all_mutual_exchange(n_child)
    n_none_mutual_exchange = calc_none_mutual_exchange(n_child)
    return [n_all_mutual_exchange, n_none_mutual_exchange]


def calc_all_mutual_exchange(n_child):
    n = n_child
    if n % 2 == 1:
        return 0
    result = 1
    while n > 0:
        result *= comb(n, 2)
        n -= 2
    return result / factorial(n_child / 2)


def calc_none_mutual_exchange(n_child):
    if n_child <= 2:
        return 0
    return factorial(n_child - 1)


if __name__ == '__main__':
    main()
