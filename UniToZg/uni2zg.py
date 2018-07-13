# -*- coding: utf-8 -*-
import re

def replace(input):
    output = input
    output = output.replace(u'\u103A', u'\u1039')  # AThet...
    output = output.replace(u'\u103B', u'\u103A')  # YaPint...
    output = output.replace(u'\u103C', u'\u103B')  # YaYit...
    output = output.replace(u'\u103D', u'\u103C')  # WaSwe...
    output = output.replace(u'\u103E', u'\u103D')  # HaHtoe...
    output = output.replace(u'\u103F', u'\u1086')  # ThaGyi...
    output = output.replace(u'\u1009\u1039', u'\u106A\u1039')  # NyaLay...
    output = output.replace(u'\u103C\u103D', u'\u103D\u103C')  # WaSwe...HaHtoe...
    output = output.replace(u'\u103D\u103C', u'\u108A')  # WaSwe....HaHtoe...

    # ------------------------------------------ Pint / Yit / Swe / Htoe --------------------------------
    return output


def decompose(input):
    output = input
    output = output.replace(u'\u1039\u1000', u'\u1060')  # Ka...
    output = output.replace(u'\u1039\u1001', u'\u1061')  # Kha...
    output = output.replace(u'\u1039\u1002', u'\u1062')  # Ga...
    output = output.replace(u'\u1039\u1003', u'\u1063')  # GaGyi...
    output = output.replace(u'\u1039\u1005', u'\u1065')  # Sa...
    output = output.replace(u'\u1039\u1006', u'\u1066')  # SaLai...
    output = output.replace(u'\u1039\u1006', u'\u1067')  # SaLai...
    output = output.replace(u'\u1039\u1007', u'\u1068')  # Za...
    output = output.replace(u'\u1039\u1008', u'\u1069')  # ZaMyinZwe...
    output = output.replace(u'\u1039\u100B', u'\u106C')  # TaTaLin...
    output = output.replace(u'\u1039\u100C', u'\u106D')  # HtaWan...
    output = output.replace(u'\u1039\u100F', u'\u1070')  # NaGyi...
    output = output.replace(u'\u1039\u1010', u'\u1071')  # Ta....
    output = output.replace(u'\u1039\u1010', u'\u1072')  # Ta...
    output = output.replace(u'\u1039\u1011', u'\u1073')  # Hta...
    output = output.replace(u'\u1039\u1011', u'\u1074')  # Hta...
    output = output.replace(u'\u1039\u1012', u'\u1075')  # Da...
    output = output.replace(u'\u1039\u1013', u'\u1076')  # DaOut...
    output = output.replace(u'\u1039\u1014', u'\u1077')  # NaNge...
    output = output.replace(u'\u1039\u1015', u'\u1078')  # Pa...
    output = output.replace(u'\u1039\u1016', u'\u1079')  # Pha...
    output = output.replace(u'\u1039\u1017', u'\u107A')  # BaHtet...
    output = output.replace(u'\u1039\u1018', u'\u107B')  # Ba...
    output = output.replace(u'\u1039\u1019', u'\u107C')  # Ma...
    output = output.replace(u'\u1039\u101C', u'\u1085')  # La...
    output = output.replace(u'\u1039\u1018', u'\u1093')  # Ba...
    output = output.replace(u'\u100F\u103A\u100D', u'\u1091')  # ႑....

    # ------------------------------------------ A Sint ------------------------------------------------

    output = output.replace(u'\u1004\u1039\u1062', u'\u1002\u1064')  # Ka....
    output = output.replace(u'\u1004\u1039\u1060', u'\u1000\u1064')  # Kha...
    output = output.replace(u'\u1004\u1039\u1061', u'\u1001\u1064')  # Ga....
    output = output.replace(u'\u1004\u1039\u1063', u'\u1003\u1064')  # NgaGyi...NgaThet...
    output = output.replace(u'\u1064\u102D', u'\u108B')  # NgaThet...LoneGyiTin...
    output = output.replace(u'\u1064\u102E', u'\u108C')  # NgaThet...SanKhat...
    output = output.replace(u'\u1064\u1036', u'\u108D')  # NgaThet...ThayTin...
    output = output.replace(u'\u102D\u1036', u'\u108E')  # LoneGyiTin...ThayTin...

    # ------------------------------------------------------------------- Nga Thet -------------------------------------

    return output


