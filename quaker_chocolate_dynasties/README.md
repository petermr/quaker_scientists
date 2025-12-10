# Quaker Chocolate Dynasties Knowledge Graph

**Date:** December 10, 2025  
**Project:** Knowledge Graph for Quaker Chocolate Dynasties (Cadbury, Rowntree, Fry families)

---

## Overview

This knowledge graph visualizes the three major Quaker chocolate dynasties: the Cadbury, Rowntree, and Fry families. It covers their businesses, family relationships, contacts/networks, and philanthropic work, with a total of 50 key entries organized into four phases.

---

## Four Phases

### Phase 1: Businesses (12 entries)
- Cadbury Brothers Ltd. (founded 1824)
- Bournville Factory (established 1879)
- Bournville Village (established 1893)
- J.S. Fry & Sons (founded 1759)
- Rowntree & Co. (founded 1862)
- Rowntree's Cocoa Works
- New Earswick Village (established 1901)
- Cadbury Dairy Milk (introduced 1905)
- Kit Kat (introduced 1935)
- First Solid Chocolate Bar (1847)
- Cadbury Schweppes (merger 1969)
- Fry's Chocolate Cream (introduced 1866)

### Phase 2: Families (18 entries)

**Cadbury Family (7 entries):**
- John Cadbury (1801-1889) - Founder
- Richard Cadbury (1835-1899) - Businessman
- George Cadbury (1839-1922) - Businessman & Philanthropist
- Edward Cadbury (1873-1948) - Businessman
- Laurence Cadbury (1889-1982) - Businessman
- Barrow Cadbury (1868-1958) - Philanthropist
- Dominic Cadbury (b. 1938) - Businessman

**Rowntree Family (6 entries):**
- Henry Isaac Rowntree (1838-1883) - Founder
- Joseph Rowntree (1836-1925) - Founder & Philanthropist
- Seebohm Rowntree (1871-1954) - Social Reformer
- Arnold Rowntree (1872-1951) - Businessman
- John Wilhelm Rowntree (1868-1905) - Quaker Minister

**Fry Family (5 entries):**
- Joseph Fry (1728-1787) - Founder
- Joseph Storrs Fry II (1826-1913) - Businessman
- Elizabeth Fry (1780-1845) - Prison Reformer
- Francis Fry (1803-1886) - Businessman
- Joseph Fry III (1795-1875) - Businessman

### Phase 3: Contacts (10 entries)
- Barclay Family (Quaker Bankers)
- Gurney Family (Quaker Bankers)
- Seebohm Family (Quaker Family)
- Tuke Family (Quaker Reformers)
- Quaker Business Network
- Adult School Movement
- Quaker Meeting Houses
- William Allen (1770-1843) - Quaker Scientist
- George Fox (1624-1691) - Quaker Founder
- Quaker Industrial Welfare Movement

### Phase 4: Philanthropic Work (10 entries)
- Bournville Village Trust (established 1900)
- Cadbury Pension Scheme
- Cadbury Medical Services
- Cadbury Educational Programs
- Joseph Rowntree Foundation (established 1904)
- Joseph Rowntree Charitable Trust
- Joseph Rowntree Reform Trust
- Seebohm Rowntree Poverty Studies (1901)
- Elizabeth Fry Prison Reform
- Quaker Social Reform Movement

---

## Color Coding Scheme

Following the project style guide:

- **Gold (penwidth=3):** Central figures - Founders (John Cadbury, Joseph Rowntree, Henry Isaac Rowntree, Joseph Fry)
- **Light Pink (penwidth=2):** Family members (all Quaker)
- **Light Cyan (penwidth=2):** Quaker contacts and associates
- **Light Gray (penwidth=2, diamond):** Businesses, factories, organizations (all Quaker)
- **Orange (penwidth=2, diamond):** Product innovations and key events
- **Plum (penwidth=2, diamond):** Philanthropic organizations and trusts

---

## Key Relationships

