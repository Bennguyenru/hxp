#!/usr/bin/env python3
"""
Script to fix search view group-by filters across all modules
to ensure Odoo 19 compatibility
"""

import os
import re
import glob

def fix_group_by_filters(file_path):
    """Fix group-by filters in search views to include domain attribute"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match group-by filters without domain attribute
        # <filter string="..." name="group_..." context="{'group_by': '...'}"
        pattern = r'(<filter\s+string="[^"]+"\s+name="group_[^"]+"\s+)context="(\{\'group_by\':[^}]+\})"([^>]*>)'

        # Replace with version that includes domain="[]"
        def replace_func(match):
            prefix = match.group(1)
            context = match.group(2)
            suffix = match.group(3)
            return f'{prefix}domain="[]" context="{context}"{suffix}'

        new_content = re.sub(pattern, replace_func, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            changes = len(re.findall(pattern, content))
            print(f"Fixed {changes} group-by filters in: {file_path}")
            return changes

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
        fixed_count = fix_group_by_filters(xml_file)
        if fixed_count > 0:
            files_fixed += 1
            total_fixed += fixed_count

    print(f"\nSummary:")
    print(f"Files processed: {len(xml_files)}")
    print(f"Files fixed: {files_fixed}")
    print(f"Total group-by filters fixed: {total_fixed}")

if __name__ == "__main__":
    main()
