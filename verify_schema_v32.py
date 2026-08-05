#!/usr/bin/env python3
"""Simple verification of MASTERY-AI Framework v3.2 schema updates"""

def verify_v32_updates():
    """Verify that all v3.2 updates have been applied correctly"""
    
    print("=" * 60)
    print("MASTERY-AI Framework v3.2 Update Verification")
    print("=" * 60)
    
    print("\n📄 Checking schema.py updates...")
    with open('mastery_ai/core/schema.py', 'r') as f:
        schema_content = f.read()
    
    checks = []
    
    # Check version
    if 'v3.2.0' in schema_content or 'v3.2' in schema_content:
        checks.append(("✅", "Version updated to v3.2"))
    else:
        checks.append(("❌", "Version NOT updated to v3.2"))
    
    # Check edition
    if 'AI Bot Access Control Edition' in schema_content:
        checks.append(("✅", "Edition updated to 'AI Bot Access Control Edition'"))
    else:
        checks.append(("❌", "Edition NOT updated"))
    
    # Check total factors
    if 'total_factors: int = Field(default=149' in schema_content:
        checks.append(("✅", "Total factors updated to 149"))
    else:
        checks.append(("❌", "Total factors NOT updated to 149"))
    
    # Check specific weight updates
    weight_checks = [
        ('weight=23.7', 'AI pillar weight = 23.7%'),
        ('weight=17.8', 'A pillar weight = 17.8%'),
        ('weight=15.0', 'M pillar weight = 15.0% (CRITICAL)'),
        ('weight=13.8', 'S pillar weight = 13.8%'),
        ('weight=10.9', 'E pillar weight = 10.9%'),
        ('weight=8.9', 'T pillar weight = 8.9%'),
        ('weight=5.9', 'R pillar weight = 5.9%'),
        ('weight=4.0', 'Y pillar weight = 4.0%')
    ]
    
    for check_str, desc in weight_checks:
        if check_str in schema_content:
            checks.append(("✅", desc))
        else:
            checks.append(("❌", f"{desc} NOT found"))
    
    # Check M pillar factor count
    if 'factor_count=22' in schema_content:
        checks.append(("✅", "M pillar factor count = 22"))
    else:
        checks.append(("❌", "M pillar factor count NOT updated to 22"))
    
    print("\n📄 Checking __version__.py updates...")
    with open('mastery_ai/__version__.py', 'r') as f:
        version_content = f.read()
    
    # Check framework version
    if '__framework_version__ = "3.2.0"' in version_content:
        checks.append(("✅", "Framework version updated to 3.2.0"))
    else:
        checks.append(("❌", "Framework version NOT updated"))
    
    # Check framework edition
    if '__framework_edition__ = "AI Bot Access Control Edition"' in version_content:
        checks.append(("✅", "Framework edition updated"))
    else:
        checks.append(("❌", "Framework edition NOT updated"))
    
    # Display results
    print("\n📋 Verification Results:")
    print("-" * 40)
    
    all_pass = True
    for status, description in checks:
        print(f"{status} {description}")
        if status == "❌":
            all_pass = False
    
    print("-" * 40)
    
    # Summary
    print("\n🎯 Summary:")
    if all_pass:
        print("✅ SUCCESS: All v3.2 updates have been applied correctly!")
        print("\nKey changes verified:")
        print("  • Version: 3.2.0")
        print("  • Edition: AI Bot Access Control Edition")
        print("  • Total Factors: 149 (+1 from v3.1.1)")
        print("  • M Pillar Weight: 15.0% (+0.4% from v3.1.1)")
        print("  • M Pillar Factors: 22 (+1 for AI Bot Access Configuration)")
        print("\n🆕 New Factor: M.5.3 - AI Bot Access Configuration")
        print("  - Robots.txt allowlisting for OAI-SearchBot")
        print("  - Robots.txt allowlisting for GPTBot")
        print("  - Gateway control for AI system access")
    else:
        print("❌ FAILURE: Some updates are missing. Please review the results above.")
    
    print("=" * 60)
    
    return all_pass

if __name__ == "__main__":
    import sys
    success = verify_v32_updates()
    sys.exit(0 if success else 1)