#!/usr/bin/env python3
"""
Example script showing how to generate QR codes for the Quaker Scientists project
"""

from qr_code_generator import generate_basic_qr, generate_styled_qr, generate_multiple_qrs

def main():
    print("Generating QR codes for Quaker Scientists project...")
    
    # Create a directory for QR codes
    import os
    qr_dir = "qr_codes"
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)
    
    # QR codes for the main scientists
    scientists_data = [
        "https://en.wikipedia.org/wiki/John_Dalton",
        "https://en.wikipedia.org/wiki/Kathleen_Lonsdale", 
        "https://en.wikipedia.org/wiki/William_Allen_(English_Quaker)"
    ]
    
    print("Generating QR codes for scientist Wikipedia pages...")
    scientist_files = generate_multiple_qrs(
        scientists_data, 
        prefix=f"{qr_dir}/scientist",
        size=15
    )
    
    # QR code for the project repository
    repo_url = "https://github.com/your-username/quaker_scientists"  # Replace with actual repo
    generate_basic_qr(
        repo_url, 
        f"{qr_dir}/project_repo.png",
        size=12
    )
    
    # QR code for a specific knowledge graph
    graph_url = "https://example.com/john_dalton_knowledge_graph"  # Replace with actual URL
    generate_styled_qr(
        graph_url,
        f"{qr_dir}/dalton_graph_styled.png",
        size=12
    )
    
    # QR code with contact information
    contact_info = """BEGIN:VCARD
VERSION:3.0
FN:Quaker Scientists Project
ORG:Historical Research
EMAIL:contact@example.com
URL:https://quaker-scientists.example.com
NOTE:Research project on Quaker scientists and their networks
END:VCARD"""
    
    generate_basic_qr(
        contact_info,
        f"{qr_dir}/contact_vcard.png",
        size=10
    )
    
    print(f"\nAll QR codes generated in '{qr_dir}' directory:")
    for file in os.listdir(qr_dir):
        if file.endswith('.png'):
            print(f"  - {file}")

if __name__ == "__main__":
    main()


