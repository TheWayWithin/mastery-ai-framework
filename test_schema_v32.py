#!/usr/bin/env python3
"""Test script to verify MASTERY-AI Framework v3.2 schema updates"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mastery_ai.core.schema import FrameworkSchema
from mastery_ai import __version__ as lib_version
from mastery_ai import __framework_version__, __framework_edition__

def test_schema_v32():
    """Test that schema v3.2 is correctly configured"""
    
    print("=" * 60)
    print("MASTERY-AI Framework v3.2 Schema Test")
    print("=" * 60)
    
    # Test version information
    print("\n📦 Version Information:")
    print(f"  Library Version: {lib_version.__version__}")
    print(f"  Framework Version: {__framework_version__}")
    print(f"  Framework Edition: {__framework_edition__}")
    
    # Create default schema
    schema = FrameworkSchema.get_default_schema()
    
    # Test framework metadata
    print("\n🏷️ Framework Metadata:")
    print(f"  Schema Version: {schema.version}")
    print(f"  Schema Edition: {schema.edition}")
    print(f"  Total Factors: {schema.total_factors}")
    
    # Test pillar weights
    print("\n⚖️ Pillar Weights:")
    total_weight = 0
    expected_weights = {
        'AI': 23.7, 'A': 17.8, 'M': 15.0, 'S': 13.8,
        'E': 10.9, 'T': 8.9, 'R': 5.9, 'Y': 4.0
    }
    
    for pillar_type, pillar in schema.pillars.items():
        expected = expected_weights[pillar_type.value]
        match = "✅" if abs(pillar.weight - expected) < 0.01 else "❌"
        print(f"  {pillar_type.value}: {pillar.weight}% (expected {expected}%) {match}")
        total_weight += pillar.weight
    
    print(f"\n  Total Weight: {total_weight}% {'✅' if abs(total_weight - 100.0) < 0.01 else '❌'}")
    
    # Test factor counts
    print("\n📊 Factor Counts:")
    total_factors = 0
    expected_counts = {
        'AI': 23, 'A': 15, 'M': 22, 'S': 22,
        'E': 19, 'T': 14, 'R': 19, 'Y': 15
    }
    
    for pillar_type, pillar in schema.pillars.items():
        expected = expected_counts[pillar_type.value]
        match = "✅" if pillar.factor_count == expected else "❌"
        note = " (+1 for AI Bot Access)" if pillar_type.value == 'M' else ""
        print(f"  {pillar_type.value}: {pillar.factor_count} factors (expected {expected}) {match}{note}")
        total_factors += pillar.factor_count
    
    print(f"\n  Total Factors: {total_factors} {'✅' if total_factors == 149 else '❌'}")
    
    # Validate mathematical precision
    print("\n🔬 Mathematical Validation:")
    validation_results = schema.validate_mathematical_precision()
    print(f"  Valid: {validation_results['valid']} {'✅' if validation_results['valid'] else '❌'}")
    print(f"  Pillar Weight Sum: {validation_results['pillar_weight_sum']}%")
    print(f"  Total Factor Count: {validation_results['total_factors']}")
    
    if validation_results['errors']:
        print("  ⚠️ Errors:")
        for error in validation_results['errors']:
            print(f"    - {error}")
    
    # Summary
    print("\n" + "=" * 60)
    all_pass = (
        schema.version == "3.2.0" and
        schema.edition == "AI Bot Access Control Edition" and
        schema.total_factors == 149 and
        abs(total_weight - 100.0) < 0.01 and
        total_factors == 149 and
        validation_results['valid']
    )
    
    if all_pass:
        print("✅ SUCCESS: All v3.2 schema tests passed!")
        print("The schema correctly reflects:")
        print("  - Version 3.2.0")
        print("  - AI Bot Access Control Edition")
        print("  - 149 total factors (+1 from v3.1.1)")
        print("  - M pillar weight increased to 15.0%")
        print("  - Perfect mathematical precision")
    else:
        print("❌ FAILURE: Some tests failed. Please review the output above.")
    
    print("=" * 60)
    
    return all_pass

if __name__ == "__main__":
    success = test_schema_v32()
    sys.exit(0 if success else 1)