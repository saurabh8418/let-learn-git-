
class binaryadd:
    def binary(self, a:str , b:str)->str:
        carry =0
        result=" "
        a =list(str(a))
        b =list(str(b))
        while a or b or carry == 1:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry%2)
            carry= carry//2
        return result[::-1]

xyz = binaryadd()
print (xyz.binary(1,101))