### Family Relationships
- **Cadbury:** John Cadbury → Richard & George → Edward, Laurence, Barrow → Dominic
- **Rowntree:** Henry Isaac & Joseph Rowntree (brothers) → Seebohm, Arnold, John Wilhelm
- **Fry:** Joseph Fry → Joseph Storrs Fry II → Francis Fry, Joseph Fry III

### Business Relationships
- **Cadbury:** Founded Cadbury Brothers Ltd., built Bournville Factory and Village
- **Rowntree:** Founded Rowntree & Co., built New Earswick Village
- **Fry:** Founded J.S. Fry & Sons, produced first solid chocolate bar

### Philanthropic Relationships
- **Cadbury:** Established Bournville Village Trust, pension schemes, medical services
- **Rowntree:** Established Joseph Rowntree Foundation and trusts, poverty research
- **Fry:** Elizabeth Fry's prison reform work

### Contact Relationships
- Inter-family marriages: Fry-Barclay, Fry-Gurney, Rowntree-Seebohm, Rowntree-Tuke
- Quaker business network connections
- Support for Adult School Movement and Quaker Industrial Welfare

---

## Files

- `quaker_chocolate_dynasties.dot` - Graphviz DOT source file
- `quaker_chocolate_dynasties.svg` - SVG visualization (with clickable hyperlinks)
- `quaker_chocolate_dynasties.png` - PNG visualization
- `README.md` - This documentation file

---

## How to Use

### Viewing the Graphs

1. **SVG Format (Recommended):**
   - Open `quaker_chocolate_dynasties.svg` in a web browser
   - Click on any node to visit its Wikipedia page
   - Best for interactive exploration

2. **PNG Format:**
   - Open `quaker_chocolate_dynasties.png` in any image viewer
   - Good for printing or embedding in documents

### Regenerating the Graphs

If you modify the DOT file, regenerate the visualizations:

```bash
# Generate SVG
dot -Tsvg quaker_chocolate_dynasties.dot -o quaker_chocolate_dynasties.svg

# Generate PNG
dot -Tpng quaker_chocolate_dynasties.dot -o quaker_chocolate_dynasties.png
```

---

## Data Sources

All information sourced from:
- **Wikipedia:** Individual biographical pages, company histories, foundation pages
- **Quaker.org.uk:** Historical information and Quaker resources
- **Official Websites:** Joseph Rowntree Foundation, Bournville Village Trust

**Date Accessed:** December 10, 2025

---

## Key Features

1. **50 Total Entries:** Organized into 4 phases (Businesses, Families, Contacts, Philanthropy)
2. **Hyperlinks:** All nodes link to Wikipedia pages for detailed information
3. **Quaker Emphasis:** All Quaker entities marked with thick borders and "QUAKER" labels
4. **Color Coding:** Visual distinction between founders, family, businesses, and philanthropy
5. **Relationship Mapping:** Clear visualization of family, business, and philanthropic connections

---

## Historical Context

The three Quaker chocolate dynasties (Cadbury, Rowntree, Fry) represent a unique intersection of business success and Quaker values. They pioneered:

- **Ethical Business Practices:** Fair wages, worker welfare, quality products
- **Model Villages:** Bournville and New Earswick as examples of worker housing
- **Philanthropic Foundations:** Long-lasting trusts supporting social research and reform
- **Social Reform:** Prison reform, poverty research, adult education

Their legacy continues through:
- Joseph Rowntree Foundation (still active in social research)
- Bournville Village Trust (still managing Bournville)
- Various Rowntree trusts (still supporting social causes)

---

## Related Knowledge Graphs

This project follows the same style guide as:
- John Dalton Knowledge Graph
- Kathleen Lonsdale Knowledge Graph
- William Allen Knowledge Graph
- Valiant Sixty Knowledge Graph

---

## Notes

- All individuals and organizations in this graph are Quaker (except where noted)
- Dates are based on Wikipedia and reliable historical sources
- Some relationships (especially inter-family marriages) are simplified for clarity
- The graph focuses on the most significant figures and organizations

---

**Last Updated:** December 10, 2025  
**Status:** Complete - 50 entries across 4 phases

