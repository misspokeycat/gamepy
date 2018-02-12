# 8-bit ops
def incB(gb):
    return "INC B"
def incD(gb):
    return "INC D"
def incH(gb):
    return "INC H"
def incHL_8(gb):
    return "INC (HL)"

def incC(gb):
    return "INC C"
def incE(gb):
    return "INC E"
def incL(gb):
    return "INC L"
def incA(gb):
    return "INC A"

def decB(gb):
    return "DEC B"
def decD(gb):
    return "DEC D"
def decH(gb):
    return "DEC H"
def decHL_8(gb):
    return "DEC (HL)"

def decC(gb):
    return "DEC C"
def decE(gb):
    return "DEC E"
def decL(gb):
    return "DEC L"
def decA(gb):
    return "DEC A"

def addA_B(gb):
	return "ADD A,B"
def addA_C(gb):
	return "ADD A,C"
def addA_D(gb):
	return "ADD A,D"
def addA_E(gb):
	return "ADD A,E"
def addA_H(gb):
	return "ADD A,H"
def addA_L(gb):
	return "ADD A,L"
def addA_HL(gb):
	return "ADD A,(HL)"
def addA_A(gb):
	return "ADD A,A"
def adcA_B(gb):
	return "ADD A,B"
def adcA_C(gb):
	return "ADD A,C"
def adcA_D(gb):
	return "ADC A,D"
def adcA_E(gb):
	return "ADC A,E"
def adcA_H(gb):
	return "ADC A,H"
def adcA_L(gb):
	return "ADC A,L"
def adcA_HL(gb):
	return "ADC A,(HL)"
def adcA_A(gb):
	return "ADC A,A"
def subB(gb):
	return "SUB B"
def subC(gb):
	return "SUB C"
def subD(gb):
	return "SUB D"
def subE(gb):
	return "SUB E"
def subH(gb):
	return "SUB H"
def subL(gb):
	return "SUB L"
def subHL(gb):
	return "SUB HL"
def subA(gb):
	return "SUB A"
def sbcA_B(gb):
	return "SBC A,B"
def sbcA_C(gb):
	return "SBC A,C"
def sbcA_D(gb):
	return "SBC A,D"
def sbcA_E(gb):
	return "SBC A,E"
def sbcA_H(gb):
	return "SBC A,H"
def sbcA_L(gb):
	return "SBC A,L"
def sbcA_HL(gb):
	return "SBA A,(HL)"
def sbcA_A(gb):
	return "SBC A,A"
def andB(gb):
	return "AND B"
def andC(gb):
	return "AND C"
def andD(gb):
	return "AND D"
def andE(gb):
	return "AND E"
def andH(gb):
	return "AND H"
def andL(gb):
	return "AND L"
def andHL(gb):
	return "AND (HL)"
def andA(gb):
	return "AND A"
def xorB(gb):
	return "XOR B"
def xorC(gb):
	return "XOR C"
def xorD(gb):
	return "XOR D"
def xorE(gb):
	return "XOR E"
def xorH(gb):
	return "XOR H"
def xorL(gb):
	return "XOR L"
def xorHL(gb):
	return "XOR (HL)"
def xorA(gb):
	return "XOR A"
def orB(gb):
	return "OR B"
def orC(gb):
	return "OR C"
def orD(gb):
	return "OR D"
def orE(gb):
	return "OR E"
def orH(gb):
	return "OR H"
def orL(gb):
	return "OR L"
def orHL(gb):
	return "OR (HL)"
def orA(gb):
	return "OR A"
def cpB(gb):
	return "CP B"
def cpC(gb):
	return "CP C"
def cpD(gb):
	return "CP D"
def cpE(gb):
	return "CP E"
def cpH(gb):
	return "CP H"
def cpL(gb):
	return "CP L"
def cpHL(gb):
	return "CP (HL)"
def cpA(gb):
	return "CP (A)"

# 16-bit ops
def incBC(gb):
    return "INC BC"
def incDE(gb):
    return "INC DE"
def incHL(gb):
    return "INC HL"
def incSP(gb):
    return "INC SP"

def addHL_BC(gb):
    return "ADD HL,BC"
def addHL_DE(gb):
    return "ADD HL,DE"
def addHL_HL(gb):
    return "ADD HL,HL"
def addHL_SP(gb):
    return "ADD HL,SP"

def decBC(gb):
    return "DEC BC"
def decDE(gb):
    return "DEC DE"
def decHL(gb):
    return "DEC HL"
def decSP(gb):
    return "DEC SP"

# Constants
def adcA_P(gb, param):
    return "ACD A," + hex(param)
def sbcA_P(gb, param):
    return "SBC A," + hex(param)
def xorP(gb, param):
    return "XOR " + hex(param)
def cpP(gb, param):
    return "CP " + hex(param)