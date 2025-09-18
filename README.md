# William Allen Knowledge Graph

This repository contains knowledge graphs representing the connections and relationships of William Allen (1770-1843), a prominent English Quaker, scientist, and philanthropist.

## Files

### 1. `william_allen_knowledge_graph.dot`
A comprehensive knowledge graph showing William Allen's connections including:
- Family relationships (parents, spouses, children)
- Hanbury family connections
- Bevan family connections  
- Birkbeck family connections
- Quaker friends and colleagues
- Scientific mentors and mentees
- Abolitionist collaborators
- Organizations and institutions

### 2. `william_allen_detailed_graph.dot`
A more detailed version with:
- Clustered groupings by relationship type
- More descriptive labels
- Additional context and details
- Better visual organization

### 3. `william_allen_corrected_graph.dot`
A corrected version that fixes layout issues and provides:
- Clean, readable layout
- All major connections included
- Proper color coding by relationship type
- Available in both PNG and SVG formats

### 4. `william_allen_simplified_graph.dot`
A simplified version focusing on the most important connections:
- Streamlined for easier reading
- Key family, business, and professional relationships
- Ideal for quick reference

### 5. `william_allen_quaker_highlighted.dot` ⭐ **RECOMMENDED**
The most comprehensive version with:
- **Quaker connections clearly highlighted** with thick borders and "QUAKER" labels
- **Complete color legend** explaining all color codes
- **Religious affiliations** clearly marked (Quaker vs Anglican)
- **Thick borders** for all Quaker individuals and organizations
- Available in both PNG and SVG formats

### 6. `william_allen_with_travels.dot` ⭐⭐ **MOST COMPREHENSIVE**
The complete version including:
- **All features from the Quaker-highlighted version**
- **Major travels and events** as a new category (orange diamonds)
- **Chronological events** from 1814-1841
- **International connections** and royal meetings
- **Educational and social reform initiatives**
- Available in both PNG and SVG formats

### 7. `william_allen/william_allen_with_hyperlinks.dot` ⭐⭐⭐ **INTERACTIVE VERSION**
The most advanced version featuring:
- **All features from the travels version**
- **Clickable hyperlinks** to Wikipedia pages for all nodes
- **Interactive SVG format** for web viewing
- **Direct access** to detailed information about individuals and events
- **Perfect for digital research** and exploration
- Available in both PNG and SVG formats (SVG recommended for interactivity)
- **Located in `william_allen/` subdirectory** for organized access

## Key Connections

### Family
- **Parents**: Job Allen (silk manufacturer) and Margaret Stafford
- **Spouses**: 
  - Mary Hamilton (1796, died shortly after childbirth)
  - Charlotte Hanbury (1806-1816)
  - Grizell Birkbeck (1827-1835)
- **Children**: Mary Allen (married Cornelius Hanbury)

### Hanbury Family
- **Cornelius Hanbury**: Son-in-law, married to Mary Allen
- **Daniel Bell Hanbury**: Business partner in Plough Court Pharmacy
- **Daniel Hanbury**: Botanist, son of Daniel Bell Hanbury

### Bevan Family
- **Silvanus Bevan**: Founder of Plough Court Pharmacy
- **Timothy Bevan**: Brother of Silvanus
- **Joseph Gurney Bevan**: Son of Timothy, managed the pharmacy before Allen

### Birkbeck Family
- **Wilson Birkbeck**: First husband of Grizell Birkbeck
- **Samuel Hoare Jr**: Brother of Grizell, prominent abolitionist

### Quaker Scientists & Friends
- **Luke Howard**: Meteorologist, co-founder of Askesian Society
- **Joseph Fox, William Hasledine Pepys, William Babington, Astley Cooper**: Members of Askesian Society
- **Joseph Woods Sr**: Fellow Quaker and abolitionist

### Scientific Mentors
- **Humphry Davy**: Renowned chemist
- **John Dalton**: Chemist and physicist

