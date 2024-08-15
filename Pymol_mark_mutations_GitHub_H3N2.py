# Pymol_mark_mutations_GitHub.py

# To run this code through pymol, copy: "run /path/to/code/location" into pymol command line input
# Ex: run /Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Pymol_mark_mutations.py
# Must update the following to run on a new computer: 
# 1. DEFAULT_OUTPUT_LOCATION: set to wherever you want the images to be saved to
# 2. cif_file_path: set this path to wherever your "4lxv-assembly1.cif" is saved to
# 3. strain_type: set this as either "H1N1 or "H3N2" (though H3N2 is not set up right now)
# 4. If you want to change the background color for the protein structure, you can do it here
# Instructions for running the code for a sequence or set of sequences: 
# Option 1: Fill out the process_sequence() definition for each of the sequences. This will generate 2 views of the protein for each of the listed sequnces. The final sequence will remain visible in the pymol interface
# Option 2: Copy and paste the entries for the process_sequence() definition one by one into the interface. This will generate and export the images, but will leave each structure visible.
# Option 3: You can run each of the individual functions separately, but remember to clear_all_selections() between seperate sampels to reset labelled residues

from pymol import cmd
import os

# Constants 
DEFAULT_OUTPUT_LOCATION = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Python_code/ImageOutput/"
DEFAULT_COLOR = 'grey70'

# ---------------------------------------------------
# Initialization and Setup Functions
# ---------------------------------------------------

def clear_all_selections():
    """Clear all selections, reset colors, and remove custom selections."""
    cmd.hide('everything')
    cmd.color(DEFAULT_COLOR, 'all')
    cmd.show('surface')
    cmd.show('cartoon')
    cmd.delete('all')

def set_base(cif_file_path):
    """Set up the base configuration for the structure."""
    cmd.load(cif_file_path)
    cmd.hide('all')
    cmd.show('surface')
    cmd.show('cartoon')
    cmd.set('surface_color', DEFAULT_COLOR)
    cmd.set('cartoon_color', DEFAULT_COLOR)
    cmd.set('bg_rgb', [1, 1, 1])
    cmd.set('ambient', 0.4)
    cmd.space('cmyk')
    cmd.set('ray_trace_fog', 0)
    cmd.set('depth_cue', 1)
    cmd.set('ray_trace_mode', 1)
    cmd.set('ray_trace_gain', 0.002)

# ---------------------------------------------------
# Antigenic Sites and Mutation Visualization
# ---------------------------------------------------

def set_antigenic_sites(strain_type):
    """Set and color the antigenic sites based on the strain type."""
    
    # Define color mapping for each site
    site_colors = {
        'site_Sa': 'lightpink',
        'site_Sb': 'lightblue',
        'site_Ca1': 'paleyellow',
        'site_Ca2': 'palecyan',
        'site_Cb': 'lightorange',
        'site_A': 'lightpink',
        'site_B': 'lightblue',
        'site_C': 'paleyellow',
        'site_D': 'palecyan',
        'site_E': 'lightorange',
    }
    
    if strain_type == 'H1N1':
        antigenic_sites = {
            'site_Sa': '(chain A or chain C or chain E) and resi 124-125+153-157+159-164',
            'site_Sb': '(chain A or chain C or chain E) and resi 184-194',
            'site_Ca1': '(chain A or chain C or chain E) and resi 166-170+203-205+235-237',
            'site_Ca2': '(chain A or chain C or chain E) and resi 137-142+221-222',
            'site_Cb': '(chain A or chain C or chain E) and resi 70-75',
        }
    elif strain_type == 'H3N2':
        antigenic_sites = {
            'site_A': "chain A+A-2+A-3 and resi 122-127+129+131-138+142-146",
            'site_B': "chain A+A-2+A-3 and resi 155-160+164+188-190+193-194+196-197",
            'site_C': "chain A+A-2+A-3 and resi 50+53+54+275",
            'site_D': "chain A+A-2+A-3 and resi 201-207+213+217-220+230+244",
            'site_E': "chain A+A-2+A-3 and resi 62-63+75+79-83",
        }
    else:
        print("Invalid strain type. Please use 'H1N1' or 'H3N2'.")
        return

    # Apply selections and colors
    for site, selection in antigenic_sites.items():
        cmd.select(site, selection)
        cmd.color(site_colors[site], site)  # Use the correct color from the dictionary
        cmd.show('surface', site)
        cmd.set('surface_color', site, site)

def set_clade_subclade(strain_type, clade_name, subclade_name=None):
    """Set and color the clade and optional subclade-defining mutations."""
    subclade_name = f"Subclade_{subclade_name}" if subclade_name else None

