# MASTERY-AI Framework

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Framework Version](https://img.shields.io/badge/framework-v3.2-green)](https://github.com/TheWayWithin/mastery-ai-framework)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A comprehensive AI optimization assessment framework with 149 atomic factors across 8 strategic pillars, including critical AI bot access configuration. The MASTERY-AI Framework provides organizations with production-ready tools to assess, optimize, and improve their content and infrastructure for AI system discovery and performance.

## 🚀 Quick Start

### One-Line Installation

```bash
# Install via pip
pip install mastery-ai

# Or clone and install from source
git clone https://github.com/TheWayWithin/mastery-ai-framework.git
cd mastery-ai-framework
pip install -e .
```

### Basic Usage

```python
from mastery_ai import AssessmentEngine, AssessmentInput

# Initialize the assessment engine
engine = AssessmentEngine()

# Create input data
input_data = AssessmentInput(
    url="https://example.com",
    content={"title": "Example Content", "body": "..."},
    technical_data={"mcp_status": "implemented"}
)

# Run assessment
result = engine.assess(input_data)

# Display results
print(f"Overall Score: {result.overall_score:.1f}/100")
for pillar, score in result.pillar_scores.items():
    print(f"{pillar}: {score:.1f}/100")
```

## 📊 The MASTERY Framework

The framework consists of 8 weighted pillars forming the MASTERY acronym:

| Pillar | Name | Weight | Factors | Focus |
|--------|------|--------|---------|-------|
| **AI** | AI Response Optimization & Citation | 23.7% | 23 | Core AI system optimization, MCP integration |
| **A** | Authority & Trust Signals | 17.8% | 15 | Credibility and trust indicators |
| **M** | Machine Readability & Technical Infrastructure | 15.0% | 22 | Technical implementation, LLMs.txt, robots.txt |
| **S** | Semantic Content Quality | 13.8% | 22 | Content depth and semantic richness |
| **E** | Engagement & User Experience | 10.9% | 19 | User experience signals |
| **T** | Topical Expertise & Experience | 8.9% | 14 | Expertise demonstration |
| **R** | Reference Networks & Citations | 5.9% | 19 | External validation |
| **Y** | Yield Optimization & Freshness | 4.0% | 15 | Continuous optimization |

**Total**: 149 atomic factors | 100% combined weight

## 🏗️ Architecture

```
mastery_ai/
├── core/                 # Core assessment engine
│   ├── assessment_engine.py
│   ├── config.py
│   ├── schema.py
│   └── scoring.py
├── pillars/             # Individual pillar implementations
│   ├── ai_response.py   # AI optimization (23.7%)
│   ├── authority.py     # Authority signals (17.8%)
│   └── ...             # Other pillars
├── reporting/           # Report generation
└── api/                # RESTful API
```

## 💡 Features

### Core Capabilities
- ✅ **Comprehensive Assessment**: All 149 atomic factors evaluated
- ✅ **AI Bot Access Control**: Robots.txt configuration assessment
- ✅ **Weighted Scoring**: Mathematically precise scoring (weights = 100%)
- ✅ **Modular Architecture**: Use complete framework or individual pillars
- ✅ **RESTful API**: Full API access to all capabilities
- ✅ **Custom Configuration**: Flexible weighting and parameters

### Technical Specifications
- **Assessment Time**: <30 seconds typical
- **Memory Usage**: <512MB runtime
- **Installation Time**: <5 minutes
- **Test Coverage**: 95%+ target
- **Platform Support**: Linux, macOS, Windows

## 🔧 Advanced Usage

### Custom Configuration

```python
from mastery_ai import Config, AssessmentEngine

# Create custom configuration
config = Config()
config.scoring.custom_weights = {
    "AI": 30.0,  # Increase AI pillar weight
    "A": 20.0,
    "M": 15.0,
    "S": 15.0,
    "E": 8.0,
    "T": 6.0,
    "R": 4.0,
    "Y": 2.0
}

# Use custom config
engine = AssessmentEngine(config)
```

### Pillar-Specific Assessment

```python
from mastery_ai import AssessmentEngine, PillarType

engine = AssessmentEngine()

# Assess only AI Response pillar
ai_result = engine.assess_pillar(PillarType.AI, input_data)
print(f"AI Pillar Score: {ai_result['score']:.1f}/100")
```

### Generate Reports

```python
# Generate different report formats
json_report = engine.generate_report(result, format="json")
html_report = engine.generate_report(result, format="html")
markdown_report = engine.generate_report(result, format="markdown")

# Save results
engine.save_result(result, Path("assessment_results.json"))
```

## 🌐 API Usage

### Start API Server

```bash
# Start the API server
mastery-ai serve --host 0.0.0.0 --port 8000

# Or with Docker
docker run -p 8000:8000 mastery-ai/framework
```

### API Example

```bash
# Run assessment via API
curl -X POST http://localhost:8000/assess \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

## 📈 Framework Version History

- **v3.2.0** (Current): AI Bot Access Control Edition
  - Added AI Bot Access Configuration (M.5.3)
  - Robots.txt allowlisting for OAI-SearchBot and GPTBot
  - 149 total factors (+1 for bot access control)
  - Rebalanced weights for enhanced Machine Readability

- **v3.1.1**: Enhanced Content Accessibility Edition
  - Added LLMs.txt support (M.5 sub-pillar)
  - 148 total factors (+2 for content accessibility)
  - MCP protocol integration

- **v3.1.0**: Model Context Protocol Update
- **v3.0.0**: Major framework revision
- **v2.1.0**: Extended factor set
- **v2.0.0**: Initial public release

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=mastery_ai --cov-report=html

# Run specific test suite
pytest tests/test_pillars/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone repository
git clone https://github.com/TheWayWithin/mastery-ai-framework.git
cd mastery-ai-framework

# Install development dependencies
pip install -r requirements-dev.txt

# Install in development mode
pip install -e .

# Run tests
pytest
```

## 📚 Documentation

- [Full Documentation](https://github.com/TheWayWithin/mastery-ai-framework/wiki)
- [API Reference](docs/api/README.md)
- [Implementation Guides](docs/guides/README.md)
- [Framework Specification](docs/framework/README.md)

## 🏢 Use Cases

- **Enterprise SEO**: Optimize content for AI discovery
- **Content Strategy**: Improve AI system responses
- **Technical Audits**: Assess AI readiness
- **Competitive Analysis**: Benchmark against competitors
- **Consulting Services**: AI optimization assessments

## 📊 Success Metrics

Target metrics for production deployments:

- Installation success rate: >95%
- Deployment time: <5 minutes
- Assessment execution: <30 seconds
- Memory usage: <512MB
- Test coverage: >95%
- User satisfaction: >4.5/5

## 🔒 Security

- Encrypted data transmission
- Configurable access controls
- Audit logging
- GDPR compliant
- No data retention by default

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Based on the MASTERY-AI Framework v3.2 specification
- Inspired by agent-11 repository patterns
- Community contributors and testers

## 📧 Contact

- GitHub: [https://github.com/TheWayWithin/mastery-ai-framework](https://github.com/TheWayWithin/mastery-ai-framework)
- Issues: [GitHub Issues](https://github.com/TheWayWithin/mastery-ai-framework/issues)

---

**MASTERY-AI Framework** - Comprehensive AI Optimization Assessment
*Transform your content and infrastructure for optimal AI system performance*