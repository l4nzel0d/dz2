# Dependency Graph Visualizer

This repository contains a Python application for visualizing dependency graphs of packages using Graphviz. The tool is designed to work with Alpine Linux packages, extracting dependencies and generating visual representations in PNG format.

## Features

- Read configuration from an XML file to specify the visualizer path and package name.
- Generate dependency graphs using the `dot` program.
- Open generated graphs using Ristretto.
- Comprehensive unit tests to ensure the functionality of the application.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `unittest` (for testing)
  - `subprocess`
  - `tempfile`
  - `os`
- Alpine Linux environment for testing with Alpine packages.
- Graphviz installed on your system (`dot` command).
- Ristretto installed for viewing the generated images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dependency-graph-visualizer.git
   cd dependency-graph-visualizer
   ```

2. Ensure you have the necessary dependencies installed in your Alpine Linux environment. You can install Graphviz and Ristretto using:
   ```bash
   apk add graphviz ristretto
   ```

3. Create a configuration file named `config.xml` in the project root with the following structure:
   ```xml
   <config>
       <visualizerPath>/usr/bin/dot</visualizerPath>
       <packageName>openssl</packageName>
   </config>
   ```

## Usage

To visualize the dependency graph of a specified package:

1. Run the visualizer script:
   ```bash
   python visualizer.py
   ```

2. The generated dependency graph will be saved as `<packageName>_dependencies.png` in the project directory.

3. The generated image will automatically open in Ristretto.
![Alt text](/screenshots/pic4.png)


## Testing

This project includes unit tests to ensure functionality. To run the tests:

1. Ensure that you are in the project directory.
2. Execute the following command:
   ```bash
   python -m unittest test_visualizer.py
   ```

## Author

Created by **l4nzel0d** aka **Boris Vasilyev**