clade_residues = {
    'H1N1': {
        '5a.2': {'A+C+E': '74+97+129+162+163+164+185+216+256+295','B+D+F':'124'},
        '5a.2a': {'A+C+E': '54+129+156+161+185+186+189+308'},
        '5a.2a.1': {'A+C+E': '54+129+137+142+156+161+185+186+189+308'}
    },
    'H3N2': {
        '2a.1':{
            'A+A-2+A-3': '45+48+3+144+159+160+121+171+62+142+311+131+83+94+164+186+190+193+195+156+53+104+276',
            'B+B-2+B-3': '160+77+155+200+193'
        },
        '2a.1b':{
            'A+A-2+A-3': '45+48+3+144+159+160+121+171+62+142+311+131+83+94+164+186+190+193+195+156+53+104+276+140+299',
            'B+B-2+B-3': '160+77+155+200+193'
        },
        '2b':{
            'A+A-2+A-3': '45+48+3+144+159+160+121+171+62+142+311+131+83+94+164+186+190+193+195+50+79+140',
            'B+B-2+B-3': '160+77+155+200+193'
        }
    }
}

    subclade_residues = {
        'H3N2':{
            '2a.1':{
        },
            '2a.1b':{
        },
        '2b':{
         }
        },
        'H1N1': {
            '5a.2':{
                'Subclade_C':{'A+C+E': '156+161'}
            },
            '5a.2a': {
                'Subclade_C.1': {'A+C+E': '54+186+189+308'},
                'Subclade_C.1.8': {'A+C+E': '54+186+189+308+120+47'},
                'Subclade_C.1.9': {'A+C+E': '54+186+189+308+120+169'}
            },
            '5a.2a.1': {
                'Subclade_C.1.1': {'A+C+E': '137+142'},
                'Subclade_D': {'A+C+E': '54+186+189+308+216'},
                'Subclade_D.1': {'A+C+E': '54+186+189+308+45+216'},
                'Subclade_D.2': {'A+C+E': '54+186+189+308+113+216'},
                'Subclade_D.3': {'A+C+E': '54+186+189+308+120', 'B+D+F': '45'}
            }
        },
        'H3N2': {
            # Add H3N2 subclade residues here
        }
    }

    if strain_type not in clade_residues or strain_type not in subclade_residues:
        print(f"Strain type {strain_type} not recognized. Please ensure the strain type is correct.")
        return

    if clade_name not in clade_residues[strain_type]:
        print(f"Clade {clade_name} not recognized. Please ensure the clade name is correct.")
        return

    for chain_group, residues in clade_residues[strain_type][clade_name].items():
        cmd.select(clade_name, f'chain {chain_group} and resi {residues}')
        cmd.color('tv_blue', clade_name)
        cmd.show('surface', clade_name)
        cmd.set('surface_color', clade_name, clade_name)

    if subclade_name:
        if subclade_name in subclade_residues[strain_type].get(clade_name, {}):
            for chain_group, residues in subclade_residues[strain_type][clade_name][subclade_name].items():
                cmd.select(subclade_name, f'chain {chain_group} and resi {residues}')
                cmd.color('tv_green', subclade_name)
                cmd.show('surface', subclade_name)
                cmd.set('surface_color', subclade_name, subclade_name)
        else:
            print(f"Subclade {subclade_name} does not match clade {clade_name}.")
            return

    """Set and color the clade and optional subclade-defining mutations."""
    subclade_name = f"Subclade_{subclade_name}" if subclade_name else None

    clade_residues = {
        'H1N1':{
            '5a.2': {'A+C+E': '74+97+129+162+163+164+185+216+256+295','B+D+F':'124'},
            '5a.2a': {'A+C+E': '54+129+156+161+185+186+189+308'},
            '5a.2a.1': {'A+C+E': '54+129+137+142+156+161+185+186+189+308'}
        },
        'H3N2':{
            # Add H3N2 clade residues here
        }
    }
    subclade_residues = {
    	'5a.2':{
    		'Subclade_C':{'A+C+E': '156+161'}
    	},
        '5a.2a': {
            'Subclade_C.1': {'A+C+E': '54+186+189+308'},
            'Subclade_C.1.8': {'A+C+E': '54+186+189+308+120+47'},
            'Subclade_C.1.9': {'A+C+E': '54+186+189+308+120+169'}
        },
        '5a.2a.1': {
            'Subclade_C.1.1': {'A+C+E': '137+142'},
            'Subclade_D': {'A+C+E': '54+186+189+308+216'},
            'Subclade_D.1': {'A+C+E': '54+186+189+308+45+216'},
            'Subclade_D.2': {'A+C+E': '54+186+189+308+113+216'},
            'Subclade_D.3': {'A+C+E': '54+186+189+308+120', 'B+D+F': '45'}
        }
    }

    if clade_name not in clade_residues:
        print(f"Clade {clade_name} not recognized. Please ensure the clade name is correct.")
        return

    for chain_group, residues in clade_residues[clade_name].items():
        cmd.select(clade_name, f'chain {chain_group} and resi {residues}')
        cmd.color('tv_blue', clade_name)
        cmd.show('surface', clade_name)
        cmd.set('surface_color', clade_name, clade_name)

    if subclade_name:
        if subclade_name in subclade_residues.get(clade_name, {}):
            for chain_group, residues in subclade_residues[clade_name][subclade_name].items():
                cmd.select(subclade_name, f'chain {chain_group} and resi {residues}')
                cmd.color('tv_green', subclade_name)
                cmd.show('surface', subclade_name)
                cmd.set('surface_color', subclade_name, subclade_name)
        else:
            print(f"Subclade {subclade_name} does not match clade {clade_name}.")
            return

