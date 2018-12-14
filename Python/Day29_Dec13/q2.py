#!/usr/bin/env python

"""
2. Show partywise seat share for following results of the Assembly Elections 2018
in a piechart.Party with highest percentage should be shown as detached (slightly).

Madhya Pradesh
	INC - Win (114)
        BJP - Win (15)
        Independent - Win (4)
        Others - Win (3)
Rajasthan
	INC - Win (99)
	BJP- Win (73)
	Independent- Win (3)
	Others- Win (14)
Chhattisgarh
	INC- Win (68)
	BJP- Win (15)
	BSP+- Win (9)
	Others- Win (7)
Telangana
	TRS- Win (88)
	INC- Win (19)
	BJP- Win (1)
	Others- Win (11)
Mizoram
	MNF- Win (26)
	INC- Win (5)
	BJP- Win (1)
	Others- Win (8)
"""



# importing packages
import matplotlib.pyplot as plt


fob = plt.figure(figsize = (12,12), facecolor='1')
colrs='r y c g'.split()
expl=[0.1,0,0,0]

# Sublpot for Madhya Pradesh
spmp = fob.add_subplot(3,2,1)
parties_in_mp = ["INC", "BJP", "INDEPENDENT","OTHERS"]
won_in_mp = [114,15,4,3]
spmp.pie(won_in_mp, explode=expl, colors=colrs, autopct='%1.1f%%', labels= parties_in_mp, startangle=90)
spmp.legend(loc="best")
spmp.set_title("Madhya Pradesh")

# Subplot for Rajasthan
spra = fob.add_subplot(322)
won_in_ra = [99,73,3,14]
spra.pie(won_in_ra, explode=expl, colors=colrs, autopct='%1.1f%%', labels=parties_in_mp, startangle=90)
spra.legend(loc="best")
spra.set_title("Rajasthan")

# Subplot for Chhattisgarh
spch = fob.add_subplot(3,2,3)
parties_in_ch = ["INC", "BJP", "BSP+-","OTHERS"]
won_in_ch = [68,15,9,7]
spch.pie(won_in_ch, explode=expl, colors=colrs, autopct='%1.1f%%', labels=parties_in_ch, startangle=90)
spch.legend(loc="best")
spch.set_title("Chhattisgarh")

# Subplot for Telangana
sptr = fob.add_subplot(3,2,4)
parties_in_tr = ["TRS", "INC", "BJP","OTHERS"]
won_in_tr = [88,19,1,1]
sptr.pie(won_in_tr, explode=expl, colors=colrs, autopct='%1.1f%%', labels=parties_in_tr, startangle=90)
sptr.legend(loc="best")
sptr.set_title("Telangana")

# Subplot for Mizoram
spmz = fob.add_subplot(3,2,5)
parties_in_mz = ["MNF", "INC", "BJP","OTHERS"]
won_in_mz = [26,5,1,8]
spmz.pie(won_in_mz, explode=expl, colors=colrs, autopct='%1.1f%%', labels=parties_in_mz, startangle=90)
spmz.legend(loc="best")
spmz.set_title("Mizoram")

fob.canvas.set_window_title("Assembly Elections 2018")
plt.show()







