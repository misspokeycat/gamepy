# 1 Param
def ldB_P(param):
	return "LD B," + hex(param)
def ldD_P(param):
	return "LD D," + hex(param)
def ldH_P(param):
	return "LD H," + hex(param)
def ldHL_P(param):
	return "LD (HL)," + hex(param)

def ldC_P(param):
	return "LD C," + hex(param) 
def ldE_P(param):
	return "LD E," + hex(param) 
def ldL_P(param):
	return "LD L," + hex(param) 
def ldA_P(param):
	return "LD A," + hex(param) 

def ldhP_A(param):
	return "LDH " + hex(param) + ",A"
def ldhA_P(param):
	return "LDH A," + hex(param)

def ldP_SP(param):
	return "LD " + hex(param) + ",SP"

# 2 (16 bit) param
def ldP_A16(param):
	return  "LD " + hex(param) + ",A"
def ldA_P16(param):
	"LD A," + hex(param)

# No params
def ldBC_A():
	return "LD (BC),A"
def ldDE_A():
	return "LD (DE),A"
def ldHLp_A():
	return "LD (HL+),A"
def ldHLm_A():
	return "LD (HL-),A"
def ldA_BC():
	return "LD A,(BC)"
def ldA_DE():
	return "LD A,(DE)"
def ldA_HLp():
	return "LD A,(HL+)"
def ldA_HLm():
	return "LD A,(HL-)"
def ldB_B():
	return "LD B,B"
def ldB_C():
	return "LD B,C"
def ldB_D():
	return "LD B,D"
def ldB_E():
	return "LD B,E"
def ldB_H():
	return "LD B,H"
def ldB_L():
	return "LD B,L"
def ldB_HL():
	return "LD B,HL"
def ldB_A():
	return "LD B,A"
def ldC_B():
	return "LD C,B"
def ldC_C():
	return "LD C,C"
def ldC_D():
	return "LD C,D"
def ldC_E():
	return "LD C,E"
def ldC_H():
	return "LD C,H"
def ldC_L():
	return "LD C,L"
def ldC_HL():
	return "LD C,(HL)"
def ldC_A():
	return "LD C,A"
def ldD_B():
	return "LD D,B"
def ldD_C():
	return "LD D,C"
def ldD_D():
	return "LD D,D"
def ldD_E():
	return "LD D,E"
def ldD_H():
	return "LD D,H"
def ldD_L():
	return "LD D,L"
def ldD_HL():
	return "LD D,(HL)"
def ldD_A():
	return "LD D,A"
def ldE_B():
	return "LD E,B"
def ldE_C():
	return "LD E,C"
def ldE_D():
	return "LD E,D"
def ldE_E():
	return "LD E,E"
def ldE_H():
	return "LD E,H"
def ldE_L():
	return "LD E,L"
def ldE_HL():
	return "LD E,(HL)"
def ldE_A():
	return "LD E,A"
def ldH_B():
	return "LD H,B"
def ldH_C():
	return "LD H,C"
def ldH_D():
	return "LD H,D"
def ldH_E():
	return "LD H,E"
def ldH_H():
	return "LD H,H"
def ldH_L():
	return "LD H,L"
def ldH_HL():
	return "LD H,(HL)"
def ldH_A():
	return "LD H,A"
def ldL_B():
	return "LD L,B"
def ldL_C():
	return "LD L,C"
def ldL_D():
	return "LD L,D"
def ldL_E():
	return "LD L,E"
def ldL_H():
	return "LD L,H"
def ldL_L():
	return "LD L,L"
def ldL_HL():
	return "LD L,(HL)"
def ldL_A():
	return "LD L,A"
def ldHL_B():
	return "LD (HL),B"
def ldHL_C():
	return "LD (HL),C"
def ldHL_D():
	return "LD (HL),D"
def ldHL_E():
	return "LD (HL),E"
def ldHL_H():
	return "LD (HL),F"
def ldHL_L():
	return "LD (HL),G"
def halt():
    return "HALT"
def ldHL_A():
	return "LD (HL),A"
def ldA_B():
	return "LD A,B"
def ldA_C():
	return "LD A,C"
def ldA_D():
	return "LD A,D"
def ldA_E():
	return "LD A,E"
def ldA_H():
	return "LD A,H"
def ldA_L():
	return "LD A,L"
def ldA_HL():
	return "LD A,(HL)"
def ldA_A():
	return "LD A,A"