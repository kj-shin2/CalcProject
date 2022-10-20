## 함수 선언부
def add_fnc(n1,n2) :
    return n1+n2

def sub_fnc(n1,n2) :
    return n1-n2

def mul_fnc(n1,n2) :
    return n1*n2


def div_fnc(n1,n2) :
    return n1/n2

def doub_fnc(n1,n2) :
    return n1/n2

## 전역 변수부
num1, num2, res = 100,200,0

## 메인 코드부
res = add_fnc(num1,num2)
print(num1,"+",num2,"=",res)

res = sub_fnc(num1,num2)
print(num1,"-",num2,"=",res)

res = mul_fnc(num1,num2)
print(num1,"*",num2,"=",res)

res = div_fnc(num1,num2)
print(num1,"/",num2,"=",res)

res = div_fnc(num1,num2)
print(num1,"**",num2,"=",res)
