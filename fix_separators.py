#!/usr/bin/env python3
"""
Script to remove <separator/> tags from all view files
as they may not be compatible with Odoo 19
"""

import os
import re
import glob

def fix_separators_in_file(file_path):
    """Remove <separator/> tags from XML files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count separators before removal
        separator_count = len(re.findall(r'\s*<separator\s*/>', content))

        if separator_count > 0:
            # Remove separator tags with surrounding whitespace
            content = re.sub(r'\s*<separator\s*/>\s*\n?', '\n', content)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Fixed {separator_count} separators in: {file_path}")
            return separator_count

        return 0
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def main():
    # Find all XML files in hexapay_modules
    pattern = "hexapay_modules/**/views/*.xml"
    xml_files = glob.glob(pattern, recursive=True)

    total_fixed = 0
    files_fixed = 0

    for xml_file in xml_files:
        fixed_count = fix_separators_in_file(xml_file)
        if fixed_count > 0:
            files_fixed += 1
            total_fixed += fixed_count

    print(f"\nSummary:")
    print(f"Files processed: {len(xml_files)}")
    print(f"Files fixed: {files_fixed}")
    print(f"Total separators removed: {total_fixed}")

if __name__ == "__main__":
    main()
