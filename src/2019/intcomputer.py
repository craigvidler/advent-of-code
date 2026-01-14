from inspect import signature

# TODO: runs slow, especially noticeable for Day 2 Part 2

# modes
POSITION = 0
IMMEDIATE = 1


class IntComputer:
    def __init__(self, program, input_=None):
        self.program = program
        self.input = input_
        self.output = []
        self.ptr = 0
        self.static_params = self.get_static_params()
        self.running = False

    def op1(self, a, b, address):  # add
        self.program[address] = a + b

    def op2(self, a, b, address):  # multiply
        self.program[address] = a * b

    def op3(self, address):  # input
        self.program[address] = self.input

    def op4(self, output):  # output
        self.output.append(output)

    def op5(self, a, b):  # jump if true (overriding default pointer advance)
        if a:
            self.ptr = b

    def op6(self, a, b):  # jump if false (overriding default pointer advance)
        if not a:
            self.ptr = b

    def op7(self, a, b, address):  # less than
        self.program[address] = 1 if a < b else 0

    def op8(self, a, b, address):  # equals
        self.program[address] = 1 if a == b else 0

    def op99(self):  # halt
        """
        Raise error if any output value except last is non-zero; exit main
        loop.
        """
        assert all(n == 0 for n in self.output[:-1])
        self.running = False

    def get_static_params(self):
        """
        Get the `op*` methods in self, and for each add to the list the opcode
        and param position if the param is specified as `address`, meaning
        it's not to be modified. Return a list of tuples [(opcode, param
        position), …].
        """
        out = []
        ops = [att for att in dir(self) if att.startswith('op')]
        for op in ops:
            func = getattr(self, op)
            opcode = int(op[2:])
            params = signature(func).parameters.keys()
            static_params = [(opcode, i)
                             for i, param in enumerate(params) if param == 'address']
            out.extend(static_params)
        return out

    def parse_instruction(self):
        """return (opcode, param 3 mode, param 2 mode, param 1 mode)"""
        instr = f'{self.program[self.ptr]:05}'
        self.ptr += 1  # advance pointer once instruction is read
        return (int(instr[3:]), int(instr[2]), int(instr[1]), int(instr[0]))

    def modify_params(self, opcode, params, modes):
        """
        If a param is specified as an `address` in `op*` signature above, or
        its mode is given in the instruction as 1/'immediate', leave as is.
        If it's not an `address` but an operand (`a`, `b`) or `output`, and
        the mode is 0/'position', treat the param as a reference to an
        address and replace param with the value found there.
        """
        for i, (param, mode) in enumerate(zip(params, modes)):
            if (opcode, i) not in self.static_params and mode == POSITION:
                params[i] = (self.program[param])

    def build_op(self, opcode, modes):
        """
        Look up operation corresponding to `opcode`, count its parameters
        (-1 for `self`), get a corresponding number of params from the
        program, advance pointer, modify params according to `modes` from
        instruction, return operation method and params ready for execution.
        """
        op = getattr(self, f'op{opcode}')
        argcount = op.__code__.co_argcount - 1
        params = self.program[self.ptr: self.ptr + argcount]
        self.ptr += argcount
        self.modify_params(opcode, params, modes)
        return op, params

    def run(self):
        """
        Main loop. Get opcode and modes from instruction, advance pointer, get
        right method and params (modified depending on modes), advance pointer,
        execute operation.
        """
        self.running = True
        while self.running:
            opcode, *modes = self.parse_instruction()
            op, params = self.build_op(opcode, modes)
            op(*params)

        if self.output:
            return self.output[-1]
