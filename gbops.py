from gbops_cb import cbops
from gboplen import oplen
from gbops_stack import *
from gbops_ld import *
from gbops_arith import *

def padhexa(s):
    return '0x' + s[2:].zfill(2)


def nop(gb):
    return "NOP"

def stop(gb,param):
    return "STOP 0"

def ldBC(gb,param):
    return "LD BC," + hex(param)

def ldDE(gb,param):
    return "LD DE," + hex(param)

def ldHL(gb,param):
    return "LD HL," + hex(param)

def ldSP(gb,param):
    return "LD SP," + hex(param)

def ldC(gb,param):
    return "LD C," + hex(param)

def ldA(gb,param):
    return "LD A," + hex(param)

def ldL(gb,param):
    return "LD L," + hex(param)

def ldE(gb,param):
    return "LD E," + hex(param)

def jrNZ(gb,param):
    # param is relative, need to eventually account for this
    return "JR NZ " + hex(param)

def ldhC_A(gb,param):
    return "LD $FF" + padhexa(hex(param))[-2:] + ",A"

def ldP_A(gb,param):
    return "LD $FF" + padhexa(hex(param))[-2:] + ",C"

# CB operations
def cbOP(gb,param):
    return cbops[param]

def call(gb,param):
    return "CALL " + hex(param)

def callZ(gb,param):
    return "CALL Z," + hex(param)

def callC(gb,param):
    return "CALL C," + hex(param)

def jr(gb,param):
    return "JR, " + hex(param)

def jrZ(gb,param):
    return "JR Z," + hex(param)

def cp_P(gb,param):
    return "CP " + hex(param)

def rlca(gb):
    return "RLCA"

def rla(gb):
    return "RLA"

def ret(gb):
    return "RET"

def reti(gb):
    return "RETI"

opcode = {
    0: nop,
    1: ldBC,
    2: ldBC_A,
    3: incBC,
    4: incB,
    5: decB,
    6: ldB_P,
    7: rlca,
    8: ldP_SP,
    10: ldA_BC,
    11: decBC,
    12: incC,
    13: decC,
    14: ldC,
    16: stop,
    17: ldDE,
    18: ldDE_A,
    19: incDE,
    20: incD,
    21: decD,
    22: ldD_P,
    23: rla,
    24: jr,
    26: ldA_DE,
    28: incE,
    29: decE,
    30: ldE_P,
    32: jrNZ,
    33: ldHL,
    34: ldDE_A,
    35: incHL_8,
    36: decHL_8,
    37: decH,
    40: jrZ,
    44: incC,
    45: decC,
    46: ldL_P,
    49: ldSP,
    50: ldHLm_A,
    51: incSP,
    60: incA,
    61: decA,
    62: ldA,
    64: ldB_B,
    65: ldB_C,
    66: ldB_D,
    67: ldB_E,
    68: ldB_H,
    69: ldB_L,
    70: ldB_HL,
    71: ldB_A,
    72: ldC_B,
    73: ldC_C,
    74: ldC_D,
    75: ldC_E,
    76: ldC_H,
    77: ldC_L,
    78: ldC_HL,
    79: ldC_A,
    80: ldD_B,
    81: ldD_C,
    82: ldD_D,
    83: ldD_E,
    84: ldD_H,
    85: ldD_L,
    86: ldD_HL,
    87: ldD_A,
    88: ldE_B,
    89: ldE_C,
    90: ldE_D,
    91: ldE_E,
    92: ldE_H,
    93: ldE_L,
    94: ldE_HL,
    95: ldE_A,
    96: ldH_B,
    97: ldH_C,
    98: ldH_D,
    99: ldH_E,
    100: ldH_H,
    101: ldH_L,
    102: ldH_HL,
    103: ldH_A,
    104: ldL_B,
    105: ldL_C,
    106: ldL_D,
    107: ldL_E,
    108: ldL_H,
    109: ldL_L,
    110: ldL_HL,
    111: ldL_A,
    112: ldHL_B,
    113: ldHL_C,
    114: ldHL_D,
    115: ldHL_E,
    116: ldHL_H,
    117: ldHL_L,
    118: halt,
    119: ldHL_A,
    120: ldA_B,
    121: ldA_C,
    122: ldA_D,
    123: ldA_E,
    124: ldA_H,
    125: ldA_L,
    126: ldA_HL,
    127: ldA_A,
    128: addA_B,
    129: addA_C,
    130: addA_D,
    131: addA_E,
    132: addA_H,
    133: addA_L,
    134: addA_HL,
    135: addA_A,
    136: adcA_B,
    137: adcA_C,
    138: adcA_D,
    139: adcA_E,
    140: adcA_H,
    141: adcA_L,
    142: adcA_HL,
    143: adcA_A,
    144: subB,
    145: subC,
    146: subD,
    147: subE,
    148: subH,
    149: subL,
    150: subHL,
    151: subA,
    152: sbcA_B,
    153: sbcA_C,
    154: sbcA_D,
    155: sbcA_E,
    156: sbcA_H,
    157: sbcA_L,
    158: sbcA_HL,
    159: sbcA_A,
    160: andB,
    161: andC,
    162: andD,
    163: andE,
    164: andH,
    165: andL,
    166: andHL,
    167: andA,
    168: xorB,
    169: xorC,
    170: xorD,
    171: xorE,
    172: xorH,
    173: xorL,
    174: xorHL,
    175: xorA,
    176: orB,
    177: orC,
    178: orD,
    179: orE,
    180: orH,
    181: orL,
    182: orHL,
    183: orA,
    184: cpB,
    185: cpC,
    186: cpD,
    187: cpE,
    188: cpH,
    189: cpL,
    190: cpHL,
    191: cpA,
    193: popBC,
    197: pushBC,
    201: ret,
    203: cbOP,
    204: callZ,
    205: call,
    206: adcA_P,
    209: popDE,
    213: pushDE,
    217: reti,
    222: sbcA_P,
    224: ldhC_A,
    225: popHL,
    226: ldP_A,
    229: pushHL,
    234: ldP_A16,
    238: xorP,
    240: ldhA_P,
    241: popAF,
    242: ldA_P,
    245: pushAF,
    250: ldA_P16,
    254: cp_P
}