# OWASP-Why-Random-Matters demo
from MT19937 import Random

if __name__ == "__main__":
    rnd = Random (100)
    print rnd.get()