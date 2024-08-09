# ASL_pymol
This repo is for organizing and annotating hemagglutinin structures in pymol. 

README / Summary:
=================

This script is designed to automate the process of loading molecular structures into PyMOL, selecting and visualizing antigenic sites, clade and subclade-defining mutations, and generating high-quality images of these structures. It includes functions for setting up the base structure, highlighting specific sites and mutations, and exporting images. 

To use this script:
1. Ensure PyMOL is installed and running.
2. Place this script in your working directory.
3. Customize the parameters as needed within the `process_sequence` function calls in the `if __name__ == "__main__":` block.
4. Run the script directly using PyMOL's Python environment (e.g., `run pymol_script.py`).
5. The script will output images to the specified directory, organized by protein and sequence name.

Main Sections:
--------------
1. Initialization and Setup Functions
2. Antigenic Sites and Mutation Visualization
3. Image Export Functions
4. Process Sequence Function
5. Main Execution Block

Author: [Ashley Sobel Leonard]
Date: [08/09/2024]
"""
