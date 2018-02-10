# 8-bit ops
def incB():
    return "INC B"
def incD():
    return "INC D"
def incH():
    return "INC H"
def incHL_8():
    return "INC (HL)"

def incC():
    return "INC C"
def incE():
    return "INC E"
def incL():
    return "INC L"
def incA():
    return "INC A"

def decB():
    return "DEC B"
def decD():
    return "DEC D"
def decH():
    return "DEC H"
def decHL_8():
    return "DEC (HL)"

def decC():
    return "DEC C"
def decE():
    return "DEC E"
def decL():
    return "DEC L"
def decA():
    return "DEC A"

def addA_B():
	return "ADD A,B"
def addA_C():
	return "ADD A,C"
def addA_D():
	return "ADD A,D"
def addA_E():
	return "ADD A,E"
def addA_H():
	return "ADD A,H"
def addA_L():
	return "ADD A,L"
def addA_HL():
	return "ADD A,(HL)"
def addA_A():
	return "ADD A,A"
def adcA_B():
	return "ADD A,B"
def adcA_C():
	return "ADD A,C"
def adcA_D():
	return "ADC A,D"
def adcA_E():
	return "ADC A,E"
def adcA_H():
	return "ADC A,H"
def adcA_L():
	return "ADC A,L"
def adcA_HL():
	return "ADC A,(HL)"
def adcA_A():
	return "ADC A,A"
def subB():
	return "SUB B"
def subC():
	return "SUB C"
def subD():
	return "SUB D"
def subE():
	return "SUB E"
def subH():
	return "SUB H"
def subL():
	return "SUB L"
def subHL():
	return "SUB HL"
def subA():
	return "SUB A"
def sbcA_B():
	return "SBC A,B"
def sbcA_C():
	return "SBC A,C"
def sbcA_D():
	return "SBC A,D"
def sbcA_E():
	return "SBC A,E"
def sbcA_H():
	return "SBC A,H"
def sbcA_L():
	return "SBC A,L"
def sbcA_HL():
	return "SBA A,(HL)"
def sbcA_A():
	return "SBC A,A"
def andB():
	return "AND B"
def andC():
	return "AND C"
def andD():
	return "AND D"
def andE():
	return "AND E"
def andH():
	return "AND H"
def andL():
	return "AND L"
def andHL():
	return "AND (HL)"
def andA():
	return "AND A"
def xorB():
	return "XOR B"
def xorC():
	return "XOR C"
def xorD():
	return "XOR D"
def xorE():
	return "XOR E"
def xorH():
	return "XOR H"
def xorL():
	return "XOR L"
def xorHL():
	return "XOR (HL)"
def xorA():
	return "XOR A"
def orB():
	return "OR B"
def orC():
	return "OR C"
def orD():
	return "OR D"
def orE():
	return "OR E"
def orH():
	return "OR H"
def orL():
	return "OR L"
def orHL():
	return "OR (HL)"
def orA():
	return "OR A"
def cpB():
	return "CP B"
def cpC():
	return "CP C"
def cpD():
	return "CP D"
def cpE():
	return "CP E"
def cpH():
	return "CP H"
def cpL():
	return "CP L"
def cpHL():
	return "CP (HL)"
def cpA():
	return "CP (A)"

# 16-bit ops
def incBC():
    return "INC BC"
def incDE():
    return "INC DE"
def incHL():
    return "INC HL"
def incSP():
    return "INC SP"

def addHL_BC():
    return "ADD HL,BC"
def addHL_DE():
    return "ADD HL,DE"
def addHL_HL():
    return "ADD HL,HL"
def addHL_SP():
    return "ADD HL,SP"

def decBC():
    return "DEC BC"
def decDE():
    return "DEC DE"
def decHL():
    return "DEC HL"
def decSP():
    return "DEC SP"

# Constants
def adcA_P(param):
    return "ACD A," + hex(param)
def sbcA_P(param):
    return "SBC A," + hex(param)
def xorP(param):
    return "XOR " + hex(param)
def cpP(param):
    return "CP " + hex(param)