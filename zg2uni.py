# -*- coding: utf-8 -*-
import re


def convert(input):

	output = input

	output = re.sub(u'[\u103D\u1087]', u'\u103E', output)  # HaHtoe...
	output = re.sub(u'\u103C', u'\u103D', output)  # WaSwe...
	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]', u'\u103C', output)  # YaYit....
	output = re.sub(u'[\u103A\u107D]', u'\u103B', output)  # YaPint....

# -----------------------------------------------------------------Pint / Yit / Swe / Htoe--------------------------------------------------------------------------

	output = re.sub(u'(\u1031)([\u1000-\u1021])', u"\\2\\1", output)  # Byee...TheWayHtoe
	output = re.sub(u'(\u1031)([\u103B\u103D\u103E])', u"\\2\\1", output) # Byee...TheWayHtoe
	output = re.sub(u'(\u103C)([\u1000-\u1021])', u"\\2\\1", output)  # YaPSH....Byee
	output = re.sub(u'(\u1031)([\u1000-\u1021])(\u103C)', u"\\2\\3\\1", output) # Byee...PYSH...TWH
	#output = re.sub(u'(\u1031)([\u1000-\u1021])(\u103E)', u"\\2\\3\\1", output)  # TheWayHtoe....Byee...HaHtoe

# ------------------------------------------------------------------Ta Ya----------------------------------------------------------------------------------

	output = output.replace(u'\u1039', u'\u103A') # AThet...
	output = output.replace(u'\u108F', u'\u1014') # NaNge....
	output = output.replace(u'\u106A', u'\u1009') # NyaLay...
	output = output.replace(u'\u106B', u'\u100A') # NyaGyi...
	output = output.replace(u'\u1086', u'\u103F') # ThaGyi....
	output = output.replace(u'\u1033', u'\u102F') # TaCgNgin....
	output = output.replace(u'\u1034', u'\u1030') # NhaCgNgin....
	output = re.sub(u'[\u1094\u1095]', u'\u1037', output) # AutMyint....

	#--------------------------------------------------------------------Direct Change-----------------------------------------------------------------------------

	output = re.sub(u'\u1060', u'\u1039\u1000', output) # Ka
	output = re.sub(u'\u1061', u'\u1039\u1001', output) # Kha
	output = re.sub(u'\u1062', u'\u1039\u1002', output) # Gha
	output = re.sub(u'\u1063', u'\u1039\u1003', output) # GhaGyi
	output = re.sub(u'\u1065', u'\u1039\u1005', output) # SaLone
	output = re.sub(u'([\u1066-\u1067])', u'\u1039\u1006', output) # SaLai
	output = re.sub(u'\u1068', u'\u1039\u1007', output) # ZaGwe
	output = re.sub(u'\u1069', u'\u1039\u1008', output)  # ZaMyinZwe
	output = re.sub(u'\u106C', u'\u1039\u100B', output)  # TaTaLinJate
	output = re.sub(u'\u106D', u'\u1039\u100C', output)  # HtaWanBae
	output = re.sub(u'\u1070', u'\u1039\u100F', output)  # NaGyi
	output = re.sub(u'([\u1071-\u1072])', u'\u1039\u1010', output)  # TaWanPu
	output = re.sub(u'([\u1073-\u1074])', u'\u1039\u1011', output)  # HtaSinHtoo
	output = re.sub(u'\u1075', u'\u1039\u1012', output)  # DaDwae
        output = re.sub(u'\u1076', u'\u1039\u1013', output)  # DaOut
	output = re.sub(u'\u1077', u'\u1039\u1014', output)  # Na
	output = re.sub(u'\u1078', u'\u1039\u1015', output)  # Pa
	output = re.sub(u'\u1079', u'\u1039\u1016', output)  # Pha
	output = re.sub(u'\u107A', u'\u1039\u1017', output)  # BaHtaChite
	output = re.sub(u'\u107B', u'\u1039\u1018', output)  # BaGone
	output = re.sub(u'\u107C', u'\u1039\u1019', output)  # Ma
	output = re.sub(u'\u1085', u'\u1039\u101C', output)  # La
	output = re.sub(u'\u1093', u'\u1039\u1018', output)  # Ba
	output = re.sub(u'\u1096', u'\u1039\u1010\u103D', output)  # Twa
	output = re.sub(u'\u106E', u'\u1039\u100B', output)  # ဋ.....
	output = re.sub(u'\u106F', u'\u1039\u100D', output)  # ဍ....

#------------------------------------------------------------------A Sint---------------------------------------------------------------------------------

	output = re.sub(u'\u105A', u'\u102B' + '\u103A', output)  # YaChaShaeHtoe.......
	output = re.sub(u'\u1088', u'\u103E' + '\u102F', output)  # Ha1Cg.....
	output = re.sub(u'\u1089', u'\u103E' + '\u1030', output)  # Ha2Cg.......
	output = re.sub(u'\u108A', u'\u103C' + '\u103D', output)  # WaHaHtoe......
	output = re.sub(u'\u106F', u'\u100D\u100E', output)  # ...ၯ...
	output = re.sub(u'\u104E', u'\u104E' + '\u1004' + '\u103A' + '\u1038', output)  # ...၎...
	output = re.sub(u'\u1091', u'\u100F' + '\u1039' + '\u100D', output)  # ...႑...
	output = re.sub(u'\u1026', u'\u1025' + '\u102E', output)  # ...ဦ...
	output = re.sub(u'\u104E', u'\u104E' + '\u1004' + '\u103A' + '\u1038', output)
	output = re.sub(u'\u108B', u'\u1064' + '\u102D', output)
	output = re.sub(u'\u108C', u'\u1064' + '\u102E', output)
	output = re.sub(u'\u108D', u'\u1064' + '\u1036', output)
	output = re.sub(u'\u108E', u'\u102D' + '\u1036', output)


	output = re.sub(u'([\u1000-\u1021])([\u1000-\u1021])(\u1064)', u"\\1\\3\\2", output)
	output = re.sub(u'(\u1064)', u'\u1004' + '\u103A', output)



#-------------------------------------------------------------------+++++----------------------------------------------------------------------------------

	return output
