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
    return rules


# def generate_seq_facts(M):
#   facts = list(range(0, M))
#  shuffle(facts)
#  return facts


def generate_rand_facts(code_max, M):
    facts = []
    for i in range(0, M):
        facts.append(randint(0, code_max))
    return facts


def evidence_check(facts, rules_list, result_list) -> []:
    s_list = [[], [], []]  # or and not
    result = []
    it = 0
    # create list or and not
    for rule in rules_list:
        if rule != {}:
            for key in rule['if'].keys():
                if key == 'or':
                    s_list[0].append(rule)
                if key == 'and':
                    s_list[1].append(rule)
                if key == 'not':
                    s_list[2].append(rule)
    for rule in s_list[0]:  # or
        for item in rule['if']['or']:
            size = len(rule['if']['or'])
            if item in facts:
                result.append(rule['then'])
                it = 0
                break
            else:
                it += 1
                if it == size:
                    result.append(0)
                    it = 0

    for rule in s_list[2]:  # not
        for item in rule['if']['not']:
            size = len(rule['if']['not'])
            if item not in facts:
                it += 1
        if it == size:
            result.append(rule['then'])
            it = 0
        else:
            result.append(0)
            it = 0
    print(result)


def main():
    # samples:
    # print(generate_simple_rules(100, 4, 10), end='\n\n')
    # print(generate_random_rules(100, 4, 10), end='\n\n')
    # print(generate_stairway_rules(100, 4, 10, ["or"]), end='\n\n')
    # print(generate_ring_rules(100, 4, 10, ["or"]), end='\n\n')

    # generate rules and facts and check time
    time_start = time()
    N = 100000
    M = 1000
    rules = generate_simple_rules(100, 4, N)
    facts = generate_rand_facts(100, M)
    # print(len(facts))
    print("%d rules generated in %f seconds" % (N, time() - time_start))

    result_list = [0 for i in range(0, 10000)]
    evidence_check(facts, rules,result_list)

    time_start = time()
    # check facts vs rules
    # YOUR CODE HERE

    print("%d facts validated vs %d rules in %f seconds" % (M, N, time() - time_start))


if __name__ == "__main__":
    main()
