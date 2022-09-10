from random import choice, shuffle, randint
from time import time
import re


def generate_simple_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': code_max + j
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_stairway_rules(n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(i + j)
        rule = {
            'if': {
                log_oper: items
            },
            'then': i + j + 1
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_ring_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = generate_stairway_rules(code_max, n_max, n_generate - 1, log_oper_choice)
    log_oper = choice(log_oper_choice)  # not means and-not (neither)
    if n_max < 2:
        n_max = 2
    n_items = randint(2, n_max)
    items = []
    for i in range(0, n_items):
        items.append(code_max - i)
    rule = {
        'if': {
            log_oper: items
        },
        'then': 0
    }
    rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_random_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': randint(1, code_max)
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_seq_facts(M):
    facts = list(range(0, M))
    shuffle(facts)
    return facts


def generate_rand_facts(code_max, M):
    facts = []
    for i in range(0, M):
        facts.append(randint(0, code_max))
    return facts


def one_evidence_check(in_value , rules_list, res_list) -> []:
    condition = rules_list[0].get('if')
    logical_operand = list(condition.keys())[0]
    print(logical_operand)
    tolerance_range = condition.get(logical_operand)
    print(tolerance_range)
    if logical_operand == 'or' and in_value in tolerance_range:
        print("1")
        pass
    if logical_operand == 'and':#?????????????? something going wrong
        pass
    if logical_operand == 'not':
        pass
    result = rules_list[0]['then']


def main():
    # samples:
    # print(generate_simple_rules(100, 4, 10), end='\n\n')
    # print(generate_random_rules(100, 4, 10), end='\n\n')
    # print(generate_stairway_rules(100, 4, 10, ["or"]), end='\n\n')
    # print(generate_ring_rules(100, 4, 10, ["or"]), end='\n\n')

    # generate rules and facts and check time
    time_start = time()
    N = 100000
    M = 100000
    rules = generate_simple_rules(100, 4, N)
    facts = generate_rand_facts(100, M)
    # print(len(facts))
    print("%d rules generated in %f seconds" % (N, time() - time_start))

    result_list = [0 for i in range(0, 10000)]
    value = 50
    one_evidence_check(value, rules, result_list)
    number_for_validate = 10

    time_start = time()
    # check facts vs rules
    # YOUR CODE HERE

    print("%d facts validated vs %d rules in %f seconds" % (M, N, time() - time_start))


if __name__ == "__main__":
    main()
