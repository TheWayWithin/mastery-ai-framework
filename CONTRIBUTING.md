# Contributing to MASTERY-AI Framework

Thank you for your interest in contributing to the MASTERY-AI Framework! This document provides guidelines for contributing to this comprehensive AI optimization assessment framework.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Testing Guidelines](#testing-guidelines)
- [Code Style](#code-style)
- [Framework Architecture](#framework-architecture)
- [Submitting Changes](#submitting-changes)
- [Issue Guidelines](#issue-guidelines)
- [Feature Requests](#feature-requests)
- [Documentation](#documentation)
- [Community](#community)

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a branch for your changes
5. Make your changes and test them
6. Submit a pull request

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug Fixes**: Fix issues in existing functionality
- **Feature Enhancements**: Improve existing features
- **New Features**: Add new capabilities to the framework
- **Documentation**: Improve or add documentation
- **Tests**: Add or improve test coverage
- **Performance**: Optimize existing code
- **Framework Factors**: Propose new assessment factors or modify existing ones

### Framework-Specific Contributions

The MASTERY-AI Framework has specific architecture requirements:

- **Pillar Modifications**: Changes to the 8 pillars (AI, A, M, S, T, E, R, Y) must maintain the 148 total atomic factors
- **Weight Adjustments**: Pillar weights must always total exactly 100%
- **Factor Additions**: New factors require comprehensive documentation and validation
- **Scoring Changes**: Mathematical precision is critical for assessment consistency

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip or conda
- Virtual environment tool (venv, conda, poetry)

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/TheWayWithin/mastery-ai-framework.git
cd mastery-ai-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .

# Verify installation
python -c "import mastery_ai; print(mastery_ai.__version__)"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mastery_ai --cov-report=html

# Run specific test categories
pytest tests/test_pillars/
pytest tests/test_core/
pytest tests/test_api/

# Run performance tests
pytest tests/test_performance/
```

## Testing Guidelines

### Test Requirements

- All new features must include comprehensive tests
- Bug fixes must include regression tests
- Test coverage must remain above 95%
- Performance tests for assessment timing (<30 seconds)
- Integration tests for API endpoints

### Test Structure

```python
def test_feature_name():
    """Test description following docstring conventions."""
    # Arrange
    input_data = create_test_input()
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result.score >= 0.0
    assert result.score <= 100.0
    assert len(result.factors) == expected_count
```

### Framework Validation Tests

All changes must pass the framework validation script:

```bash
python Ideation/schema_v3_1_1_validation.py
```

## Code Style

### Python Style Guidelines

We follow PEP 8 with these specific requirements:

- Line length: 88 characters (Black formatter)
- Use type hints for all public functions
- Docstrings for all modules, classes, and public functions
- Import sorting with isort

### Code Formatting

```bash
# Format code
black mastery_ai/
isort mastery_ai/

# Check linting
flake8 mastery_ai/
mypy mastery_ai/
```

### Documentation Style

- Use Google-style docstrings
- Include examples in docstrings
- Update README.md for significant changes
- Maintain API documentation

## Framework Architecture

### Core Components

1. **Assessment Engine** (`mastery_ai/core/`): Main assessment logic
2. **Pillars** (`mastery_ai/pillars/`): Individual pillar implementations
3. **Factors** (`mastery_ai/factors/`): Atomic assessment factors
4. **API** (`mastery_ai/api/`): RESTful API interface
5. **Reporting** (`mastery_ai/reporting/`): Result generation and formatting

### Architecture Principles

- **Modular Design**: Each pillar is independently testable
- **Mathematical Precision**: Scoring must be mathematically accurate
- **Performance**: Assessments complete in <30 seconds
- **Extensibility**: New factors can be added without breaking changes
- **API-First**: All functionality available via REST API

### Adding New Assessment Factors

1. Define the factor in the appropriate pillar module
2. Add factor weighting (must sum to pillar total)
3. Implement assessment logic
4. Add comprehensive tests
5. Update documentation
6. Validate with framework schema

## Submitting Changes

### Pull Request Process

1. **Branch Naming**: Use descriptive names
   - Features: `feature/description`
   - Bugs: `fix/description`
   - Docs: `docs/description`

2. **Commit Messages**: Follow conventional commit format
   ```
   type(scope): description
   
   - feat: new feature
   - fix: bug fix
   - docs: documentation
   - test: testing
   - refactor: code refactoring
   - perf: performance improvement
   ```

3. **Pull Request Template**: Fill out all sections
4. **Review Process**: At least one maintainer approval required
5. **CI/CD**: All checks must pass

### Before Submitting

- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Framework validation passes
- [ ] Performance benchmarks met
- [ ] Security considerations addressed

## Issue Guidelines

### Bug Reports

Use the bug report template and include:

- Framework version
- Python version
- Operating system
- Minimal reproduction case
- Expected vs actual behavior
- Error messages and stack traces

### Framework Issues

For framework-specific issues, include:

- Which pillar(s) affected
- Assessment input data (anonymized)
- Scoring discrepancies
- Performance measurements

## Feature Requests

Use the feature request template and include:

- Clear use case description
- Proposed implementation approach
- Impact on existing functionality
- Framework factor implications
- Performance considerations

### Framework Enhancements

For framework enhancements, consider:

- Impact on the 148 atomic factors
- Weight distribution changes
- Backward compatibility
- Documentation requirements

## Documentation

### Types of Documentation

- **API Documentation**: Auto-generated from docstrings
- **User Guides**: Step-by-step implementation guides
- **Framework Specification**: Technical framework details
- **Examples**: Working code examples

### Documentation Standards

- Clear, concise language
- Working code examples
- Screenshots where helpful
- Version-specific information
- Cross-references to related topics

## Community

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code review and collaboration

### Getting Help

1. Check existing documentation
2. Search GitHub issues
3. Create a new issue with detailed information
4. Join community discussions

### Recognition

Contributors are recognized in:

- Repository contributors list
- Release notes
- Project documentation
- Community acknowledgments

## Release Process

### Version Numbering

We use Semantic Versioning (SemVer):

- **MAJOR**: Incompatible framework changes
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

### Framework Versioning

Framework versions (currently v3.1.1) may have different versioning:

- **MAJOR**: Significant architectural changes
- **MINOR**: Factor additions or modifications
- **PATCH**: Bug fixes and minor improvements

## Security

Please review our [Security Policy](SECURITY.md) for reporting security vulnerabilities.

### Security Considerations

- Input validation for all user data
- Secure handling of assessment data
- API authentication and authorization
- Data privacy and retention policies

## Questions?

If you have questions not covered in this guide:

1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/TheWayWithin/mastery-ai-framework/issues)
3. Create a [new issue](https://github.com/TheWayWithin/mastery-ai-framework/issues/new)

Thank you for contributing to the MASTERY-AI Framework! Your contributions help improve AI optimization for everyone.