# Valiant Sixty Knowledge Graph: Data Collection Method and Graph Building Strategy

**Date:** November 28, 2025  
**Project:** The Valiant Sixty Knowledge Graph

---

## Data Collection Method

### **Overview**
A systematic, source-verified approach to collecting biographical and relational data about The Valiant Sixty from authoritative Quaker sites and Wikipedia, ensuring complete provenance documentation for every data point.

### **Phase 1: Source Identification and List Compilation**

#### **Step 1: Source Discovery**
- **Quaker Official Sites:**
  - Search quaker.org.uk for "Valiant Sixty" or "First Publishers of Truth"
  - Browse historical archives and biographical pages
  - Check Friends Historical Library (Swarthmoor College) collections
  - Review Quaker Tapestry historical panels
  - Search local Quaker meeting house websites

- **Wikipedia Sources:**
  - Search en.wikipedia.org for "Valiant Sixty" article
  - Search individual member names with "Quaker" qualifier
  - Verify articles have citations and references sections
  - Prefer "Good Article" or "Featured Article" status
  - Follow citation links to verify reliability

#### **Step 2: Canonical List Creation**
- Extract complete membership list from primary sources
- Cross-reference multiple sources to resolve discrepancies
- Document alternative names: "Valiant 60", "First Publishers of Truth"
- Create master spreadsheet with:
  - Full names and variations
  - Birth/death dates (if known)
  - Birth locations
  - Primary ministry areas
  - Known aliases

#### **Step 3: Source Inventory**
- Create source log spreadsheet
- Document all URLs accessed
- Record date of access for each source
- Note source type (Quaker site / Wikipedia)
- Track citation quality and reliability

### **Phase 2: Individual Biographical Data Collection**

For each member, systematically collect:

#### **Core Biographical Data**
- **Names:** Full name, variations, aliases, titles
- **Vital Statistics:** Birth date/place, death date/place (with sources)
- **Family:** Parents, spouse(s), children, siblings (names, Quaker status)
- **Occupation:** Pre-Quaker occupation, social class, education level

#### **Quaker Ministry Data**
- **Conversion:** Date, location, circumstances, who influenced
- **Ministry Activities:** Areas traveled, dates of journeys, meetings established
- **Writings:** Published works, letters, journals (titles, dates, availability)
- **Persecution:** Imprisonments (dates, locations, reasons), other persecutions
- **Roles:** Meeting roles (clerk, elder), Yearly Meeting participation

#### **Relationship Data**
- **Mentors:** George Fox, Margaret Fell, other early leaders
- **Peers:** Other Valiant Sixty members (traveling companions, correspondents)
- **Mentees:** Quakers they influenced or converted
- **Non-Quaker Connections:** Authorities, opponents, supporters

#### **Historical Context**
- **Geographic:** Birth region, ministry areas, associated meeting houses
- **Temporal:** Key dates in Quaker history during their lifetime
- **Social:** Social class, economic status, networks

#### **Legacy Data**
- **Memorials:** Meeting houses, plaques, commemorations
- **Historical Recognition:** Mentions in histories, biographical treatments

### **Phase 3: Relationship Mapping**

#### **Relationship Identification**
- Extract relationship mentions from biographical texts
- Cross-reference relationship claims across sources
- Document relationship types:
  - Family (parent, child, spouse, sibling)
  - Quaker (mentor, friend, colleague, traveling companion)
  - Organizational (member, founder, clerk)
  - Historical (converted by, imprisoned with, corresponded with)
  - Location (born in, died in, ministered in)

#### **Relationship Documentation**
- Record relationship start/end dates (if known)
- Note relationship descriptions from sources
- Document source URLs for each relationship
- Create relationship matrix spreadsheet

### **Phase 4: Quality Assurance and Verification**

#### **Completeness Checks**
- Verify all known members included
- Check core biographical data collected
- Ensure relationships documented where known
- Explicitly note missing information

#### **Accuracy Verification**
- Cross-reference information across multiple sources
- Flag discrepancies between sources
- Prefer official Quaker sites over Wikipedia when in conflict
- Document uncertainty levels

#### **Provenance Documentation**
- Every data point must have source URL
- Source type must be documented
- Date of access recorded
- Citation information preserved

---

## Graph Building Strategy

### **Technology Stack**

#### **Open Source Tools**
- **NetworkX (Python):** Graph data structure and manipulation
- **GraphML:** XML-based graph format for data storage
- **Graphviz:** Graph visualization (DOT format generation)
- **Python Libraries:**
  - `networkx` for graph operations
  - `xml.etree.ElementTree` or `lxml` for GraphML parsing
  - `graphviz` Python package for DOT file generation

### **Data Structure Design**

#### **GraphML Format**
- **Nodes:** Represent people, places, events, organizations, writings
- **Edges:** Represent relationships between nodes
- **Attributes:** Store all collected data as node/edge attributes
- **Metadata:** Graph-level metadata for Graphviz rendering

#### **Node Types**
1. **Person Nodes:**
   - Central figures (George Fox, Margaret Fell)
   - Valiant Sixty members
   - Family members
   - Contemporaries (Quaker and non-Quaker)

2. **Place Nodes:**
   - Meeting houses
   - Towns and regions
   - Birth/death locations

