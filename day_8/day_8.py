from typing import Tuple, List


def parse_instruction(inst: str) -> Tuple[str, int]:
    """
    'acc +1' -> ('acc', 1)
    'jmp -3' -> ('jmp', -3)
    :param inst:
    :return:
    """
    inst_splt = inst.split(' ')
    return inst_splt[0], int(inst_splt[1])


def nop(accum: int, pos: int, *args) -> Tuple[int, int]:
    """
    update instruction accumulator and position for nop
    :param pos:
    :param accum:
    :return:
    """

    return accum, pos + 1


def acc(accum: int, pos: int, value) -> Tuple[int, int]:
    """
    update instruction accumulator and position for acc
    :param accum:
    :param pos:
    :param value:
    :return:
    """
    return accum + value, pos + 1


def jmp(accum: int, pos: int, value) -> Tuple[int, int]:
    """
    update instruction accumulator and position for jmp
    :param accum:
    :param pos:
    :param value:
    :return:
    """
    return accum, pos + value


def update_accumulator_and_pos(accum: int, pos:int, inst_str: str) -> Tuple[int, int]:
    """

    :param accum:
    :param pos:
    :param inst_str:
    :return:
    """
    switcher = {
        'nop': nop,
        'jmp': jmp,
        'acc': acc
    }

    inst, val = parse_instruction(inst_str)
    return switcher.get(inst)(accum, pos, val)


def acc_val_bfr_frst_recurring_inst_or_prg_term(inst_set: List[str]) -> Tuple[int, List[Tuple[int, str]], bool]:
    """

    :param inst_set:
    :return:
    """
    accumulator = 0
    position = 0
    pos_mem = [0]
    inst_mem = []
    program_terminated = True

    while position < len(inst_set):
        pos_inst_tup = position, inst_set[position]
        inst_mem.append(pos_inst_tup)
        accumulator, position = update_accumulator_and_pos(accumulator, *pos_inst_tup)

        if position in pos_mem:
            program_terminated = False
            break
        else:
            pos_mem.append(position)

    return accumulator, inst_mem, program_terminated


def swap_jmp_nop(inst: str) -> str:
    """

    :param inst:
    :return:
    """
    if parse_instruction(inst)[0] == 'jmp':
        return inst.replace('jmp', 'nop')
    elif parse_instruction(inst)[0] == 'nop':
        return inst.replace('nop', 'jmp')
    else:
        return inst


def fix_wrong_inst_and_ret_accum_val(inst_set: List[str]) -> int:
    """

    :param inst_set:
    :return:
    """

    _, inst_set_mem, _ = acc_val_bfr_frst_recurring_inst_or_prg_term(inst_set)

    jmp_nop_inst = [inst for inst in inst_set_mem if parse_instruction(inst[1])[0] in ['jmp', 'nop']]

    for pos, inst in jmp_nop_inst:
        inst_set_fixed = inst_set.copy()
        inst_set_fixed[pos] = swap_jmp_nop(inst)

        accumulator, inst_set_mem, prg_term = acc_val_bfr_frst_recurring_inst_or_prg_term(inst_set_fixed)

        if prg_term:
            return accumulator


# %%

sample_input = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]

filename = "day_8/input.txt"
with open(filename) as f:
    input_data = f.readlines()

input_data = [(x.strip()) for x in input_data]

#%%
# part 1

ans, _, _ = acc_val_bfr_frst_recurring_inst_or_prg_term(input_data)
print(f'Value in the accumulator immediately before first recurring instruction: {ans}')

#%%
ans = fix_wrong_inst_and_ret_accum_val(input_data)
print(f'Value in the accumulator after program terminates: {ans}')
