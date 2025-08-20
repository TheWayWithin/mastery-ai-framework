#!/usr/bin/env python3
"""
MASTERY-AI Framework Quick Start Example
Demonstrates basic usage of the assessment engine
"""

from mastery_ai import AssessmentEngine, Config
from mastery_ai.core.assessment_engine import AssessmentInput
from mastery_ai.core.schema import PillarType


def main():
    """Run a basic assessment example"""
    
    print("=" * 60)
    print("MASTERY-AI Framework - Quick Start Example")
    print("=" * 60)
    
    # Initialize the assessment engine with default config
    print("\n1. Initializing Assessment Engine...")
    engine = AssessmentEngine()
    print("   ✓ Engine initialized with default configuration")
    
    # Create sample input data
    print("\n2. Creating sample input data...")
    input_data = AssessmentInput(
        url="https://example.com",
        content={
            "title": "Example AI-Optimized Content",
            "body": "This is sample content optimized for AI systems.",
            "keywords": ["AI", "optimization", "assessment"],
            "depth_analysis": {"comprehensive": True, "detailed": True},
            "verification_status": "verified",
            "sources": ["Source 1", "Source 2"],
        },
        technical_data={
            "mcp_status": "implemented",
            "api_status": "available",
            "structured_data": True,
        },
        metadata={
            "author": "Example Author",
            "published_date": "2024-01-01",
            "last_updated": "2024-08-01",
        }
    )
    print("   ✓ Sample data created")
    
    # Validate input data
    print("\n3. Validating input data...")
    validation = engine.validate_input(input_data)
    print(f"   ✓ Data valid: {validation['valid']}")
    print(f"   ✓ Data completeness: {validation['data_completeness']:.1%}")
    
    # Run the assessment
    print("\n4. Running comprehensive assessment...")
    result = engine.assess(input_data)
    print("   ✓ Assessment complete")
    
    # Display overall results
    print("\n" + "=" * 60)
    print("ASSESSMENT RESULTS")
    print("=" * 60)
    
    print(f"\n📊 Overall Score: {result.overall_score:.1f}/100")
    
    # Get score interpretation
    from mastery_ai.core.scoring import ScoringEngine
    scoring = ScoringEngine(engine.schema)
    rating, description = scoring.get_score_interpretation(result.overall_score)
    print(f"   Rating: {rating}")
    print(f"   {description}")
    
    # Display pillar scores
    print("\n📈 Pillar Scores (by weight):")
    print("-" * 40)
    
    # Sort pillars by weight
    pillars_by_weight = sorted(
        [(p, engine.schema.pillars[p]) for p in PillarType],
        key=lambda x: x[1].weight,
        reverse=True
    )
    
    for pillar_type, pillar_info in pillars_by_weight:
        score = result.pillar_scores.get(pillar_type, 0.0)
        print(f"{pillar_info.name:45} ({pillar_info.weight:4.1f}%): {score:5.1f}/100")
    
    # Display top recommendations
    print("\n💡 Top Recommendations:")
    print("-" * 40)
    for i, rec in enumerate(result.recommendations[:5], 1):
        print(f"{i}. {rec}")
    
    # Calculate improvement potential
    print("\n📊 Improvement Potential (by impact):")
    print("-" * 40)
    improvement = scoring.calculate_improvement_potential(result.pillar_scores)
    sorted_improvement = sorted(improvement.items(), key=lambda x: x[1], reverse=True)
    
    for pillar_type, potential in sorted_improvement[:3]:
        pillar_name = engine.schema.pillars[pillar_type].name
        print(f"{pillar_name}: +{potential:.1f} points potential impact")
    
    # Generate and save report
    print("\n5. Generating reports...")
    
    # Generate markdown report
    markdown_report = engine.generate_report(result, format="markdown")
    with open("assessment_report.md", "w") as f:
        f.write(markdown_report)
    print("   ✓ Markdown report saved to assessment_report.md")
    
    # Save JSON results
    from pathlib import Path
    engine.save_result(result, Path("assessment_results.json"))
    print("   ✓ JSON results saved to assessment_results.json")
    
    print("\n" + "=" * 60)
    print("Assessment complete! Check the generated reports for details.")
    print("=" * 60)


if __name__ == "__main__":
    main()