# 10. 클래스
    # 객체 정의 틀
    # 멤버 변수 + 멤버 함수

    # 생성자 : 객체가 생성될 때마다 자동으로 호출되는 멤버함수

class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    # 멤버함수 구현과 활용
    def speedUp(self): self.speed += 10

car1 = Car("black", 0)
car1.speedUp()
car1.color = "purple"

class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

# 11. 연산자 중복 overloading

    # 비교 연산자 == 중복
        # car1 == car2

    def __eq__(self, carB) : return self.color == carB.color

    # 문자열로 변환 연산자
        # print(car1)

    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)

    # 중복 가능한 연산자들~

    # private 멤버변수

class Student:
    def __init__(self, name, age):
        self.name = name # 인스턴스 변수
        self.__age = age # private 멤버변수

    def output(self):
        print("name: ", self.name)
        print("age: ", self.__age)

st1 = Student("ekgus9", 23)
st1.output()
st1.__age = 25
# print(st1.__age) # error

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    # 접근자와 설정자

    def getAge(self): # 접근자 : 멤버변수의 값을 읽는 함수
        return self.__age
    
    def setAge(self, age): # 설정자 : 멤버변수의 값을 수정하는 함수
        self.__age = age

st1.getAge()
st1.setAge()

    # 클래스 변수
        # 객체마다 생성 X <-> 인스턴스 변수
        # 멤버함수 밖에서 선언
        # 멤버함수에서 사용할 때는 클래스명.클래스변수

class Student:
    st_count = 0
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        Student.st_count += 1

    def getCount(self):
        return Student.st_count

        # st1.getCount() = st2.getCount() = st1.st_count = Student.st_count

# 12. 상속 inheritance
    # 기존 클래스로부터 멤버 추가해 새로운 클래스 만듬
    # 자식 클래스는 부모의 모든 멤버 상속

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo

    # 재정의 overriding
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()

# 연습문제1 : 은행 계좌 클래스 선언과 객체 생성

class BankAccount:
    def __init__(self, name, number, balance = 0):
        self.__name = name
        self.__number = number
        self.__balance = balance

    def deposit(self, val):
        self.__balance += val

    def withdraw(self, val):
        if self.__balance - val < 0:
            return False
        else:
            self.__balance -= val
            return True

    def __str__(self):
        return "name: %s number: %d balance: %d"% (self.__name, self.__number, self.__balance)

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getBalance(self):
        return self.__balance

# from 해당파일 import *

b1 = BankAccount("김철수", 10001, 30000)
b2 = BankAccount("이영희", 10002)
print(b1)
print(b2)

b1.deposit(150000)
print("\n김철수통장에 150000 입금")
print(b1)
b1.withdraw(50000)
print("김철수통장에 50000 출금")
print(b1)
b2.deposit(50000)
print("\n이영희통장에 50000 입금")
print(b2)
if b2.withdraw(100000) == False:
    print("이영희통장에 100000 출금")
    print("잔액부족")
    print(b2)
else :
    print("이영희통장에 100000 출금")
    print(b2)

print("\n%s"%(b2))
print(b2)

# 연습문제 2 : 은행계좌 상속

class BankAccount:
    def __init__(self, name, number, balance = 0):
        self.__name = name
        self.__number = number
        self.__balance = balance

    def deposit(self, val):
        self.__balance += val

    def withdraw(self, val):
        if self.__balance - val < 0:
            return False
        else:
            self.__balance -= val
            return True

    def __str__(self):
        return "name: %s number: %d balance: %d"% (self.__name, self.__number, self.__balance)

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

class SavingAccount(BankAccount):
    acc = 0
    def __init__(self, name, balance, inte):
        SavingAccount.acc += 1
        number = "01-{:03d}".format(SavingAccount.acc)
        super().__init__(name, number, balance)
        self.__inte = inte

    def inte_give(self):
        super().setBalance((super().getBalance() + (super().getBalance() * self.__inte)))

    def __str__(self):
        return "name: %s number: %s balance: %d interest: %0.2f"% (super().getName(), super().getNumber(), super().getBalance(),self.__inte)

class CheckingAccount(BankAccount):
    acc2 = 0
    def __init__(self, name, balance, ssl):
        CheckingAccount.acc2 += 1
        number = "02-{:03d}".format(CheckingAccount.acc2)
        super().__init__(name, number,balance)
        self.__ssl = ssl

    def ssl_give(self, val):
        if val + self.__ssl <= super().getBalance():
            super().setBalance((super().getBalance() - (val + self.__ssl)))
            return True
        else : return False

    def __str__(self):
        return "name: %s number: %s balance: %d fee: %d"% (super().getName(), super().getNumber(), super().getBalance(),self.__ssl)

b11 = SavingAccount("김철수",10000, 0.05)
b22 = SavingAccount("이영희",200000, 0.03)
b33 = CheckingAccount("홍길동",2000000,30000)

print("통장 초기값 출력")
print(b11)
print(b22)
print(b33)

print("\n김철수 50000 입금, 100000 출금")
b11.deposit(50000)
print(b11)
if b11.withdraw(100000) == False:
    print("잔액부족!!")
    print(b11)
else :
    print(b11)

print("\n이영희 100000 입금, 75000 출금")
b22.deposit(100000)
print(b22)
if b22.withdraw(75000) == False:
    print("잔액부족!!")
    print(b22)
else :
    print(b22)

print("\n홍길동 500000 입금")
b33.deposit(500000)
print(b33)

print("\n이자지급/ 당좌수표 1000000 발행")
print("계산전")
print(b11)
print(b22)
print(b33)

print("계산후")
b11.inte_give()
b22.inte_give()
b33.ssl_give(1000000)
print(b11)
print(b22)
print(b33)

# 과제

class Employee():
    def __init__(self, name, base, extra = 0):
        self.__name = name
        self.__base = base
        self.__extra = extra

    def calc_salary(self):
        return self.__base + self.__extra

    def plus_extra(self, num):
        self.__extra += num
    
    def __str__(self):
        return ( "이    름 : " + self.__name + "\n기 본 금 : " + str(self.__base ) 
        + "\n초과금액 : " + str(self.__extra) + "\n총 월 급 : " + str(Employee.calc_salary(self)) )

    def getName(self):
        return self.__name

    def getBase(self):
        return self.__base

    def getExtra(self):
        return self.__extra

class Manager(Employee):
    def __init__(self, name, base, add, extra = 0):
        super().__init__(name,base,extra)
        self.__add = add

    def calc_salary(self):
        return super().getBase() + super().getExtra() + self.__add

    def __str__(self):
        return ( "이    름 : " + super().getName() + "\n기 본 금 : " + str(super().getBase()) 
        + "\n초과금액 : " + str(super().getExtra()) + "\n추가수당 : " + str(self.__add) 
        + "\n총 월 급 : " + str(Manager.calc_salary(self)) )

e1 = Employee("홍길동",200)
e2 = Employee("이영희",220)
m1 = Manager("김철수",250,30)
print(e1)
print("================\n")
print(e2)
print("================\n")
print(m1)
print("================\n")

print("홍길동 : 초과근무액 50, 60 추가")
e1.plus_extra(50)
e1.plus_extra(60)
print(e1)
print("================\n")

print("이영희 : 초과근무액 60, 60, 60 추가")
e2.plus_extra(60)
e2.plus_extra(60)
e2.plus_extra(60)
print(e2)
print("================\n")

print("김철수 : 초과근무액 50, 50 추가")
m1.plus_extra(50)
m1.plus_extra(50)
print(m1)
print("================\n")