def logical2visual(input):
    output = input
    output = re.sub(u'\u103B\u102F', u'\u103B\u1033', output)  # YAYit...TaCg...
    output = re.sub(u'\u103B\u1030', u'\u103B\u1034', output)  # YAYit...Nacg...
    output = re.sub(u'\u103B\u102D\u102F', u'\u103B\u102D\u1033', output)  # YAYit...LoneGyi...TaCg...
    output = re.sub(u'\u103A\u102F', u'\u103A\u1033', output)  # YaPint...TaCg...
    output = re.sub(u'\u103A\u1030', u'\u103A\u1034', output)  # YaPint...NaCg...
    output = re.sub(u'\u103A\u103C', u'\u107D\u103C', output)  # YaPint...WaSwe...
    output = output.replace(u'\u103D\u103A', u'\u103A\u103D')  # YaPint...HaHtoe...
    output = re.sub(u'\u103A\u102D\u102F', u'\u103A\u102D\u1033', output)  # YaPint...LoneGyi...TaCg...

    output = re.sub(u'([\u1000-\u1021])([\u103A])(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Byee...YaPint...

    output = re.sub(u'([\u1000-\u1021])(\u103B)', u"\\2\\1", output)  # YaYit...Byee...
    output = re.sub(u'([\u1000-\u1021])(\u1031)', u"\\2\\1", output)  # ThaWayHtoe...Byee...
    output = re.sub(u'([\u103B])(\u1031)', u"\\2\\1", output)  # ThaWayHtoe...YaYit...
    output = re.sub(u'([\u1000-\u1021])([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Byee...Swe/Htoe...
    output = re.sub(u'(\u108F)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Na...Swe/Htoe...
    output = re.sub(u'(\u1090)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Ya...Swe/Htoe...
    output = re.sub(u'(\u108F)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Na...Swe/Htoe...
    output = re.sub(u'(\u1090)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Ya...Swe/Htoe...
    output = re.sub(u'([\u1000-\u1021])([\u108A])(\u1031)', u"\\3\\1\\2", output)  # ThaWayHtoe...Byee...Swe/Htoe...
    output = re.sub(u'([\u1000-\u1021])(\u103A)(\u103D)(\u1031)', u"\\4\\1\\2\\3", output)  # ThaWayHtoe...Byee...Pint/Htoe...

    # -------------------------------------------------------------------- Tha Way Htoe ------------------------------------------------------------------------

    output = re.sub(u'\u1030\u1037', u'\u1030\u1094', output)  # NaCg...OutMyit...
    output = re.sub(u'\u103C\u1037', u'\u103C\u1094', output)  # YaYit...OutMyit...
    output = re.sub(u'\u108A\u1037', u'\u108A\u1095', output)  # Swe/Htoe...OutMyit...
    output = re.sub(u'\u102D\u102F\u1037', u'\u102D\u102F\u1094', output)  # LoneGyi...TaCg...OutMyit...
    output = re.sub(u'\u103C\u1032\u1037', u'\u103C\u1032\u1094', output)  # NouthMyit...Swe...OutMyit...
    output = re.sub(u'\u103C\u1036\u1037', u'\u103C\u1036\u1095', output)  # ThayTin...Swe...OutMyit...
    output = re.sub(u'\u1036\u1088\u1037', u'\u1036\u1088\u1095', output)  # HaHtoe...TaCg...OutMyit...
    output = output.replace(u'\u1014\u1037', u'\u1014\u1094')  # Na...OutMyit...

    # ------------------------------------------------------------------- Out Ka Myit ------------------------------------------------------------------------

    return output



def shape(input):
    output = input

    output = output.replace(u'\u1014\u103D', u'\u108F\u103D')  # NgaNge...HaHtoe...
    output = output.replace(u'\u1014\u103C', u'\u108F\u103C')  # NgaNge...WaSwe...
    output = output.replace(u'\u1014\u102F', u'\u108F\u102F')  # NgaNge...TaCg...
    output = output.replace(u'\u1014\u1075', u'\u108F\u1075')  # NgaNge...Da...
    output = output.replace(u'\u1014\u1076', u'\u108F\u1076')  # NgaNge...DaOut...
    output = output.replace(u'\u1014\u1077', u'\u108F\u1077')  # NgaNge...NgaNge...
    output = output.replace(u'\u1014\u102D\u102F', u'\u108F\u102D\u102F')  # NgaNge...TaCg...LoneGyi...

    # ---------------------------------------------------------------- Nga Nge -------------------------------------------------------------

    output = output.replace(u'\u101B\u103D', u'\u1090\u103D')  # Ya...HaHtoe...
    output = output.replace(u'\u101B\u103C', u'\u1090\u103C')  # Ya...WaSwe...
    output = output.replace(u'\u101B\u102F', u'\u1090\u102F')  # Ya...TaCg...
    output = output.replace(u'\u101B\u102D\u102F', u'\u1090\u102D\u102F')  # Ya...TaCg...LoneGyi...
    output = output.replace(u'\u101B\u108A', u'\u1090\u108A')  # Ya...WaSwe...HaHtoe...

    # ------------------------------------------------------------------ Ya ------------------------------------------------------------


    output = output.replace(u'\u102B\u1039', u'\u105A')  # YaCha...ShaeHtoe...
    output = output.replace(u'\u103D\u102F', u'\u1088')  # HaHtoe...TaCg...
    output = output.replace(u'\u103D\u1030', u'\u1089')  # HaHtoe...NaCg...
    output = output.replace(u'\u1062\u102D\u102F', u'\u1062\u102D\u1033')  # Ga...LoneGyi...TaCg...
    output = output.replace(u'\u1062\u102F', u'\u1062\u1033')  # Ga...TaCg...

    # --------------------------------------------------------------------- Ta Chaung Ngin ----------------------------------------------------------------------

    output = re.sub(u'\u103B\u1000', u'\u107E\u1000', output)  # Ka...
    output = re.sub(u'\u103B\u1006', u'\u107E\u1006', output)  # SaLai...
    output = re.sub(u'\u103B\u1010', u'\u107E\u1010', output)  # Ta...

    # -------------------------------------------------------------------- Ya Yit Gyi -----------------------------------------------------------------------------------

    output = re.sub(u'\u107E\u1000\u103C\u102D', u'\u1084\u1000\u103C\u102D', output)  # YY...Ka...Swe...LGT...
    output = re.sub(u'\u107E\u1006\u103C\u102D', u'\u1084\u1006\u103C\u102D', output)  # YY...SaLai...Swe...LGT...
    output = re.sub(u'\u107E\u1010\u103C\u102D', u'\u1084\u1010\u103C\u102D', output)  # YY...Ta...Swe...LGT...
    output = re.sub(u'\u107E\u1000\u103C\u102E', u'\u1084\u1000\u103C\u102E', output)  # YY...Ka...Swe...LGTSan...
    output = re.sub(u'\u107E\u1006\u103C\u102E', u'\u1084\u1006\u103C\u102E', output)  # YY...SaLai...Swe...LGTSan...
    output = re.sub(u'\u107E\u1010\u103C\u102E', u'\u1084\u1010\u103C\u102E', output)  # YY...Ta...Swe...LGTSan...

    # ----------------------------------------------------------------- Lone Gyi Tin / Ya Yit Gyi / Wa Swe -------------------------------------------------------------

    output = re.sub(u'\u107E\u1000\u102D', u'\u1080\u1000\u102D', output)  # YY...Ka...Swe...LGT...
    output = re.sub(u'\u107E\u1006\u102D', u'\u1080\u1006\u102D', output)  # YY...SaLai...Swe...LGT...
    output = re.sub(u'\u107E\u1010\u102D', u'\u1080\u1010\u102D', output)  # YY...Ta...Swe...LGT...
    output = re.sub(u'\u107E\u1000\u102E', u'\u1080\u1000\u102E', output)  # YY...Ka...Swe...LGTSan...
    output = re.sub(u'\u107E\u1006\u102E', u'\u1080\u1006\u102E', output)  # YY...SaLai...Swe...LGTSan...
    output = re.sub(u'\u107E\u1010\u102E', u'\u1080\u1010\u102E', output)  # YY...Ta...Swe...LGTSan...

    # -------------------------------------------------------------------- Lone Gyi Tin / Ya Yit Gyi ------------------------------------------------------------------------

    output = re.sub(u'\u107E\u1000\u103C', u'\u1082\u1000\u103C', output)  # YY...Ka...Swe...
    output = re.sub(u'\u107E\u1006\u103C', u'\u1082\u1006\u103C', output)  # YY...SaLai...Swe...
    output = re.sub(u'\u107E\u1010\u103C', u'\u1082\u1010\u103C', output)  # YY...Ta...Swe...

    # ------------------------------------------------------------------------- Wa Swe / Ya Yit Gyi -------------------------------------------

    output = re.sub(u'\u103B\u1001\u103C\u102D', u'\u1083\u1001\u103C\u102D', output)  # YYL...Ka...Swe...LGT...
    output = re.sub(u'\u103B\u1002\u103C\u102D', u'\u1083\u1002\u103C\u102D', output)  # YYL...Ga...Swe...LGT...
    output = re.sub(u'\u103B\u1004\u103C\u102D', u'\u1083\u1004\u103C\u102D', output)  # YYL...Nga...Swe...LGT...
    output = re.sub(u'\u103B\u1012\u103C\u102D', u'\u1083\u1012\u103C\u102D', output)  # YYL...Da...Swe...LGT...
    output = re.sub(u'\u103B\u1015\u103C\u102D', u'\u1083\u1015\u103C\u102D', output)  # YYL...Pa...Swe...LGT...
    output = re.sub(u'\u103B\u1016\u103C\u102D', u'\u1083\u1016\u103C\u102D', output)  # YYL...Pha...Swe...LGT...
    output = re.sub(u'\u103B\u1017\u103C\u102D', u'\u1083\u1017\u103C\u102D', output)  # YYL...BaHtat...Swe...LGT...
    output = re.sub(u'\u103B\u1019\u103C\u102E', u'\u1083\u1019\u103C\u102D', output)  # YYL...Ma...Swe...LGT...
    output = re.sub(u'\u103B\u1001\u103C\u102E', u'\u1083\u1001\u103C\u102E', output)  # YYL...Ka...Swe...LGTSan...
    output = re.sub(u'\u103B\u1002\u103C\u102E', u'\u1083\u1002\u103C\u102E', output)  # YYL...Ga...Swe...LGTSan...
    output = re.sub(u'\u103B\u1004\u103C\u102E', u'\u1083\u1004\u103C\u102E', output)  # YYL...Nga...Swe...LGTSan...
    output = re.sub(u'\u103B\u1012\u103C\u102E', u'\u1083\u1012\u103C\u102E', output)  # YYL...Da...Swe...LGTSan...
    output = re.sub(u'\u103B\u1015\u103C\u102E', u'\u1083\u1015\u103C\u102E', output)  # YYL...Pa...Swe...LGTSan...
    output = re.sub(u'\u103B\u1016\u103C\u102E', u'\u1083\u1016\u103C\u102E', output)  # YYL...Pha...Swe...LGTSan...
    output = re.sub(u'\u103B\u1017\u103C\u102E', u'\u1083\u1017\u103C\u102E', output)  # YYL...BaHtat...Swe...LGTSan...
    output = re.sub(u'\u103B\u1019\u103C\u102E', u'\u1083\u1019\u103C\u102E', output)  # YYL...Ma...Swe...LGTSan...

    # ---------------------------------------------------------------- Lone Gyi Tin / Ya Yit Lay / Wa Swe ----------------------------------------------------------------

    output = re.sub(u'\u103B\u1001\u102D', u'\u107F\u1001\u102D', output)  # YYL...Ka...LGT...
    output = re.sub(u'\u103B\u1002\u102D', u'\u107F\u1002\u102D', output)  # YYL...Ga...LGT...
    output = re.sub(u'\u103B\u1004\u102D', u'\u107F\u1004\u102D', output)  # YYL...Nga...LGT...
    output = re.sub(u'\u103B\u1012\u102D', u'\u107F\u1012\u102D', output)  # YYL...Da...LGT...
    output = re.sub(u'\u103B\u1015\u102D', u'\u107F\u1015\u102D', output)  # YYL...Pa...LGT...
    output = re.sub(u'\u103B\u1016\u102D', u'\u107F\u1016\u102D', output)  # YYL...Pha...LGT...
    output = re.sub(u'\u103B\u1017\u102D', u'\u107F\u1017\u102D', output)  # YYL...BaHtat...LGT...
    output = re.sub(u'\u103B\u1019\u102E', u'\u107F\u1019\u102D', output)  # YYL...Ma...LGT...
    output = re.sub(u'\u103B\u1001\u102E', u'\u107F\u1001\u102E', output)  # YYL...Ka...LGTSan...
    output = re.sub(u'\u103B\u1002\u102E', u'\u107F\u1002\u102E', output)  # YYL...Ga...LGTSan...
    output = re.sub(u'\u103B\u1004\u102E', u'\u107F\u1004\u102E', output)  # YYL...Nga...LGTSan...
    output = re.sub(u'\u103B\u1012\u102E', u'\u107F\u1012\u102E', output)  # YYL...Da...LGTSan...
    output = re.sub(u'\u103B\u1015\u102E', u'\u107F\u1015\u102E', output)  # YYL...Pa...LGTSan...
    output = re.sub(u'\u103B\u1016\u102E', u'\u107F\u1016\u102E', output)  # YYL...Pha...LGTSan...
    output = re.sub(u'\u103B\u1017\u102E', u'\u107F\u1017\u102E', output)  # YYL...BaHtat...LGTSan...
    output = re.sub(u'\u103B\u1019\u102E', u'\u107F\u1019\u102E', output)  # YYL...Ma...LGTSan...

    # --------------------------------------------------------------- Lone Gyi Tin / Ya Yit Lay ------------------------------------------------------------------

    output = re.sub(u'\u103B\u1001\u103C', u'\u1081\u1001\u103C', output)  # YYL...Ka...Swe...
    output = re.sub(u'\u103B\u1002\u103C', u'\u1081\u1002\u103C', output)  # YYL...Ga...Swe...
    output = re.sub(u'\u103B\u1004\u103C', u'\u1081\u1004\u103C', output)  # YYL...Nga...Swe...
    output = re.sub(u'\u103B\u1012\u103C', u'\u1081\u1012\u103C', output)  # YYL...Da...Swe...
    output = re.sub(u'\u103B\u1015\u103C', u'\u1081\u1015\u103C', output)  # YYL...Pa...Swe...
    output = re.sub(u'\u103B\u1016\u103C', u'\u1081\u1016\u103C', output)  # YYL...Pha...Swe...
    output = re.sub(u'\u103B\u1017\u103C', u'\u1081\u1017\u103C', output)  # YYL...BaHtat...Swe...
    output = re.sub(u'\u103B\u1019\u103C', u'\u1081\u1019\u103C', output)  # YYL...Ma...Swe...

    # ---------------------------------------------------------------- Ya Yit Lay / Wa Swe -------------------------------------------------------------------------------

    return output



def convert(input):

    output = input
    output = decompose(output)
    output = replace(output)
    output = logical2visual(output)
    output = shape(output)
    return output
