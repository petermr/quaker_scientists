# Kathleen Lonsdale Knowledge Graph

This directory contains knowledge graphs representing the connections and relationships of Kathleen Lonsdale (1903-1971), a prominent English Quaker, crystallographer, and peace activist who was the first woman to be elected a Fellow of the Royal Society.

## Files

### 1. `kathleen_lonsdale_knowledge_graph.dot`
A comprehensive knowledge graph showing Kathleen Lonsdale's connections including:
- Family relationships (parents, husband, children)
- Quaker mentors and scientific colleagues
- Professional organizations and institutions
- Major scientific contributions and discoveries
- Significant life events and achievements

### 2. `kathleen_lonsdale_with_hyperlinks.dot` ⭐ **INTERACTIVE VERSION**
The most advanced version featuring:
- **All features from the basic version**
- **Clickable hyperlinks** to Wikipedia pages for all nodes
- **Interactive SVG format** for web viewing
- **Direct access** to detailed information about individuals and events
- **Perfect for digital research** and exploration
- Available in both PNG and SVG formats (SVG recommended for interactivity)

## Key Connections

### Family
- **Parents**: Harry Yardley (father) and Jessie Cameron (mother)
- **Husband**: Thomas Lonsdale (1900-1994), Quaker engineer
- **Children**: Jane, Nancy, and Patricia Lonsdale (all Quakers)

### Quaker Mentors & Scientific Colleagues
- **William Henry Bragg** (1862-1942): Quaker mentor and Nobel Prize winner
- **Lawrence Bragg** (1890-1971): Quaker colleague, son of William Henry Bragg
- **Dorothy Hodgkin** (1910-1994): Quaker crystallographer, Nobel Prize winner
- **Rosalind Franklin** (1920-1958): Quaker crystallographer, DNA structure researcher
- **John Desmond Bernal** (1901-1971): Quaker crystallographer and social activist

### Non-Quaker Scientists
- **Max Perutz** (1914-2002): Austrian crystallographer, Nobel Prize winner
- **Francis Crick** (1916-2004): Anglican biologist, DNA structure co-discoverer
- **James Watson** (1928-): Anglican biologist, DNA structure co-discoverer
- **Linus Pauling** (1901-1994): American chemist, Nobel Prize winner

### Organizations
- **University College London**: Quaker institution, professor of chemistry
- **Royal Institution**: Anglican scientific institution, researcher
- **Bedford College**: Quaker women's college, student
- **Royal Society**: Anglican scientific institution, first woman fellow (1945)
- **International Union of Crystallography**: Mixed Quaker/Anglican, first woman president (1966)
- **British Association for Advancement of Science**: Mixed Quaker/Anglican, first woman president (1968)
- **Quaker Society of Friends**: Quaker organization, member since 1936
- **Pugwash Conferences**: Quaker peace organization, member
- **Women's International League for Peace and Freedom**: Quaker organization, president
- **Howard League for Penal Reform**: Quaker organization, member

### Major Scientific Contributions
- **Benzene Structure Determination** (1929): First accurate determination of benzene's hexagonal structure
- **Diamond Structure Analysis** (1929): Confirmed diamond's tetrahedral structure
- **Hexachlorobenzene Structure** (1931): Determined structure of complex organic compound
- **Crystallographic Tables** (1934): Compiled essential reference tables for crystallographers
- **X-ray Diffraction Techniques**: Developed methods for analyzing crystal structures
- **Lonsdaleite**: Mineral named in her honor, discovered in meteorites

