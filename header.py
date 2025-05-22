# Header
from typing import *
from pair import *
from MathFunction import *


def HeaderUp1():
    print("+--------+---------+----------------------+")

def HeaderUp2():
    print("+--------+---------+----------------------+----------------------+")
    
def HeaderUp3():
    print("+--------+---------+----------------------+----------------------+----------------------+----------------------+")
    
def HeaderUp4():
    print("+---------------------+----------------------+----------------------+----------------------+")

def HeaderUp5():
    print("+---------------------+----------------------+---------+--------+")

def HeaderUp6():
    print("+---------------------+----------------------+---------+--------+--------------------------+")
    

def Tahap1Header():
    HeaderUp3()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} | {'Fitness':^20} | {'Cumulative':^20} | {'Interval':^20} |")
    HeaderUp3()
    
def Tahap2Header():
    HeaderUp4()
    print(f"|{'Kromosom Lama':^20} | {'Random R[k]':^20} | {'Interval':^20} | {'Kromosom Baru':^20} |")
    HeaderUp4() 
    
def TahapCrossOverHeader():
    HeaderUp5()
    print(f"|{'NO':^20} | {'Kromosom Baru':^20} | {'x1':^7} | {'x2':^7}|")
    HeaderUp5()
    
def TahapMutationHeader():
    print()
    print("Mutation")
    HeaderUp6()
    print(f"|{'NO':^20} | {'Kromosom Baru':^20} | {'x1':^7} | {'x2':^7}| {'Nilai Objective':^24} |")
    HeaderUp6()
    
def printTahap1(pairs: List[Pair], o: List[float], f: List[float], cum: List[float],interval: List[str], n:int) -> None:
    Tahap1Header()
    for i in range(n):
        print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {o[i]:^20} | {f[i]:^20} | {cum[i]:^20} | {interval[i]:^20} | ")
    HeaderUp3()
    
def printTahap2(parent) -> None:
    print()
    print("Parent Selection")
    Tahap2Header()
    for idx, r, interval, kromosom in parent:
        print(f"|{idx + 1:^20} | {r:^20} | {interval:^20} | {f'{idx+1} ({kromosom})':^20} | {Decode(kromosom[:5])} {Decode(kromosom[5:])}")
    HeaderUp4()

def printCrossOver(children) -> None:
    TahapCrossOverHeader()
    for idx, (kromosom_baru, x1, x2) in enumerate(children):
        print(f"|{f'Kromosom {idx+1}':^20} | {kromosom_baru:^20} | {x1:^7} | {x2:^7}|")
    HeaderUp5()
    
    
def printMutation(mutation) -> None:
    TahapMutationHeader()
    for idx, (krom, x1, x2) in enumerate(mutation):
        objective_value = CheckObjectiveFunction(x1, x2)
        print(f"|{f'Mutasi {idx+1}':^20} | {krom:^20} | {x1:^7} | {x2:^7}| {objective_value:^24} |")
    HeaderUp6()
    

    