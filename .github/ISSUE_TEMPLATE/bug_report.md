---
name: Bug Report
about: Create a report to help us improve the MASTERY-AI Framework
title: '[BUG] '
labels: ['bug', 'needs-triage']
assignees: ''

---

## Bug Description

**Summary**
A clear and concise description of what the bug is.

**Expected Behavior**
A clear description of what you expected to happen.

**Actual Behavior**
A clear description of what actually happened.

## Environment Information

**Framework Version**
- Framework Version: [e.g., v3.1.1]
- Library Version: [e.g., 1.0.0]
- Installation Method: [pip, source, docker]

**System Environment**
- Python Version: [e.g., 3.9.7]
- Operating System: [e.g., Ubuntu 22.04, macOS 13.0, Windows 11]
- Architecture: [e.g., x86_64, ARM64]

**Dependencies**
- Relevant package versions (paste from `pip list` if needed)

## Reproduction Steps

**Minimal Reproduction Case**
Provide the smallest possible code example that reproduces the issue:

```python
# Your code here
from mastery_ai import AssessmentEngine

engine = AssessmentEngine()
# Steps to reproduce...
```

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Input Data**
If applicable, provide anonymized assessment input data:

```json
{
  "url": "https://example.com",
  "content": {...},
  "technical_data": {...}
}
```

## Error Details

**Error Messages**
Provide the complete error message and stack trace:

```
Traceback (most recent call last):
  File "...", line ..., in ...
    ...
Error: ...
```

**Log Output**
Include relevant log output (please anonymize any sensitive data):

```
[2025-01-20 10:30:15] ERROR: ...
```

## Framework-Specific Information

**Affected Pillars**
Which pillar(s) are affected by this bug? (check all that apply)
- [ ] AI - AI Response Optimization & Citation
- [ ] A - Authority & Trust Signals  
- [ ] M - Machine Readability & Technical Infrastructure
- [ ] S - Semantic Content Quality
- [ ] E - Engagement & User Experience
- [ ] T - Topical Expertise & Experience
- [ ] R - Reference Networks & Citations
- [ ] Y - Yield Optimization & Freshness
- [ ] Core Assessment Engine
- [ ] API Endpoints
- [ ] Other (specify): 

**Assessment Results**
If applicable, describe the impact on assessment results:

- Expected Score Range: [e.g., 75-85]
- Actual Score: [e.g., 45]
- Affected Factors: [e.g., specific factors not working]

**Performance Impact**
- Assessment Duration: [e.g., 2 minutes instead of <30 seconds]
- Memory Usage: [e.g., high memory consumption]
- Other Performance Issues: [describe]

## Additional Context

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Configuration**
Provide relevant configuration details:

```python
config = Config()
config.setting = value  # Any custom configuration
```

**Workarounds**
Have you found any workarounds for this issue?

**Impact Assessment**
- [ ] Blocks functionality completely
- [ ] Causes incorrect assessment results
- [ ] Performance degradation
- [ ] Minor inconvenience
- [ ] Documentation or usability issue

**Related Issues**
Link any related issues or pull requests.

## Framework Validation

**Schema Validation**
Have you run the framework validation script?

```bash
python Ideation/schema_v3_1_1_validation.py
```

Result: [Pass/Fail with details]

**Test Status**
Have you run the test suite?

```bash
pytest
```

Result: [Pass/Fail with details]

## Checklist

Please confirm the following:

- [ ] I have searched existing issues for duplicates
- [ ] I have provided a minimal reproduction case
- [ ] I have included all relevant error messages and logs
- [ ] I have tested this with the latest supported version
- [ ] I have anonymized any sensitive data in my report
- [ ] I have run the framework validation script (if applicable)

## Additional Information

Add any other context about the problem here, including:

- When did this issue first occur?
- Does this happen consistently or intermittently?
- Any recent changes to your environment or configuration?
- Any additional debugging steps you've taken?

---

**Note**: For security vulnerabilities, please do not create a public issue. Instead, please follow our [Security Policy](../../SECURITY.md) and report through appropriate private channels.