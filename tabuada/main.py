#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.1"
__author__ = "Jonatas"

factors = list(range(1,11))
separator = (30*"#")
template = """
------Tabuada do número: {factor}------

{operations}

{separator}
"""

for factor1 in factors:
	operations = ""
	for newFactor in factors:
			line = ""
			result = factor1 * newFactor
			line += f"{factor1} x {newFactor} = {result}"
			operations += f"{line:^30}\n"
	print(
		template.format(
			factor=factor1,
			operations=operations,
			separator=separator
		)
	)
