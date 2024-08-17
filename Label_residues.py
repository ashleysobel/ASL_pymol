

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

def assess_mutations_HA(seq_name, H1_mutations=None, H2_mutations=None, color='grey20'):
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
        cmd.color(color, seq_name)
        cmd.show('surface', seq_name)
        cmd.set('surface_color', color, seq_name)

def clear_all_selections():
    """Clear all selections, reset colors, and remove custom selections."""
    cmd.hide('everything')
    cmd.color(DEFAULT_COLOR, 'all')
    cmd.show('surface')
    cmd.show('cartoon')
    cmd.delete('all')

def label_sequence(seq_name, cif_file_path, strain_type, H1_mutations, H2_mutations, color='grey20'):
    """Process a sequence by setting up the base, assessing mutations, and generating images."""
    
    # Clear prior functions
    clear_all_selections()

    # Set up the base environment
    set_base(cif_file_path)
    set_antigenic_sites(strain_type)
    
    # Assess mutations and generate images
    assess_mutations_HA(seq_name, H1_mutations, H2_mutations, color=color)

label_sequence(seq_name='test', cif_file_path=cif_file_path, strain_type='H1N1', H1_mutations=[142,189], H2_mutations=[],color='tv_red')
