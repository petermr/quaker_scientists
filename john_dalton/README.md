# John Dalton Knowledge Graph

This directory contains knowledge graphs representing the connections and relationships of John Dalton (1766-1844), a prominent English Quaker, chemist, physicist, and meteorologist best known for developing modern atomic theory.

## Files

### 1. `john_dalton_knowledge_graph.dot`
A comprehensive knowledge graph showing John Dalton's connections including:
- Family relationships (parents, siblings)
- Quaker mentors and influences
- Scientific colleagues and mentees
- Professional organizations and institutions
- Major scientific contributions and discoveries

### 2. `john_dalton_with_hyperlinks.dot` ⭐ **INTERACTIVE VERSION**
The most advanced version featuring:
- **All features from the basic version**
- **Clickable hyperlinks** to Wikipedia pages for all nodes
- **Interactive SVG format** for web viewing
- **Direct access** to detailed information about individuals and events
- **Perfect for digital research** and exploration
- Available in both PNG and SVG formats (SVG recommended for interactivity)

## Key Connections

### Family
- **Parents**: Joseph Dalton (Quaker weaver) and Deborah Greenup
- **Siblings**: Mary Dalton and Jonathan Dalton (both Quakers)

### Quaker Mentors
- **Elihu Robinson** (1734-1809): Early Quaker mentor and mathematician
- **John Gough** (1757-1825): Quaker mentor who taught Dalton mathematics and natural philosophy
- **George Bewley** (1750-1828): Quaker mentor and natural philosopher

### Scientific Colleagues (Quaker)
- **William Henry** (1774-1836): Quaker chemist, collaborator on gas laws
- **Thomas Thomson** (1773-1852): Quaker chemist, student of Dalton
- **James Prescott Joule** (1818-1889): Quaker physicist, influenced by Dalton
- **William Allen** (1770-1843): Quaker scientist, friend and collaborator
- **Luke Howard** (1772-1864): Quaker meteorologist, friend

### Non-Quaker Scientists
- **Joseph Priestley** (1733-1804): Dissenter chemist who influenced Dalton
- **Humphry Davy** (1778-1829): Anglican chemist, collaborator
- **Michael Faraday** (1791-1867): Anglican physicist, influenced by Dalton

### Organizations
- **Manchester Literary and Philosophical Society**: Quaker scientific group, member
- **Royal Society**: Anglican scientific institution, fellow (1822)
- **New College Manchester**: Quaker academy, teacher
- **Manchester Academy**: Quaker school, student
- **Askesian Society**: Quaker scientific group, member

### Major Scientific Contributions
- **Atomic Theory** (1808): Revolutionary theory of matter
- **Dalton's Law of Partial Pressures**: Fundamental gas law
- **Color Blindness Research** (1794): First scientific description of color vision deficiency
- **Meteorological Observations**: Systematic weather recording
- **A New System of Chemical Philosophy** (1808-1827): Major scientific work
- **Meteorological Observations and Essays** (1793): Early meteorological work

### Major Life Events
- **1793 Move to Manchester**: Relocated to center of scientific activity
- **1801 First Meteorological Journal**: Began systematic weather observations
- **1803 Atomic Theory Presentation**: First public presentation of atomic theory
- **1822 Royal Society Fellowship**: Recognition by establishment science
- **1833 French Academy Foreign Member**: International recognition

## How to Use

### Viewing the Graphs

1. **Install Graphviz** (if not already installed):
   ```bash
   # On macOS with Homebrew
   brew install graphviz
   
   # On Ubuntu/Debian
   sudo apt-get install graphviz
   
   # On Windows
   # Download from https://graphviz.org/download/
   ```

