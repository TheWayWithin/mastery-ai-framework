"""
Core Assessment Engine for MASTERY-AI Framework
Orchestrates assessments across all 8 pillars and 148 atomic factors
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import json
from pathlib import Path

from pydantic import BaseModel, Field
import numpy as np

from mastery_ai.core.schema import (
    FrameworkSchema,
    PillarType,
    AssessmentResult,
    Pillar
)
from mastery_ai.core.config import Config
from mastery_ai.core.scoring import ScoringEngine


class AssessmentInput(BaseModel):
    """Input data for assessment"""
    url: Optional[str] = Field(None, description="URL to assess")
    content: Optional[Dict[str, Any]] = Field(None, description="Content data")
    technical_data: Optional[Dict[str, Any]] = Field(None, description="Technical infrastructure data")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class AssessmentEngine:
    """
    Main assessment engine for MASTERY-AI Framework
    Coordinates assessment across all pillars and generates comprehensive results
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        Initialize the assessment engine
        
        Args:
            config: Optional configuration object
        """
        self.config = config or Config()
        self.schema = FrameworkSchema.get_default_schema()
        self.scoring_engine = ScoringEngine(self.schema)
        self._pillar_assessors = {}
        self._initialize_pillars()
    
    def _initialize_pillars(self):
        """Initialize pillar-specific assessors"""
        # Import pillar implementations dynamically to avoid circular imports
        from mastery_ai.pillars import (
            AIResponsePillar,
            AuthorityPillar,
            MachineReadabilityPillar,
            SemanticContentPillar,
            EngagementPillar,
            TopicalExpertisePillar,
            ReferenceNetworksPillar,
            YieldOptimizationPillar
        )
        
        # Map pillar types to their implementation classes
        pillar_classes = {
            PillarType.AI: AIResponsePillar,
            PillarType.A: AuthorityPillar,
            PillarType.M: MachineReadabilityPillar,
            PillarType.S: SemanticContentPillar,
            PillarType.E: EngagementPillar,
            PillarType.T: TopicalExpertisePillar,
            PillarType.R: ReferenceNetworksPillar,
            PillarType.Y: YieldOptimizationPillar,
        }
        
        # Initialize each pillar assessor
        for pillar_type, pillar_class in pillar_classes.items():
            self._pillar_assessors[pillar_type] = pillar_class(
                self.schema.pillars[pillar_type]
            )
    
    def assess(self, input_data: AssessmentInput) -> AssessmentResult:
        """
        Perform a comprehensive assessment across all pillars
        
        Args:
            input_data: Input data for assessment
            
        Returns:
            AssessmentResult with scores and recommendations
        """
        # Initialize results containers
        pillar_scores = {}
        factor_scores = {}
        all_recommendations = []
        
        # Assess each pillar
        for pillar_type in PillarType:
            if pillar_type in self._pillar_assessors:
                assessor = self._pillar_assessors[pillar_type]
                
                # Perform pillar-specific assessment
                pillar_result = assessor.assess(input_data)
                
                # Store pillar score
                pillar_scores[pillar_type] = pillar_result["score"]
                
                # Store factor scores
                factor_scores.update(pillar_result.get("factor_scores", {}))
                
                # Collect recommendations
                all_recommendations.extend(pillar_result.get("recommendations", []))
        
        # Calculate overall weighted score
        overall_score = self.scoring_engine.calculate_overall_score(pillar_scores)
        
        # Sort recommendations by priority
        all_recommendations = self._prioritize_recommendations(all_recommendations)
        
        # Create assessment result
        result = AssessmentResult(
            timestamp=datetime.utcnow().isoformat(),
            overall_score=overall_score,
            pillar_scores=pillar_scores,
            factor_scores=factor_scores,
            recommendations=all_recommendations[:10],  # Top 10 recommendations
            metadata={
                "framework_version": self.schema.version,
                "assessment_type": "comprehensive",
                "input_type": self._determine_input_type(input_data),
                "config": self.config.to_dict() if hasattr(self.config, 'to_dict') else {}
            }
        )
        
        return result
    
    def assess_pillar(self, pillar_type: PillarType, input_data: AssessmentInput) -> Dict[str, Any]:
        """
        Perform assessment for a specific pillar only
        
        Args:
            pillar_type: The pillar to assess
            input_data: Input data for assessment
            
        Returns:
            Dictionary with pillar-specific results
        """
        if pillar_type not in self._pillar_assessors:
            raise ValueError(f"Unknown pillar type: {pillar_type}")
        
        assessor = self._pillar_assessors[pillar_type]
        return assessor.assess(input_data)
    
    def validate_input(self, input_data: AssessmentInput) -> Dict[str, Any]:
        """
        Validate input data for assessment
        
        Args:
            input_data: Input data to validate
            
        Returns:
            Validation results with any issues found
        """
        validation_results = {
            "valid": True,
            "issues": [],
            "warnings": [],
            "data_completeness": 0.0
        }
        
        # Check for required data
        if not input_data.url and not input_data.content:
            validation_results["valid"] = False
            validation_results["issues"].append("Either URL or content data is required")
        
        # Check data completeness for each pillar
        completeness_scores = []
        for pillar_type, assessor in self._pillar_assessors.items():
            if hasattr(assessor, 'validate_input'):
                pillar_validation = assessor.validate_input(input_data)
                completeness_scores.append(pillar_validation.get("completeness", 0.0))
                
                if pillar_validation.get("issues"):
                    validation_results["warnings"].extend([
                        f"{pillar_type.value}: {issue}" 
                        for issue in pillar_validation["issues"]
                    ])
        
        # Calculate overall data completeness
        if completeness_scores:
            validation_results["data_completeness"] = np.mean(completeness_scores)
        
        return validation_results
    
    def generate_report(self, result: AssessmentResult, format: str = "json") -> str:
        """
        Generate a formatted report from assessment results
        
        Args:
            result: Assessment result to format
            format: Output format (json, html, markdown)
            
        Returns:
            Formatted report string
        """
        if format == "json":
            return json.dumps(result.dict(), indent=2, default=str)
        elif format == "markdown":
            return self._generate_markdown_report(result)
        elif format == "html":
            return self._generate_html_report(result)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _generate_markdown_report(self, result: AssessmentResult) -> str:
        """Generate a markdown formatted report"""
        report = []
        report.append(f"# MASTERY-AI Framework Assessment Report")
        report.append(f"\n**Assessment Date:** {result.timestamp}")
        report.append(f"**Framework Version:** {self.schema.version}")
        report.append(f"\n## Overall Score: {result.overall_score:.1f}/100")
        
        report.append(f"\n## Pillar Scores\n")
        for pillar_type in PillarType:
            if pillar_type in result.pillar_scores:
                pillar = self.schema.pillars[pillar_type]
                score = result.pillar_scores[pillar_type]
                report.append(f"- **{pillar.name}** ({pillar.weight}% weight): {score:.1f}/100")
        
        report.append(f"\n## Top Recommendations\n")
        for i, rec in enumerate(result.recommendations, 1):
            report.append(f"{i}. {rec}")
        
        return "\n".join(report)
    
    def _generate_html_report(self, result: AssessmentResult) -> str:
        """Generate an HTML formatted report"""
        # This would use Jinja2 templates in production
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>MASTERY-AI Assessment Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1 {{ color: #333; }}
                .score {{ font-size: 24px; font-weight: bold; color: #007bff; }}
                .pillar {{ margin: 10px 0; padding: 10px; background: #f8f9fa; }}
            </style>
        </head>
        <body>
            <h1>MASTERY-AI Framework Assessment Report</h1>
            <p><strong>Assessment Date:</strong> {result.timestamp}</p>
            <p class="score">Overall Score: {result.overall_score:.1f}/100</p>
            <h2>Pillar Scores</h2>
            {"".join(f'<div class="pillar">{p}: {s:.1f}/100</div>' for p, s in result.pillar_scores.items())}
            <h2>Recommendations</h2>
            <ol>
                {"".join(f'<li>{rec}</li>' for rec in result.recommendations)}
            </ol>
        </body>
        </html>
        """
        return html
    
    def _determine_input_type(self, input_data: AssessmentInput) -> str:
        """Determine the type of input data provided"""
        if input_data.url:
            return "url"
        elif input_data.content:
            return "content"
        else:
            return "unknown"
    
    def _prioritize_recommendations(self, recommendations: List[str]) -> List[str]:
        """
        Prioritize recommendations based on impact and ease of implementation
        
        Args:
            recommendations: List of all recommendations
            
        Returns:
            Prioritized list of recommendations
        """
        # For now, return unique recommendations in order
        # In production, this would use a more sophisticated prioritization algorithm
        seen = set()
        prioritized = []
        for rec in recommendations:
            if rec not in seen:
                seen.add(rec)
                prioritized.append(rec)
        return prioritized
    
    def save_result(self, result: AssessmentResult, filepath: Path):
        """
        Save assessment result to file
        
        Args:
            result: Assessment result to save
            filepath: Path to save file
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(result.dict(), f, indent=2, default=str)
    
    def load_result(self, filepath: Path) -> AssessmentResult:
        """
        Load assessment result from file
        
        Args:
            filepath: Path to result file
            
        Returns:
            Loaded assessment result
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        return AssessmentResult(**data)