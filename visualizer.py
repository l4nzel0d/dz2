import xml.etree.ElementTree as ET
import subprocess
import sys
import tempfile
import os

def read_config(config_path):
	try:
		tree = ET.parse(config_path)
		root = tree.getroot()
		visualizer_path = root.find('visualizerPath').text
		package_name = root.find('packageName').text
		return visualizer_path, package_name
	except ET.ParseError:
		print("Error Parsing XML file")
		sys.exit(1)

def main(config_path):
	visualizer_path, package_name = read_config(config_path)
	print(visualizer_path, package_name)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("---")
		sys.exit(1)
	main(sys.argv[1])
