# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The MASTERY-AI Framework is a comprehensive AI optimization framework for AI Search Optimization (AISO) and AI Agent Integration. The framework consists of 8 strategic pillars containing 148 atomic factors for evaluating and optimizing content for AI systems.

## Repository Structure

```
mastery-ai Framework/
├── Ideation/                     # Core framework documentation and specifications
│   ├── The MASTERY-AI Framework v3.1.1 250703.md    # Main framework document
│   ├── Pillar *.md              # Individual pillar specifications (8 files)
│   ├── Product Requirements Document: AI Mastery Framework Library.md
│   └── schema_v3_1_1_validation.py  # Framework validation script
└── README.md                     # Basic project readme
```

## Development Commands

### Framework Validation
```bash
# Run the framework validation script
python Ideation/schema_v3_1_1_validation.py
```

## Architecture and Framework Structure

### The Eight MASTERY-AI Pillars

The framework is organized into 8 weighted pillars that form the MASTERY acronym:

1. **AI** - AI Response Optimization & Citation (23.8% weight, 23 factors)
   - Core pillar for AI system optimization
   - Includes MCP (Model Context Protocol) integration
   
2. **A** - Authority & Trust Signals (17.9% weight, 15 factors)
   - Credibility and trust indicators for AI systems
   
3. **M** - Machine Readability & Technical Infrastructure (14.6% weight, 21 factors)
   - Technical implementation including LLMs.txt content accessibility
   
4. **S** - Semantic Content Quality (13.9% weight, 22 factors)
   - Content depth, semantic richness, and integrity
   
5. **E** - Engagement & User Experience (10.9% weight, 19 factors)
   - User experience signals for AI validation
   
6. **T** - Topical Expertise & Experience (8.9% weight, 14 factors)
   - Expertise demonstration and topical authority
   
7. **R** - Reference Networks & Citations (5.9% weight, 19 factors)
   - External validation and citation networks
   
8. **Y** - Yield Optimization & Freshness (4.1% weight, 15 factors)
   - Continuous optimization and content freshness

### Key Technical Components

- **Total Atomic Factors**: 148 across all pillars
- **Framework Version**: 3.1.1 (Enhanced Content Accessibility Edition)
- **Scoring System**: 100-point comprehensive scoring methodology
- **Integration Standards**: MCP (Model Context Protocol) and LLMs.txt

### Implementation Phases

The Product Requirements Document outlines a 24-week implementation timeline:
1. **Weeks 1-4**: Foundation and Core Architecture
2. **Weeks 5-12**: Pillar Implementation and Assessment Engine
3. **Weeks 13-18**: Deployment System and Documentation
4. **Weeks 19-24**: Testing, Optimization, and Community Preparation

## Important Implementation Notes

### When Implementing the Framework Library

1. **Modular Architecture**: Each pillar should be implemented as a separate module with clear interfaces
2. **Scoring Methodology**: Maintain mathematical precision in weight calculations (must total exactly 100%)
3. **Schema Validation**: Use the validation script to ensure framework compliance
4. **Documentation Structure**: Follow the modular documentation approach with main framework doc + 8 pillar appendices

### Repository Deployment Structure (from PRD)

When building out the library implementation, follow this structure:
```
ai-mastery-framework/
├── docs/           # Framework documentation
├── src/            # Core library source
├── schema/         # Framework schema and validation
├── deployment/     # Deployment scripts
├── tests/          # Test suite
├── examples/       # Implementation examples
└── tools/          # Development tools
```

### Key Development Priorities

1. **One-Line Installation**: Target < 5 minute deployment time
2. **Cross-Platform Support**: Linux, macOS, Windows compatibility
3. **API-First Design**: RESTful APIs for all assessment capabilities
4. **95%+ Test Coverage**: Comprehensive unit and integration testing
5. **Backward Compatibility**: Maintain compatibility across minor versions

## Framework-Specific Considerations

### MCP Integration
The framework includes comprehensive Model Context Protocol assessment for AI agent ecosystem integration.

### LLMs.txt Implementation
Sub-Pillar M.5 specifically addresses LLMs.txt content accessibility standards - an emerging protocol for AI content discovery.

### Content Integrity
Sub-Pillar S.5 addresses synthetic content validation and provenance tracking, critical for AI-generated content assessment.

## Commercial Context

This framework serves as proprietary intellectual property for:
- AImpactScanner assessment tools
- Automated optimization systems
- Competitive intelligence platforms
- Consulting services
- Training and certification programs

The framework is designed to enable commercial tool development while maintaining academic rigor and comprehensive coverage of AI optimization requirements.