### Major Life Events
- **1922 Bedford College Student**: Attended Quaker women's college
- **1924 UCL Researcher**: Joined University College London
- **1927 Marriage to Thomas Lonsdale**: Married Quaker engineer
- **1936 Quaker Conversion**: Converted to Quakerism, influenced by pacifist beliefs
- **1943 Holloway Prison Imprisonment**: Imprisoned for refusing civil defense duties
- **1945 First Woman Royal Society Fellow**: Historic achievement
- **1949 UCL Professor of Chemistry**: First woman professor at UCL
- **1956 Dame Commander of the British Empire**: High honor for scientific achievement
- **1957 Davy Medal Award**: Prestigious chemistry award
- **1966 IUCr President First Woman**: First woman president of crystallography union
- **1968 BAAS President First Woman**: First woman president of science association
- **1971 Death London**: Died in London, aged 68

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
   dot -Tpng kathleen_lonsdale_knowledge_graph.dot -o kathleen_lonsdale_knowledge_graph.png
   
   # Generate SVG for better scalability
   dot -Tsvg kathleen_lonsdale_knowledge_graph.dot -o kathleen_lonsdale_knowledge_graph.svg
   
   # Generate interactive hyperlinked version (RECOMMENDED)
   dot -Tsvg kathleen_lonsdale_with_hyperlinks.dot -o kathleen_lonsdale_with_hyperlinks.svg
   dot -Tpng kathleen_lonsdale_with_hyperlinks.dot -o kathleen_lonsdale_with_hyperlinks.png
   ```

3. **View the graphs**:
   - Open the generated PNG or SVG files in any image viewer
   - For interactive viewing, open the SVG files in a web browser

### Understanding the Graph

- **Node Colors** (see legend in the graphs):
  - **Gold**: Kathleen Lonsdale (central figure)
  - **Pink**: Family members (Quaker - thick borders)
  - **Light Cyan**: Quaker scientists (thick borders)
  - **Light Coral**: Non-Quaker scientists (thin borders)
  - **Light Gray**: Organizations (diamond shape - thick borders for Quaker organizations)
  - **Orange**: Scientific contributions (diamond shape - thick borders)
  - **Plum**: Major life events (diamond shape - thick borders)

- **Border Thickness**:
  - **Thick borders (penwidth=3)**: All Quaker individuals and organizations
  - **Thin borders**: Non-Quaker individuals and organizations
  - **"QUAKER" labels**: Clearly marked on all Quaker connections

- **Edge Labels**: Describe the type of relationship (e.g., "father", "mentor", "friend", "discovered")

## Interactive Hyperlinks

The `kathleen_lonsdale_with_hyperlinks.dot` version includes clickable links to Wikipedia pages for all nodes. Here's what you can explore:

### **How to Use the Hyperlinks:**
1. **SVG Format**: Open `kathleen_lonsdale_with_hyperlinks.svg` in a web browser for full interactivity
2. **Clickable Nodes**: Each node is clickable and will open the corresponding Wikipedia page
3. **Compatible Viewers**: Works in most modern web browsers and SVG viewers

### **Linked Wikipedia Pages Include:**

#### **Individuals:**
- **Kathleen Lonsdale** - Main biographical page
- **Scientific Figures**: William Henry Bragg (Anglican), Lawrence Bragg (Anglican), Dorothy Hodgkin (Anglican), Rosalind Franklin (Jewish), John Desmond Bernal (Irish)
- **Non-Quaker Scientists**: Max Perutz, Francis Crick, James Watson, Linus Pauling
- **Family Members**: All family connections

#### **Organizations & Institutions:**
- **University College London** - Secular educational institution
- **Royal Institution** - Scientific institution
- **Bedford College** - Women's college
- **Royal Society** - Scientific society
- **International Union of Crystallography** - Professional organization
- **British Association for Advancement of Science** - Scientific organization
- **Quaker Society of Friends** - Religious organization
- **Pugwash Conferences** - Peace organization
- **Women's International League for Peace and Freedom** - Peace organization
- **Howard League for Penal Reform** - Reform organization

#### **Scientific Contributions:**
- **Benzene** - Chemical compound structure
- **Diamond** - Crystal structure
- **Hexachlorobenzene** - Chemical compound
- **X-ray Crystallography** - Scientific technique
- **Lonsdaleite** - Mineral named after her

### **Research Benefits:**
- **Quick Reference**: Click any node to learn more about that person or organization
- **Historical Context**: Access detailed biographical and historical information
- **Source Verification**: All links lead to reliable Wikipedia sources
- **Educational Tool**: Perfect for students and researchers exploring Quaker scientific networks

## Historical Context

Kathleen Lonsdale was a pioneering figure in 20th-century Quaker science, connecting:
- **Crystallography**: Through her groundbreaking work on molecular structures
- **Women's Rights**: Through her many "first woman" achievements
- **Peace Activism**: Through her Quaker pacifist beliefs and imprisonment
- **Social Reform**: Through her work on prison reform and peace organizations
- **Quaker Community**: Through extensive family and friendship networks
- **Scientific Societies**: Through leadership roles in major organizations

The knowledge graphs visualize these interconnected relationships, showing how Lonsdale's influence extended across multiple domains of 20th-century British science while maintaining her Quaker identity and commitment to peace and social justice.

## Sources

The information in these graphs is based on historical research about Kathleen Lonsdale and her connections, including:
- Biographical information about Kathleen Lonsdale
- Family trees and genealogical records
- Historical accounts of Quaker scientific networks
- Records of scientific societies and collaborations
- Scientific publications and correspondence
- Peace and social reform movement documentation