3. **Event Nodes:**
   - Imprisonments
   - Ministry journeys
   - Key historical events
   - Conversions

4. **Organization Nodes:**
   - Meetings
   - Yearly Meetings
   - Other Quaker organizations

5. **Writing Nodes:**
   - Published works
   - Letters
   - Journals

#### **Edge Types**
- **Family:** father, mother, spouse, sibling, child
- **Quaker:** mentor, friend, colleague, traveling_companion
- **Organizational:** member, founder, clerk, visited
- **Historical:** converted_by, imprisoned_with, corresponded_with
- **Location:** born_in, died_in, ministered_in, imprisoned_in
- **Event:** participated_in, organized, witnessed

### **Graph Building Workflow**

#### **Step 1: Data Import**
1. Load GraphML file using NetworkX
2. Parse node and edge attributes
3. Validate data structure
4. Check for missing required fields

#### **Step 2: Graph Construction**
1. Create NetworkX directed graph
2. Add all nodes with attributes
3. Add all edges with relationship types
4. Verify graph connectivity
5. Check for isolated nodes

#### **Step 3: Graph Analysis**
1. Calculate basic statistics (nodes, edges, density)
2. Identify central figures (degree centrality)
3. Find communities/clusters
4. Analyze relationship patterns
5. Identify data gaps

#### **Step 4: Graphviz Generation**
1. Read GraphML metadata for Graphviz settings
2. Map node attributes to Graphviz node properties:
   - `fillcolor` from node attribute
   - `penwidth` from node attribute
   - `shape` from node attribute
   - `label` from node attribute
   - `URL` from wikipedia_url or quaker_org_url
3. Map edge attributes to Graphviz edge properties:
   - `label` from relationship_type
   - Style based on relationship type
4. Generate DOT file following existing patterns
5. Apply color scheme and styling from metadata

#### **Step 5: Visualization**
1. Generate PNG using Graphviz: `dot -Tpng input.dot -o output.png`
2. Generate SVG for scalability: `dot -Tsvg input.dot -o output.svg`
3. Create hyperlinked version with Wikipedia/Quaker.org.uk URLs
4. Add legend subgraph explaining color coding
5. Optimize layout and readability

### **Graph Structure Following Existing Patterns**

#### **Color Coding Scheme**
- **Gold:** Central figures (George Fox, Margaret Fell) - penwidth=3
- **Light Pink:** Family members - penwidth=2 (QUAKER), penwidth=1 (non-Quaker)
- **Light Cyan:** Quaker mentors and early leaders - penwidth=2
- **Light Steel Blue:** Valiant Sixty members - penwidth=2
- **Light Coral:** Non-Quaker contemporaries - penwidth=1
- **Light Gray (Diamond):** Places/Organizations - penwidth=2 (QUAKER), penwidth=1 (non-Quaker)
- **Orange (Diamond):** Events - penwidth=2
- **Plum (Diamond):** Writings - penwidth=2

#### **Visual Conventions**
- **Thick borders (penwidth=2-3):** All Quaker individuals and organizations
- **Thin borders (penwidth=1):** Non-Quaker individuals and organizations
- **Box shape:** People
- **Diamond shape:** Places, events, organizations, writings
- **"QUAKER" labels:** Clearly marked on all Quaker connections

#### **Hyperlink Integration**
- All nodes with Wikipedia URLs include `URL="[wikipedia_url]"`
- All nodes with Quaker.org.uk URLs include `URL="[quaker_org_url]"`
- Hyperlinks work in SVG format when opened in web browser

### **Implementation Approach**

#### **Python Script Structure**
```python
# Pseudocode outline
1. Load GraphML file
2. Create NetworkX graph
3. Parse nodes and edges
4. Apply Graphviz styling based on attributes
5. Generate DOT file
6. Render to PNG/SVG
```

#### **Data Flow**
1. **Collection Phase:** Manual data entry → Spreadsheet → GraphML
2. **Processing Phase:** GraphML → NetworkX → Analysis
3. **Visualization Phase:** NetworkX → DOT → Graphviz → PNG/SVG

#### **Quality Checks**
- Verify all nodes have required attributes
- Check edge relationships are valid
- Ensure color coding follows scheme
- Validate hyperlinks are accessible
- Test Graphviz rendering

### **Deliverables**

1. **GraphML File:** Complete graph data with all attributes
2. **NetworkX Analysis:** Python scripts for graph analysis
3. **DOT Files:** Graphviz source files (basic and hyperlinked versions)
4. **Visualizations:** PNG and SVG renderings
5. **Documentation:** README with usage instructions
6. **Source Citations:** Complete provenance documentation

---

## Summary

### **Data Collection Method:**
A systematic, multi-phase approach starting with source identification from Quaker sites and Wikipedia, followed by comprehensive biographical data collection for each member, relationship mapping, and rigorous quality assurance. Every data point includes full provenance documentation.

### **Graph Building Strategy:**
Using open-source tools (NetworkX, GraphML, Graphviz), construct a knowledge graph that follows existing project patterns. The GraphML format stores all data with metadata for Graphviz rendering. The workflow transforms collected data into a NetworkX graph, applies styling based on attributes, generates Graphviz DOT files, and creates visualizations with proper color coding, hyperlinks, and legends.

---

**Document Version:** 1.0  
**Last Updated:** November 28, 2025





