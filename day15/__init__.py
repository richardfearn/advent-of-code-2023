from collections import OrderedDict


def part_1_answer(line):
    return sum(calculate_hash(step) for step in line.split(","))


def calculate_hash(s):
    current_value = 0
    for c in s:
        ascii_code = ord(c)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


def part_2_answer(line):
    boxes = [OrderedDict() for _ in range(256)]
    apply_steps(boxes, line.split(","))
    return total_focusing_power(boxes)


def apply_steps(boxes, steps):
    for step in steps:

        if "=" in step:
            label, new_value = step.split("=")
            new_value = int(new_value)
        else:
            label, new_value = step[:-1], None

        box = boxes[calculate_hash(label)]

        if new_value is None:
            box.pop(label, None)
        else:
            box[label] = new_value


def total_focusing_power(boxes):
    total = 0
    for box_num, box in enumerate(boxes):
        for slot_num, (_, focal_length) in enumerate(box.items()):
            focusing_power = (1 + box_num) * (slot_num + 1) * focal_length
            total += focusing_power
    return total
