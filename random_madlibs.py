from MADLIBS.sample_madlibs import hungergames
from MADLIBS.sample_madlibs import hp, code, zombie
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
