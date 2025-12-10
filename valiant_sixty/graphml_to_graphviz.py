#!/usr/bin/env python3
"""
Convert GraphML to Graphviz DOT format and render to SVG
"""

import networkx as nx
import sys
import os

def graphml_to_dot(graphml_file, dot_file):
    """Convert GraphML file to Graphviz DOT format"""
    
    # Read GraphML file
    print(f"Reading GraphML file: {graphml_file}")
    G = nx.read_graphml(graphml_file)
    
    # Create DOT file content
    dot_lines = []
    dot_lines.append('digraph ValiantSixty {')
    dot_lines.append('    // Graph settings')
    dot_lines.append('    rankdir=TB;')
    dot_lines.append('    node [shape=box, style=filled, fontname="Arial", fontsize=9];')
    dot_lines.append('    edge [fontname="Arial", fontsize=7];')
    dot_lines.append('')
    
    # Process nodes
    print(f"Processing {len(G.nodes())} nodes...")
    for node_id, data in G.nodes(data=True):
        # Get node attributes
        name = data.get('name', node_id)
        node_type = data.get('type', 'Person')
        subtype = data.get('subtype', '')
        birth_date = data.get('birth_date', '')
        death_date = data.get('death_date', '')
        quaker_status = data.get('quaker_status', '')
        fillcolor = data.get('fillcolor', 'lightgray')
        penwidth = data.get('penwidth', 1)
        shape = data.get('shape', 'box')
        label = data.get('label', name)
        wikipedia_url = data.get('wikipedia_url', '')
        quaker_org_url = data.get('quaker_org_url', '')
        
        # Build node definition
        node_attrs = []
        node_attrs.append(f'fillcolor={fillcolor}')
        node_attrs.append(f'penwidth={penwidth}')
        node_attrs.append(f'shape={shape}')
        
        # Add URL if available (prefer Wikipedia, then Quaker.org)
        url = wikipedia_url if wikipedia_url else quaker_org_url
        if url:
            node_attrs.append(f'URL="{url}"')
        
        # Create label with proper escaping
        label_escaped = label.replace('"', '\\"').replace('\n', '\\n')
        node_attrs.append(f'label="{label_escaped}"')
        
        # Add fontweight for central figures (gold) or Quaker members
        if fillcolor == 'gold' or quaker_status == 'QUAKER':
            node_attrs.append('fontweight=bold')
        
        # Build node line
        attrs_str = ', '.join(node_attrs)
        node_line = f'    "{node_id}" [{attrs_str}];'
        dot_lines.append(node_line)
    
    dot_lines.append('')
    
    # Process edges
    print(f"Processing {len(G.edges())} edges...")
    for source, target, data in G.edges(data=True):
        relationship_type = data.get('relationship_type', 'related')
        label = data.get('label', relationship_type)
        description = data.get('description', '')
        
        # Build edge definition
        edge_attrs = []
        edge_attrs.append(f'label="{label}"')
        
        if description:
            # Add tooltip with description
            tooltip = description.replace('"', '\\"')
            edge_attrs.append(f'tooltip="{tooltip}"')
        
        attrs_str = ', '.join(edge_attrs)
        edge_line = f'    "{source}" -> "{target}" [{attrs_str}];'
        dot_lines.append(edge_line)
    
    # Add legend
    dot_lines.append('')
    dot_lines.append('    // Legend')
    dot_lines.append('    subgraph cluster_legend {')
    dot_lines.append('        label="LEGEND - Color Coding & Quaker Connections";')
    dot_lines.append('        style=filled;')
    dot_lines.append('        fillcolor=white;')
    dot_lines.append('        fontsize=12;')
    dot_lines.append('        fontweight=bold;')
    dot_lines.append('')
    dot_lines.append('        "Central Figures\n(Thick Border)" [fillcolor=gold, penwidth=3, fontweight=bold];')
    dot_lines.append('        "QUAKER Family\n(Thick Border)" [fillcolor=lightpink, penwidth=3, fontweight=bold];')
    dot_lines.append('        "QUAKER Leaders\n(Thick Border)" [fillcolor=lightcyan, penwidth=3, fontweight=bold];')
    dot_lines.append('        "Valiant Sixty Members\n(Thick Border)" [fillcolor=lightsteelblue, penwidth=3, fontweight=bold];')
    dot_lines.append('        "Non-Quaker\n(Thin Border)" [fillcolor=lightcoral, penwidth=1];')
    dot_lines.append('        "QUAKER Places\n(Thick Border)" [fillcolor=lightgray, penwidth=3, fontweight=bold, shape=diamond];')
    dot_lines.append('        "Events\n(Thick Border)" [fillcolor=orange, penwidth=3, fontweight=bold, shape=diamond];')
    dot_lines.append('    }')
    
    dot_lines.append('}')
    
    # Write DOT file
    dot_content = '\n'.join(dot_lines)
    with open(dot_file, 'w', encoding='utf-8') as f:
        f.write(dot_content)
    
    print(f"DOT file created: {dot_file}")
    return dot_file

def render_to_svg(dot_file, svg_file):
    """Render DOT file to SVG using Graphviz"""
    import subprocess
    
    print(f"Rendering SVG from: {dot_file}")
    
    # Check if dot command is available
    try:
        result = subprocess.run(['dot', '-V'], capture_output=True, text=True)
        print(f"Graphviz version: {result.stderr.strip()}")
    except FileNotFoundError:
        print("Error: Graphviz 'dot' command not found.")
        print("Please install Graphviz:")
        print("  macOS: brew install graphviz")
        print("  Ubuntu/Debian: sudo apt-get install graphviz")
        print("  Windows: Download from https://graphviz.org/download/")
        return False
    
    # Render to SVG
    try:
        subprocess.run(['dot', '-Tsvg', dot_file, '-o', svg_file], check=True)
        print(f"SVG file created: {svg_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error rendering SVG: {e}")
        return False

def main():
    # File paths
    graphml_file = 'valiant_sixty_basic.graphml'
    dot_file = 'valiant_sixty_basic.dot'
    svg_file = 'valiant_sixty_basic.svg'
    
    # Check if GraphML file exists
    if not os.path.exists(graphml_file):
        print(f"Error: GraphML file not found: {graphml_file}")
        sys.exit(1)
    
    # Convert GraphML to DOT
    try:
        graphml_to_dot(graphml_file, dot_file)
    except Exception as e:
        print(f"Error converting GraphML to DOT: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Render to SVG
    if render_to_svg(dot_file, svg_file):
        print(f"\nSuccess! Files created:")
        print(f"  - DOT: {dot_file}")
        print(f"  - SVG: {svg_file}")
    else:
        print(f"\nDOT file created: {dot_file}")
        print("SVG rendering failed. You can manually render with:")
        print(f"  dot -Tsvg {dot_file} -o {svg_file}")

if __name__ == "__main__":
    main()





