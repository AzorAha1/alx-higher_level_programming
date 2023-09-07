#!/usr/bin/python3
if __name__ == "__main__":
    from dis import dis
    def magic_calculation(a, b):
        return (a, b)
    dis(magic_calculation)