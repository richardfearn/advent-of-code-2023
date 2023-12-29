import math
from collections import deque, defaultdict
from enum import Enum

BUTTON = "button"
BROADCASTER = "broadcaster"

Pulse = Enum("Pulse", ["LOW", "HIGH"])
LOW, HIGH = list(Pulse)

FlipFlopState = Enum("FlipFlopState", ["OFF", "ON"])
OFF, ON = list(FlipFlopState)


class ModuleConfiguration:
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods

    def __init__(self, lines):
        lines = [line.split(" -> ") for line in lines]

        cables = {line[0]: line[1].split(", ") for line in lines}

        self.flip_flop_modules = set(module[1:] for module in cables.keys() if module.startswith("%"))
        self.conjunction_modules = set(module[1:] for module in cables.keys() if module.startswith("&"))

        self.cables = {module.lstrip("%&"): destinations for (module, destinations) in cables.items()}

        self.cables[BUTTON] = {BROADCASTER}

        self.flip_flop_states = {module: OFF for module in self.flip_flop_modules}

        inputs = defaultdict(set)
        for module, destinations in self.cables.items():
            for destination in destinations:
                inputs[destination].add(module)

        self.conjunction_inputs = {cm: {m: LOW for m in inputs[cm]} for cm in self.conjunction_modules}

        self.pulse_counts = {low_or_high: 0 for low_or_high in (LOW, HIGH)}
        self.received_low_pulse = set()

        self.pulses = deque()

    def push_button(self):
        self._send_pulse(BUTTON, LOW)

        while len(self.pulses) > 0:

            current_pulse = self.pulses.popleft()
            source, low_or_high, receiver = current_pulse

            self.pulse_counts[low_or_high] += 1

            if low_or_high == LOW:
                self.received_low_pulse.add(receiver)

            if receiver == BROADCASTER:
                self._send_pulse(receiver, low_or_high)

            elif receiver in self.flip_flop_modules:
                if low_or_high == LOW:
                    self.flip_flop_states[receiver] = ON if (self.flip_flop_states[receiver] == OFF) else OFF
                    pulse_to_send = HIGH if (self.flip_flop_states[receiver] == ON) else LOW
                    self._send_pulse(receiver, pulse_to_send)

            elif receiver in self.conjunction_modules:
                self.conjunction_inputs[receiver][source] = low_or_high
                remembers_high_pulses_for_all_inputs = LOW not in self.conjunction_inputs[receiver].values()
                pulse_to_send = LOW if remembers_high_pulses_for_all_inputs else HIGH
                self._send_pulse(receiver, pulse_to_send)

    def _send_pulse(self, source, pulse_type):
        self.pulses.extend((source, pulse_type, destination) for destination in self.cables[source])


def part_1_answer(lines):
    config = ModuleConfiguration(lines)

    for _ in range(1000):
        config.push_button()

    return math.prod(config.pulse_counts.values())


def part_2_answer(lines):
    config = ModuleConfiguration(lines)

    # I created a Graphviz diagram from the nodes/edges, and could see there were 4 subgroups of modules, with
    # the broadcaster sending a pulse to each one. I could also see each subgroup was connected to a module
    # (sh / bh / mz / jf) which in turn connected to mf, and mf connected to rx.

    # I thought that each subgroup might send a pulse towards mf/rx every X button presses (with a different value of X
    # for each subgroup), and that the answer would be the least common multiple of all those values of X.

    targets = {"sh", "bh", "mz", "jf"}
    button_presses_to_first_low = {}

    button_presses = 0

    while len(button_presses_to_first_low) < 4:

        config.push_button()
        button_presses += 1

        targets_sent_low_pulses = config.received_low_pulse & targets
        for t in targets_sent_low_pulses:
            if t not in button_presses_to_first_low:
                button_presses_to_first_low[t] = button_presses

    return math.lcm(*button_presses_to_first_low.values())
