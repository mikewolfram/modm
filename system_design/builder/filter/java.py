#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2009, Roboterclub Aachen e.V.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of the Roboterclub Aachen e.V. nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY ROBOTERCLUB AACHEN E.V. ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL ROBOTERCLUB AACHEN E.V. BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# $Id$
# -----------------------------------------------------------------------------

class Primitive:
	def __init__(self, javaType, name, size, equivalent, accessor):
		self.javaType = javaType
		self.name = name
		self.size = size
		self.equivalent = equivalent
		self.accessor = accessor
	
	def __cmp__(self, other):
		if isinstance(other, str):
			return cmp(self.name, other)
		else:
			return cmp(self.name, other.name)

PRIMITIVES = {
	"int8_t":	Primitive("int",	"Int8",		1,	"byte",		""),
	"int16_t":	Primitive("int",	"Int16",	2,	"short",	"Short"),
	"int32_t":	Primitive("int",	"Int32",	4,	"int",		"Int"),
	"uint8_t":	Primitive("int",	"Uint8",	1,	"byte",		""),
	"uint16_t":	Primitive("int",	"Uint16",	2,	"short",	"Short"),
	"uint32_t":	Primitive("int",	"Uint32",	4,	"int",		"Int"),
	"float": 	Primitive("float",	"Float",	4,	"float",	"Float"),
	"char":		Primitive("char",	"Char",		1,	"byte",		""),
	"Bool":		Primitive("boolean","Bool", 	1,	"boolean",	""),
}

# -----------------------------------------------------------------------------
def typeName(name):
	if name in PRIMITIVES:
		return PRIMITIVES[name].javaType
	else:
		return name.title().replace(' ', '')

def variableName(name):
	name = name.title().replace(' ', '')
	name = name[0].lower() + name[1:]
	return name

def enumElement(name):
	return name.upper().replace(' ', '_')
