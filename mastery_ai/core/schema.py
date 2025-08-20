"""
MASTERY-AI Framework Schema v3.1.1
Defines the complete framework structure with all 148 atomic factors across 8 pillars
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field, validator
from enum import Enum


class PillarType(str, Enum):
    """Enumeration of the 8 MASTERY pillars"""
    AI = "AI"  # AI Response Optimization & Citation
    A = "A"    # Authority & Trust Signals
    M = "M"    # Machine Readability & Technical Infrastructure
    S = "S"    # Semantic Content Quality
    E = "E"    # Engagement & User Experience
    T = "T"    # Topical Expertise & Experience
    R = "R"    # Reference Networks & Citations
    Y = "Y"    # Yield Optimization & Freshness


class Factor(BaseModel):
    """Individual atomic factor within a pillar"""
    id: str = Field(..., description="Unique factor identifier (e.g., AI.1.1)")
    name: str = Field(..., description="Factor name")
    description: str = Field(..., description="Factor description")
    weight: float = Field(..., ge=0, le=100, description="Factor weight within pillar")
    evaluation_criteria: List[str] = Field(default_factory=list, description="Evaluation criteria")
    data_requirements: List[str] = Field(default_factory=list, description="Required data points")


class SubPillar(BaseModel):
    """Sub-pillar containing related factors"""
    id: str = Field(..., description="Sub-pillar identifier (e.g., AI.1)")
    name: str = Field(..., description="Sub-pillar name")
    description: str = Field(..., description="Sub-pillar description")
    factors: List[Factor] = Field(default_factory=list, description="List of factors")
    
    @validator('factors')
    def validate_factor_weights(cls, v):
        """Ensure factor weights within sub-pillar sum to approximately 100%"""
        if v:
            total_weight = sum(f.weight for f in v)
            if abs(total_weight - 100.0) > 0.1:  # Allow 0.1% tolerance
                raise ValueError(f"Factor weights must sum to 100%, got {total_weight}")
        return v


class Pillar(BaseModel):
    """Main pillar of the MASTERY framework"""
    type: PillarType = Field(..., description="Pillar type")
    name: str = Field(..., description="Full pillar name")
    weight: float = Field(..., ge=0, le=100, description="Pillar weight in overall framework")
    factor_count: int = Field(..., ge=0, description="Total number of factors")
    sub_pillars: List[SubPillar] = Field(default_factory=list, description="Sub-pillars")
    
    @validator('factor_count')
    def validate_factor_count(cls, v, values):
        """Validate that factor count matches actual factors"""
        if 'sub_pillars' in values:
            actual_count = sum(len(sp.factors) for sp in values['sub_pillars'])
            if actual_count != v:
                raise ValueError(f"Factor count mismatch: declared {v}, actual {actual_count}")
        return v


class FrameworkSchema(BaseModel):
    """Complete MASTERY-AI Framework Schema v3.1.1"""
    version: str = Field(default="3.1.1", description="Framework version")
    name: str = Field(default="MASTERY-AI Framework", description="Framework name")
    edition: str = Field(default="Enhanced Content Accessibility Edition", description="Edition")
    total_factors: int = Field(default=148, description="Total number of atomic factors")
    pillars: Dict[PillarType, Pillar] = Field(..., description="Framework pillars")
    
    @validator('pillars')
    def validate_pillar_weights(cls, v):
        """Ensure pillar weights sum to exactly 100%"""
        total_weight = sum(p.weight for p in v.values())
        if abs(total_weight - 100.0) > 0.01:  # Allow 0.01% tolerance for rounding
            raise ValueError(f"Pillar weights must sum to 100%, got {total_weight}")
        return v
    
    @validator('total_factors')
    def validate_total_factors(cls, v, values):
        """Validate total factor count across all pillars"""
        if 'pillars' in values:
            actual_total = sum(p.factor_count for p in values['pillars'].values())
            if actual_total != v:
                raise ValueError(f"Total factor count mismatch: declared {v}, actual {actual_total}")
        return v
    
    @classmethod
    def get_default_schema(cls) -> "FrameworkSchema":
        """Return the default MASTERY-AI Framework v3.1.1 schema"""
        return cls(
            pillars={
                PillarType.AI: Pillar(
                    type=PillarType.AI,
                    name="AI Response Optimization & Citation",
                    weight=23.8,
                    factor_count=23,
                    sub_pillars=[]  # To be populated with actual factors
                ),
                PillarType.A: Pillar(
                    type=PillarType.A,
                    name="Authority & Trust Signals",
                    weight=17.9,
                    factor_count=15,
                    sub_pillars=[]
                ),
                PillarType.M: Pillar(
                    type=PillarType.M,
                    name="Machine Readability & Technical Infrastructure",
                    weight=14.6,
                    factor_count=21,  # Increased from 19 for LLMs.txt
                    sub_pillars=[]
                ),
                PillarType.S: Pillar(
                    type=PillarType.S,
                    name="Semantic Content Quality",
                    weight=13.9,
                    factor_count=22,
                    sub_pillars=[]
                ),
                PillarType.E: Pillar(
                    type=PillarType.E,
                    name="Engagement & User Experience",
                    weight=10.9,
                    factor_count=19,
                    sub_pillars=[]
                ),
                PillarType.T: Pillar(
                    type=PillarType.T,
                    name="Topical Expertise & Experience",
                    weight=8.9,
                    factor_count=14,
                    sub_pillars=[]
                ),
                PillarType.R: Pillar(
                    type=PillarType.R,
                    name="Reference Networks & Citations",
                    weight=5.9,
                    factor_count=19,
                    sub_pillars=[]
                ),
                PillarType.Y: Pillar(
                    type=PillarType.Y,
                    name="Yield Optimization & Freshness",
                    weight=4.1,
                    factor_count=15,
                    sub_pillars=[]
                ),
            }
        )
    
    def get_pillar_by_weight_order(self) -> List[Pillar]:
        """Return pillars sorted by weight (descending)"""
        return sorted(self.pillars.values(), key=lambda p: p.weight, reverse=True)
    
    def validate_mathematical_precision(self) -> Dict[str, any]:
        """Validate mathematical precision of the framework"""
        results = {
            "valid": True,
            "pillar_weight_sum": sum(p.weight for p in self.pillars.values()),
            "total_factors": sum(p.factor_count for p in self.pillars.values()),
            "errors": []
        }
        
        # Check pillar weights
        if abs(results["pillar_weight_sum"] - 100.0) > 0.01:
            results["valid"] = False
            results["errors"].append(f"Pillar weights sum to {results['pillar_weight_sum']}, not 100%")
        
        # Check factor count
        if results["total_factors"] != self.total_factors:
            results["valid"] = False
            results["errors"].append(f"Factor count mismatch: {results['total_factors']} != {self.total_factors}")
        
        return results


class AssessmentResult(BaseModel):
    """Result of a framework assessment"""
    timestamp: str = Field(..., description="Assessment timestamp")
    overall_score: float = Field(..., ge=0, le=100, description="Overall assessment score")
    pillar_scores: Dict[PillarType, float] = Field(..., description="Individual pillar scores")
    factor_scores: Dict[str, float] = Field(..., description="Individual factor scores")
    recommendations: List[str] = Field(default_factory=list, description="Improvement recommendations")
    metadata: Dict[str, any] = Field(default_factory=dict, description="Additional metadata")