### Abolitionist Colleagues
- **William Wilberforce**: Parliamentary abolitionist
- **Thomas Clarkson**: Early abolitionist
- **Stephen Grellet, Daniel Wheeler**: Quaker missionaries

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
   dot -Tpng william_allen_knowledge_graph.dot -o william_allen_graph.png
   
   # Generate PNG from the detailed graph
   dot -Tpng william_allen_detailed_graph.dot -o william_allen_detailed_graph.png
   
   # Generate SVG for better scalability
   dot -Tsvg william_allen_detailed_graph.dot -o william_allen_detailed_graph.svg
   
   # Generate interactive hyperlinked version (RECOMMENDED)
   dot -Tsvg william_allen_with_hyperlinks.dot -o william_allen_with_hyperlinks.svg
   dot -Tpng william_allen_with_hyperlinks.dot -o william_allen_with_hyperlinks.png
   ```

3. **View the graphs**:
   - Open the generated PNG or SVG files in any image viewer
   - For interactive viewing, you can use online Graphviz viewers

### Understanding the Graph

- **Node Colors** (see legend in `william_allen_quaker_highlighted.dot`):
  - **Gold**: William Allen (central figure)
  - **Pink**: Family members (mostly Quaker - thick borders)
  - **Light Blue**: Hanbury family (Quaker - thick borders)
  - **Light Green**: Bevan family (Quaker - thick borders)
  - **Light Yellow**: Birkbeck family (Quaker - thick borders)
  - **Light Cyan**: Quaker friends and scientists (thick borders)
  - **Light Coral**: Abolitionists (mixed Quaker/Anglican - thick borders for Quakers)
- **Light Steel Blue**: Scientific mentors (mixed Quaker/Anglican - thick borders for Quakers)
- **Light Gray**: Organizations (diamond shape - thick borders for Quaker organizations)
- **Orange**: Major travels and events (diamond shape - thick borders for Quaker events)
- **Plum**: Royal connections (thin borders)

- **Border Thickness**:
  - **Thick borders (penwidth=3)**: All Quaker individuals and organizations
  - **Thin borders**: Non-Quaker individuals and organizations
  - **"QUAKER" labels**: Clearly marked on all Quaker connections

- **Edge Labels**: Describe the type of relationship (e.g., "father", "married", "friend", "mentor")

- **Clusters**: In the detailed graph, related nodes are grouped together for better organization

## Quaker Connections Highlighted

The `william_allen_quaker_highlighted.dot` graph specifically highlights William Allen's extensive Quaker network:

### **Quaker Individuals** (marked with thick borders and "QUAKER" labels):
- **All family members** (parents, wives, daughter)
- **Hanbury family** (son-in-law, business partners, descendants)
- **Bevan family** (pharmacy founders and managers)
- **Birkbeck family** (third wife and her relatives)
- **Scientific colleagues** (Luke Howard, Joseph Fox, William Hasledine Pepys, William Babington, Astley Cooper, Joseph Woods Sr)
- **Missionaries** (Stephen Grellet, Daniel Wheeler)
- **Mentor** (John Dalton)

### **Quaker Organizations** (marked with thick borders):
- **Askesian Society** (scientific discussion group)
- **Plough Court Pharmacy** (pharmaceutical business)
- **Newington Academy for Girls** (educational institution)

### **Non-Quaker Connections** (thin borders):
- **Humphry Davy** (Anglican chemist mentor)
- **William Wilberforce** (Anglican parliamentarian)
- **Thomas Clarkson** (Anglican abolitionist)
- **Royal Institution** (Anglican scientific institution)
- **Society for Abolition of Slave Trade** (mixed Quaker/Anglican)

## Major Travels and Events

The `william_allen_with_travels.dot` graph includes a comprehensive timeline of William Allen's major travels and significant events (marked with orange diamonds):

### **International Meetings & Travels:**
- **1814 Meeting with Tsar Alexander I** (London) - Hosted the Russian Emperor who was interested in Quaker educational methods
- **1818-1820 European Tour** - Traveled with Stephen Grellet, visiting Norway and other European countries
- **1819 Russia Visit** - Visited Russia, meeting Tsar Alexander I to discuss educational reforms
- **1840 European Tour** - Traveled with Elizabeth Fry and Samuel Gurney, spending five months in Europe

### **Educational & Social Reform Initiatives:**
- **1823 Lindfield Community** - Established agricultural experiment community in Sussex
- **1824 Newington Academy for Girls Founded** - Co-founded with Grizell Birkbeck, offering wide range of subjects including sciences
- **1824 First School Bus Commissioned** - Pioneered the first school bus for the Newington Academy
- **1839 British and Foreign Anti-Slavery Society** - Co-founded for worldwide abolition of slavery
- **1840 International Anti-Slavery Conference** (London) - Organized the first international conference on abolition
- **1841 Pharmaceutical Society Founded** - Co-founded to provide structure to the pharmaceutical industry

### **Additional Organizations:**
- **British and Foreign School Society** (founded 1808) - Promoted Joseph Lancaster's monitorial system of education
- **Sierra Leone Company** (founded 1791) - Aimed to resettle freed slaves in Africa
- **Soup Kitchen in Spitalfields** (early 1800s) - Provided relief to impoverished silk workers

## Interactive Hyperlinks

The `william_allen/william_allen_with_hyperlinks.dot` version includes clickable links to Wikipedia pages for all nodes. Here's what you can explore:

### **How to Use the Hyperlinks:**
1. **SVG Format**: Open `william_allen_with_hyperlinks.svg` in a web browser for full interactivity
2. **Clickable Nodes**: Each node is clickable and will open the corresponding Wikipedia page
3. **Compatible Viewers**: Works in most modern web browsers and SVG viewers

### **Linked Wikipedia Pages Include:**

#### **Individuals:**
- **William Allen** - Main biographical page
- **Scientific Figures**: Luke Howard, Humphry Davy, John Dalton, William Hasledine Pepys, William Babington, Astley Cooper
- **Abolitionists**: William Wilberforce, Thomas Clarkson, Elizabeth Fry, Joseph Sturge
- **Quaker Friends**: Stephen Grellet, Daniel Wheeler, Samuel Gurney, Samuel Hoare Jr
- **Family Members**: Hanbury family, Bevan family connections
- **Royal Connections**: Tsar Alexander I

#### **Organizations & Institutions:**
- **Askesian Society** - Scientific discussion group
- **Allen & Hanburys** - Pharmaceutical business
- **Newington Academy for Girls** - Educational institution
- **Royal Institution** - Scientific lectures
- **British and Foreign School Society** - Educational reform
- **Sierra Leone Company** - Abolitionist organization
- **Royal Pharmaceutical Society** - Professional organization
- **Society for Abolition of Slave Trade** - Abolitionist movement

#### **Major Events:**
- **World Anti-Slavery Convention** (1840) - International conference
- **British and Foreign Anti-Slavery Society** - Worldwide abolition efforts

### **Research Benefits:**
- **Quick Reference**: Click any node to learn more about that person or organization
- **Historical Context**: Access detailed biographical and historical information
- **Source Verification**: All links lead to reliable Wikipedia sources
- **Educational Tool**: Perfect for students and researchers exploring Quaker networks

## Historical Context

William Allen was a central figure in 18th-19th century Quaker society, connecting:
- **Science**: Through the Askesian Society and his work in chemistry
- **Business**: Through the Plough Court Pharmacy and pharmaceutical partnerships
- **Social Reform**: Through abolitionist work and educational initiatives
- **Quaker Community**: Through extensive family and friendship networks

The knowledge graphs visualize these interconnected relationships, showing how Allen's influence extended across multiple domains of 19th-century British society.

## Sources

The information in these graphs is based on historical research about William Allen and his connections, including:
- Biographical information about William Allen
- Family trees and genealogical records
- Historical accounts of Quaker networks
- Records of scientific societies and collaborations
- Abolitionist movement documentation
