#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    def magic_calculation(a, b):
        return (a, b)
    dis.dis(magic_calculation)