import unittest 
from unittest.mock import patch, mock_open 
import tempfile
import os
import visualizer 

class TestVisualizer(unittest.TestCase): 
	@patch('builtins.open', new_callable=mock_open, read_data='<config><visualizerPath>/usr/bin/dot</visualizerPath><packageName>openssl</packageName></config>') 
	def test_read_config(self, mock_file): 
		visualizer_path, package_name = visualizer.read_config("fake_path.xml") 
		self.assertEqual(visualizer_path, "/usr/bin/dot") 
		self.assertEqual(package_name, "openssl") 

	@patch('subprocess.run') 
	def test_generate_dependencies_graph(self, mock_subproc_run): 
		mock_subproc_run.return_value.stdout = "digraph { openssl -> libssl; }" 
		graph_data = visualizer.generate_dependencies_graph("openssl") 
		self.assertIn("openssl -> libssl", graph_data) 


if __name__ == "__main__": 
	unittest.main()
