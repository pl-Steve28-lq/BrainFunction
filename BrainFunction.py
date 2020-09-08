class BrainFunction:
    def __init__(self):
        self.values = [0]*256
        self.pointer = 0
        self.command = {}

    def loopHelper(self, code):
        book = {}
        p = []
        for i in range(len(code)):
            if code[i] == "[":
                p.append(i)
            elif code[i] == "]":
                book[p[-1]] = i
                book[i] = p[-1]
                p = p[:-1]
        return book

    def compile(self, code):
        if "\n" in code:
            code = code.split('\n')
            for i in code:
                if "=" in i: self.functionCompile(i)
                else: self.compile(i)
            return 0
        x = 0
        y = len(code)
        data = []
        cnt = 0
        z = self.loopHelper(code)
        while x < y:
            self.pointer = self.pointer % 256
            p = code[x]
            if p == "+": self.values[self.pointer] += 1
            elif p == "-": self.values[self.pointer] -= 1
            elif p == ">": self.pointer += 1
            elif p == "<": self.pointer -= 1
            elif p == "[": pass
            elif p == "]":
                if self.values[self.pointer]: x = z[x] - 1
            elif p == ".": data.append(chr(self.values[self.pointer]))
            elif p == ",": self.values[self.pointer] = ord(input()[0])
            elif p in self.command.keys(): self.compile(self.command[p])
            else: continue
            x+= 1
            cnt += 1

            if cnt > 100000: print("LoopError! : {} {}".format(x,z[x])); return 1
        if data: print(''.join(data))
        return 0

    def functionCompile(self, code):
        a = code.replace("{","").replace("}","").replace(" ","").split("=")
        if len(a) != 2 or a[0] in "+-><[].,=": print("Error!"); return 1
        self.command[a[0]] = a[1]
        return 0
