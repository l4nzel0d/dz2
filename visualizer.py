import xml.etree.ElementTree as ET
import subprocess
import sys
import tempfile
import os

def read_config(config_path):
	"""Reads the config file and returns the path to the visualizer and the package name.""" 
	try:
		tree = ET.parse(config_path)
		root = tree.getroot()
		visualizer_path = root.find('visualizerPath').text
		package_name = root.find('packageName').text
		return visualizer_path, package_name
	except ET.ParseError:
		print("Error Parsing XML file")
		sys.exit(1)

def generate_dependencies_graph(package_name):
	"""Runs apk to generate the dependency graph of the package in dot format.""" 
	try:
		result = subprocess.run(["apk", "dot", package_name], capture_output=True, text=True, check=True)
		return result.stdout
	except subprocess.CalledProcessError:
		print("Error executing apk command.")
		sys.exit(1)

def visualize_graph(graph_data, visualizer_path, package_name):
	"""Generates an image of the dependency graph using the dot program and opens it with Ristretto.""" 
	with tempfile.NamedTemporaryFile(delete=False, suffix=".dot") as dot_file:
		dot_file.write(graph_data.encode('utf-8'))
		dot_path = dot_file.name
	
	output_path = f"{package_name}_dependencies.png"
	try:
		# Generate the graph image
		subprocess.run([visualizer_path, "-Tpng", dot_path, "-o", output_path], check=True)
		print(f"Dependency graph saved to {output_path}")
		
		# Open the generated image in Ristretto
		subprocess.Popen(["ristretto", output_path])
		
	finally:
		os.remove(dot_path)

def main(config_path):
	visualizer_path, package_name = read_config(config_path)
	graph_data = generate_dependencies_graph(package_name)
	visualize_graph(graph_data, visualizer_path, package_name)


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python visualizer.py <path to config file>")
		sys.exit(1)
	main(sys.argv[1])
