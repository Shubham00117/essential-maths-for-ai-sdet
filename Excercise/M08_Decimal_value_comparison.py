import pytest
num1 = 0.1 + 0.2
num2 = 0.1 + 0.3
num3 = 0.1 + 0.4
num4 = 0.1 + 0.5
num4 = 0.1 + 0.6
num5 = 0.1 + 0.32
print(num1)#0.30000000000000004
print(num2)#0.4
print(num3)#0.5
print(num4)#0.6
print(num5)#0.42000000000000004

if num1 == 0.3:
    print("Equal")
else:
    print("Not Equal")
    # As an SDET, using pytest.approx is the industry standard for assertions in test suites.


if num1 == pytest.approx(0.3):
    print("Equal (Industry standard for SDETs using pytest.approx)")
else:
    print("Not Equal (Industry standard for SDETs using pytest.approx)")





