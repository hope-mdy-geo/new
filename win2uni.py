# -*- coding: utf-8 -*-
import re

def replace(input):
	""" Replace each win char value with equivlant code point in Unicode.
	Conversions will be one on one. """
	output = input
	output = output.replace(u'\u0075', u'\u1000')
	return output


def convert(input):
	output = replace(input)
	return output
