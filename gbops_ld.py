# 1 Param
def ldB_P(gb, param):
	return "LD B," + hex(param)
def ldD_P(gb, param):
	return "LD D," + hex(param)
def ldH_P(gb, param):
	return "LD H," + hex(param)
def ldHL_P(gb, param):
	return "LD (HL)," + hex(param)

def ldC_P(gb, param):
	return "LD C," + hex(param) 
def ldE_P(gb, param):
	return "LD E," + hex(param) 
def ldL_P(gb, param):
	return "LD L," + hex(param) 
def ldA_P(gb, param):
	return "LD A," + hex(param) 

def ldhP_A(gb, param):
	return "LDH " + hex(param) + ",A"
def ldhA_P(gb, param):
	return "LDH A," + hex(param)

def ldP_SP(gb, param):
	return "LD " + hex(param) + ",SP"

# 2 (16 bit) param
def ldP_A16(gb, param):
	return  "LD " + hex(param) + ",A"
def ldA_P16(gb, param):
	"LD A," + hex(param)

# No params
def ldBC_A(gb):
	return "LD (BC),A"
def ldDE_A(gb):
	return "LD (DE),A"
def ldHLp_A(gb):
	return "LD (HL+),A"
def ldHLm_A(gb):
	return "LD (HL-),A"
def ldA_BC(gb):
	return "LD A,(BC)"
def ldA_DE(gb):
	return "LD A,(DE)"
def ldA_HLp(gb):
	return "LD A,(HL+)"
def ldA_HLm(gb):
	return "LD A,(HL-)"
def ldB_B(gb):
	return "LD B,B"
def ldB_C(gb):
	return "LD B,C"
def ldB_D(gb):
	return "LD B,D"
def ldB_E(gb):
	return "LD B,E"
def ldB_H(gb):
	return "LD B,H"
def ldB_L(gb):
	return "LD B,L"
def ldB_HL(gb):
	return "LD B,HL"
def ldB_A(gb):
	return "LD B,A"
def ldC_B(gb):
	return "LD C,B"
def ldC_C(gb):
	return "LD C,C"
def ldC_D(gb):
	return "LD C,D"
def ldC_E(gb):
	return "LD C,E"
def ldC_H(gb):
	return "LD C,H"
def ldC_L(gb):
	return "LD C,L"
def ldC_HL(gb):
	return "LD C,(HL)"
def ldC_A(gb):
	return "LD C,A"
def ldD_B(gb):
	return "LD D,B"
def ldD_C(gb):
	return "LD D,C"
def ldD_D(gb):
	return "LD D,D"
def ldD_E(gb):
	return "LD D,E"
def ldD_H(gb):
	return "LD D,H"
def ldD_L(gb):
	return "LD D,L"
def ldD_HL(gb):
	return "LD D,(HL)"
def ldD_A(gb):
	return "LD D,A"
def ldE_B(gb):
	return "LD E,B"
def ldE_C(gb):
	return "LD E,C"
def ldE_D(gb):
	return "LD E,D"
def ldE_E(gb):
	return "LD E,E"
def ldE_H(gb):
	return "LD E,H"
def ldE_L(gb):
	return "LD E,L"
def ldE_HL(gb):
	return "LD E,(HL)"
def ldE_A(gb):
	return "LD E,A"
def ldH_B(gb):
	return "LD H,B"
def ldH_C(gb):
	return "LD H,C"
def ldH_D(gb):
	return "LD H,D"
def ldH_E(gb):
	return "LD H,E"
def ldH_H(gb):
	return "LD H,H"
def ldH_L(gb):
	return "LD H,L"
def ldH_HL(gb):
	return "LD H,(HL)"
def ldH_A(gb):
	return "LD H,A"
def ldL_B(gb):
	return "LD L,B"
def ldL_C(gb):
	return "LD L,C"
def ldL_D(gb):
	return "LD L,D"
def ldL_E(gb):
	return "LD L,E"
def ldL_H(gb):
	return "LD L,H"
def ldL_L(gb):
	return "LD L,L"
def ldL_HL(gb):
	return "LD L,(HL)"
def ldL_A(gb):
	return "LD L,A"
def ldHL_B(gb):
	return "LD (HL),B"
def ldHL_C(gb):
	return "LD (HL),C"
def ldHL_D(gb):
	return "LD (HL),D"
def ldHL_E(gb):
	return "LD (HL),E"
def ldHL_H(gb):
	return "LD (HL),F"
def ldHL_L(gb):
	return "LD (HL),G"
def halt(gb):
    return "HALT"
def ldHL_A(gb):
	return "LD (HL),A"
def ldA_B(gb):
	return "LD A,B"
def ldA_C(gb):
	return "LD A,C"
def ldA_D(gb):
	return "LD A,D"
def ldA_E(gb):
	return "LD A,E"
def ldA_H(gb):
	return "LD A,H"
def ldA_L(gb):
	return "LD A,L"
def ldA_HL(gb):
	return "LD A,(HL)"
def ldA_A(gb):
	return "LD A,A"