def assess_mutations_HA(seq_name, H1_mutations=None, H2_mutations=None):
    """Assess and display mutations for HA protein chains under the same selection name."""
    selection_string = ""
    if H1_mutations:
        H1_residues = "+".join(map(str, H1_mutations))
        selection_string += f"(chain A+C+E and resi {H1_residues})"
    if H2_mutations:
        H2_residues = "+".join(map(str, H2_mutations))
        if selection_string:
            selection_string += " or "
        selection_string += f"(chain B+D+F and resi {H2_residues})"

    if selection_string:
        cmd.select(seq_name, selection_string)
        cmd.color('grey20', seq_name)
        cmd.show('surface', seq_name)
        cmd.set('surface_color', 'grey20', seq_name)

# ---------------------------------------------------
# Image Export
# ---------------------------------------------------

def generate_image(seq_name, view, protein, clade, subclade, output_location=None):
    """Generate an image with the specified view and save it to the output location."""
    if output_location is None:
        output_location = DEFAULT_OUTPUT_LOCATION

    if view == 'side':
        cmd.set_view([
            0.888682842,  0.371483058, -0.268776417,
           -0.303239465,  0.915848851,  0.263189942,
            0.343927294, -0.152389228,  0.926546395,
            0.000021487,  0.000063539, -474.919036865,
           76.153892517, 223.045745850, 287.983581543,
         -19575.746093750, 20525.484375000,  -20.000000000
        ])
    elif view == 'top':
        cmd.set_view([
            0.795617044,  0.577678502,  0.182431772,
           -0.285880089,  0.092522122,  0.953790188,
            0.534102142, -0.811003804,  0.238758013,
            0.000021487,  0.000063539, -474.919036865,
           76.153892517, 223.045745850, 287.983581543,
         -21575.746093750, 22525.484375000,  -20.000000000
        ])
    
    # Create the subdirectory for the protein if it doesn't exist
    protein_path = os.path.join(output_location, protein)
    os.makedirs(protein_path, exist_ok=True)
    
   # Generate the filename based on provided arguments
    filename_parts = [seq_name] if seq_name else []
    filename_parts.append(protein)
    filename_parts.append(clade.replace('.', ''))

    if subclade:
        filename_parts.append(subclade.replace('.', ''))

    filename_parts.append(view)
    filename = "_".join(filename_parts) + ".png"

    full_path = os.path.join(protein_path, filename)
    
    # Clear selections to avoid showing selection dots in the image
    cmd.deselect()
    
    # Aggressively zoom in on the visible structure to reduce white space
    cmd.zoom('visible', buffer=0)  # Tight zoom
    
    # Further adjust clipping planes to reduce white space
    cmd.clip('near', -5)  # Adjust near clipping plane
    cmd.clip('far', 5)    # Adjust far clipping plane
    
    # Save the image with high DPI
    cmd.png(full_path, dpi=300)
    print(f"Image saved to: {full_path}")

# Example usage:
# generate_image(seq_name='AAID1', view='side', protein='H1', clade='5a.2a', subclade='C.1.9')


def process_sequence(seq_name, cif_file_path, strain_type, clade, subclade, H1_mutations, H2_mutations):
    """Process a sequence by setting up the base, assessing mutations, and generating images."""
    
    # Clear prior functions
    clear_all_selections()

    # Set up the base environment
    set_base(cif_file_path)
    set_antigenic_sites(strain_type)
    set_clade_subclade(strain_type,clade, subclade)
    
    # Assess mutations and generate images
    assess_mutations_HA(seq_name, H1_mutations, H2_mutations)
    generate_image(seq_name=seq_name, view='side', protein='H1', clade=clade, subclade=subclade)
    generate_image(seq_name=seq_name, view='top', protein='H1', clade=clade, subclade=subclade)
    

print("Loaded Functions")
 

# ----------------------------------------------
# Manual Execution Instructions
# ----------------------------------------------

# Set the path for the cif file
cif_file_path = "/Users/ashleysobelleonard/code/CHOP_Pymol/CHOC-Prospective/Hemagglutinin/H1/4lxv-assembly1.cif"

# To use this script, manually run the `process_sequence()` function in the PyMOL command line or script. 
# Example 1: Generate images for specific mutations
# Copy and paste the following line into the PyMOL command line (has options filled out):
process_sequence(seq_name='temp4', cif_file_path=cif_file_path, strain_type='H1N1', clade='5a.2', subclade=None, H1_mutations=[145, 188], H2_mutations=[100])

# Example 2: Generate images with no mutations
# Copy and paste the following line into the PyMOL command line (instructions for filling out command below):
# process_sequence(seq_name='your_sequence_name', cif_file_path='/path_to_your_cif_file.cif', strain_type='H1N1', clade='your_clade', subclade='your_subclade', H1_mutations=[], H2_mutations=[])