2. **Generate Images**:
   ```bash
   # Generate PNG from the basic graph
   dot -Tpng john_dalton_knowledge_graph.dot -o john_dalton_knowledge_graph.png
   
   # Generate SVG for better scalability
   dot -Tsvg john_dalton_knowledge_graph.dot -o john_dalton_knowledge_graph.svg
   
   # Generate interactive hyperlinked version (RECOMMENDED)
   dot -Tsvg john_dalton_with_hyperlinks.dot -o john_dalton_with_hyperlinks.svg
   dot -Tpng john_dalton_with_hyperlinks.dot -o john_dalton_with_hyperlinks.png
   ```

3. **View the graphs**:
   - Open the generated PNG or SVG files in any image viewer
   - For interactive viewing, open the SVG files in a web browser

### Understanding the Graph

- **Node Colors** (see legend in the graphs):
  - **Gold**: John Dalton (central figure)
  - **Pink**: Family members (Quaker - thick borders)
  - **Light Cyan**: Quaker mentors (thick borders)
  - **Light Steel Blue**: Quaker scientists (thick borders)
  - **Light Coral**: Non-Quaker scientists (thin borders)
  - **Light Gray**: Organizations (diamond shape - thick borders for Quaker organizations)
  - **Orange**: Scientific contributions (diamond shape - thick borders)
  - **Plum**: Major life events (diamond shape - thick borders)

- **Border Thickness**:
  - **Thick borders (penwidth=3)**: All Quaker individuals and organizations
  - **Thin borders**: Non-Quaker individuals and organizations
  - **"QUAKER" labels**: Clearly marked on all Quaker connections

- **Edge Labels**: Describe the type of relationship (e.g., "father", "mentor", "friend", "developed")

## Interactive Hyperlinks

The `john_dalton_with_hyperlinks.dot` version includes clickable links to Wikipedia pages for all nodes. Here's what you can explore:

### **How to Use the Hyperlinks:**
1. **SVG Format**: Open `john_dalton_with_hyperlinks.svg` in a web browser for full interactivity
2. **Clickable Nodes**: Each node is clickable and will open the corresponding Wikipedia page
3. **Compatible Viewers**: Works in most modern web browsers and SVG viewers

### **Linked Wikipedia Pages Include:**

#### **Individuals:**
- **John Dalton** - Main biographical page
- **Scientific Figures**: William Henry (Methodist), Thomas Thomson (Anglican), James Prescott Joule (Anglican), William Allen (Quaker), Luke Howard (Quaker)
- **Non-Quaker Scientists**: Joseph Priestley, Humphry Davy, Michael Faraday
- **Family Members**: All family connections

#### **Organizations & Institutions:**
- **Manchester Literary and Philosophical Society** - Scientific discussion group
- **Royal Society** - Establishment scientific institution
- **New College Manchester** - Quaker educational institution
- **Manchester Academy** - Quaker school
- **Askesian Society** - Quaker scientific group

#### **Scientific Contributions:**
- **Atomic Theory** - Revolutionary theory of matter
- **Dalton's Law** - Fundamental gas law
- **Color Blindness** - Vision research
- **A New System of Chemical Philosophy** - Major scientific work

### **Research Benefits:**
- **Quick Reference**: Click any node to learn more about that person or organization
- **Historical Context**: Access detailed biographical and historical information
- **Source Verification**: All links lead to reliable Wikipedia sources
- **Educational Tool**: Perfect for students and researchers exploring Quaker scientific networks

## Historical Context

John Dalton was a central figure in 18th-19th century Quaker science, connecting:
- **Chemistry**: Through his development of atomic theory and gas laws
- **Physics**: Through his work on partial pressures and meteorology
- **Education**: Through his teaching at Quaker institutions
- **Quaker Community**: Through extensive family and friendship networks
- **Scientific Societies**: Through membership in both Quaker and establishment organizations

The knowledge graphs visualize these interconnected relationships, showing how Dalton's influence extended across multiple domains of 19th-century British science while maintaining his Quaker identity.

## Sources

The information in these graphs is based on historical research about John Dalton and his connections, including:
- Biographical information about John Dalton
- Family trees and genealogical records
- Historical accounts of Quaker scientific networks
- Records of scientific societies and collaborations
- Scientific publications and correspondence
