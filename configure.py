# configure.py

def loadConfig():
    
    #get config
    conffile = open("drydock.cfg","r")
    conflist = conffile.readlines()
    conffile.close()
    return conflist
    
def configMatrix(conflist):
    
    #config lists
    F1conf = [conflist[1][1:-1],conflist[2][0:-1],conflist[3][0:-1],conflist[4][0:-1],conflist[5][0:-1],conflist[6][0:-1],conflist[7][0:-1],conflist[8][0:-1],conflist[9][0:-1],conflist[10][0:-1],conflist[11][0:-1]]
    F2conf = [conflist[12][1:-1],conflist[13][0:-1],conflist[14][0:-1],conflist[15][0:-1],conflist[16][0:-1],conflist[17][0:-1],conflist[18][0:-1],conflist[19][0:-1],conflist[20][0:-1],conflist[21][0:-1],conflist[22][0:-1]]
    F3conf = [conflist[23][1:-1],conflist[24][0:-1],conflist[25][0:-1],conflist[26][0:-1],conflist[27][0:-1],conflist[28][0:-1],conflist[29][0:-1],conflist[30][0:-1],conflist[31][0:-1],conflist[32][0:-1],conflist[33][0:-1]]
    F4conf = [conflist[34][1:-1],conflist[35][0:-1],conflist[36][0:-1],conflist[37][0:-1],conflist[38][0:-1],conflist[39][0:-1],conflist[40][0:-1],conflist[41][0:-1],conflist[42][0:-1],conflist[43][0:-1],conflist[44][0:-1]]
    F5conf = [conflist[45][1:-1],conflist[46][0:-1],conflist[47][0:-1],conflist[48][0:-1],conflist[49][0:-1],conflist[50][0:-1],conflist[51][0:-1],conflist[52][0:-1],conflist[53][0:-1],conflist[54][0:-1],conflist[55][0:-1]]
    F6conf = [conflist[56][1:-1],conflist[57][0:-1],conflist[58][0:-1],conflist[59][0:-1],conflist[60][0:-1],conflist[61][0:-1],conflist[62][0:-1],conflist[63][0:-1],conflist[64][0:-1],conflist[65][0:-1],conflist[66][0:-1]]
    F7conf = [conflist[67][1:-1],conflist[68][0:-1],conflist[69][0:-1],conflist[70][0:-1],conflist[71][0:-1],conflist[72][0:-1],conflist[73][0:-1],conflist[74][0:-1],conflist[75][0:-1],conflist[76][0:-1],conflist[77][0:-1]]
    F8conf = [conflist[78][1:-1],conflist[79][0:-1],conflist[80][0:-1],conflist[81][0:-1],conflist[82][0:-1],conflist[83][0:-1],conflist[84][0:-1],conflist[85][0:-1],conflist[86][0:-1],conflist[87][0:-1],conflist[88][0:-1]]
    F9conf = [conflist[89][1:-1],conflist[90][0:-1],conflist[91][0:-1],conflist[92][0:-1],conflist[93][0:-1],conflist[94][0:-1],conflist[95][0:-1],conflist[96][0:-1],conflist[97][0:-1],conflist[98][0:-1],conflist[99][0:-1]]
    F10conf = [conflist[100][1:-1]]
    F11conf = [conflist[101][1:-1]]
    F12conf = [conflist[102][1:-1]]
    Term = [conflist[103][0:-1]]
    Terminal = Term[0]
    
    #config matrix
    Fconf = [0,F1conf,F2conf,F3conf,F4conf,F5conf,F6conf,F7conf,F8conf,F9conf,F10conf,F11conf,F12conf,Terminal]
    
    return Fconf
    
def doneMatrix():
    # F Done
    F1_Done  = [False, False, False, False, False, False]
    F2_Done  = [False, False, False, False, False, False]
    F3_Done  = [False, False, False, False, False, False]
    F4_Done  = [False, False, False, False, False, False]
    F5_Done  = [False, False, False, False, False, False]
    F6_Done  = [False, False, False, False, False, False]
    F7_Done  = [False, False, False, False, False, False]
    F8_Done  = [False, False, False, False, False, False]
    F9_Done  = [False, False, False, False, False, False]
    F10_Done = [False, False, False, False, False, False]
    F11_Done = [False, False, False, False, False, False]
    F12_Done = [False, False, False, False, False, False]
    
    F_Done = [False, F1_Done, F2_Done, F3_Done, F4_Done, F5_Done, F6_Done, F7_Done, F8_Done, F9_Done, F10_Done, F11_Done, F12_Done]
    return F_Done
