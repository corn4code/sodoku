# 9x9 grid
# s11 -> s12 ... s21 -> s22 ... to s99 --> 81 squars writenn s{number of line}{character in line}

s11 = s12 = s13 = s14 = s15 = s16 = s17 = s18 = s19 = 0
s21 = s22 = s23 = s24 = s25 = s26 = s27 = s28 = s29 = 0
s31 = s32 = s33 = s34 = s35 = s36 = s37 = s38 = s39 = 0
s41 = s42 = s43 = s44 = s45 = s46 = s47 = s48 = s49 = 0
s51 = s52 = s53 = s54 = s55 = s56 = s57 = s58 = s59 = 0
s61 = s62 = s63 = s64 = s65 = s66 = s67 = s68 = s69 = 0
s71 = s72 = s73 = s74 = s75 = s76 = s77 = s78 = s79 = 0
s81 = s82 = s83 = s84 = s85 = s86 = s87 = s88 = s89 = 0
s91 = s92 = s93 = s94 = s95 = s96 = s97 = s98 = s99 = 0

line_one = [s11, s12, s13, s14, s15, s16, s17, s18, s19]
line_two = [s21, s22, s23, s24, s25, s26, s27, s28, s29]
line_three = [s31, s32, s33, s34, s35, s36, s37, s38, s39]
line_four = [s41, s42, s43, s44, s45, s46, s47, s48, s49]
line_five = [s51, s52, s53, s54, s55, s56, s57, s58, s59]
line_six = [s61, s62, s63, s64, s65, s66, s67, s68, s69]
line_seven = [s71, s72, s73, s74, s75, s76, s77, s78, s79]
line_eight = [s81, s82, s83, s84, s85, s86, s87, s88, s89]
line_nine = [s91, s92, s93, s94, s95, s96, s97, s98, s99]

# square count left -> right => [1][2][3]
#                               [4][5][6]
#                               [7][8][9]
square_one = [s11, s12, s13, s21, s22, s23, s31, s32, s33]
square_two = [s14, s15, s16, s24, s25, s26, s34, s35, s36]
square_three = [s17, s18, s19, s27, s28, s29, s37, s38, s39]
square_four = [s41, s42, s43, s51, s52, s53, s61, s62, s63]
square_five = [s44, s45, s46, s54, s55, s56, s64, s65, s66]
square_six = [s47, s48, s49, s57, s58, s59, s67, s68, s69]
square_seven = [s71, s72, s73, s81, s82, s83, s91, s92, s93]
square_eight = [s74, s75, s76, s84, s85, s86, s94, s95, s96]
square_nine = [s77, s78, s79, s87, s88, s89, s97, s98, s99]


def set_value():
    value = int(input(f"block value: "))
    return value
    

s31 = set_value()
print(s31)