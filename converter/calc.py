def doll_to_real(value, cot):
    calc = value * cot
    print (f"The conversion of US${value} from Dollar to Real is R${calc}")

def real_to_doll(value, cot):
    calc = value / cot
    print (f"The conversion of R${value} from Real to Dollar is US${calc}")