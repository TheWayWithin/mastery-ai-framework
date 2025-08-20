"""
Base Pillar Implementation for MASTERY-AI Framework
Abstract base class for all pillar implementations
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from mastery_ai.core.schema import Pillar, Factor, SubPillar
from mastery_ai.core.scoring import ScoringEngine


class BasePillar(ABC):
    """
    Abstract base class for pillar implementations
    All pillars must inherit from this class
    """
    
    def __init__(self, pillar_schema: Pillar):
        """
        Initialize base pillar
        
        Args:
            pillar_schema: Pillar schema definition
        """
        self.pillar_schema = pillar_schema
        self.pillar_type = pillar_schema.type
        self.pillar_name = pillar_schema.name
        self.weight = pillar_schema.weight
        self.factor_count = pillar_schema.factor_count
        self._initialize_factors()
    
    @abstractmethod
    def _initialize_factors(self):
        """Initialize pillar-specific factors and sub-pillars"""
        pass
    
    @abstractmethod
    def assess(self, input_data: Any) -> Dict[str, Any]:
        """
        Perform pillar-specific assessment
        
        Args:
            input_data: Assessment input data
            
        Returns:
            Dictionary with assessment results including score and recommendations
        """
        pass
    
    @abstractmethod
    def evaluate_factor(self, factor: Factor, input_data: Any) -> float:
        """
        Evaluate a specific factor
        
        Args:
            factor: Factor to evaluate
            input_data: Assessment input data
            
        Returns:
            Factor score (0-100)
        """
        pass
    
    def validate_input(self, input_data: Any) -> Dict[str, Any]:
        """
        Validate input data for this pillar
        
        Args:
            input_data: Input data to validate
            
        Returns:
            Validation results with completeness score
        """
        validation = {
            "valid": True,
            "completeness": 0.0,
            "issues": [],
            "warnings": []
        }
        
        # Check for required data points for this pillar
        required_data = self.get_required_data_points()
        available_data = self.get_available_data_points(input_data)
        
        if not available_data:
            validation["valid"] = False
            validation["issues"].append(f"No data available for {self.pillar_name} assessment")
        else:
            # Calculate completeness
            validation["completeness"] = len(available_data) / len(required_data) if required_data else 0.0
            
            # Identify missing critical data
            critical_missing = set(required_data) - set(available_data)
            if critical_missing:
                validation["warnings"].append(f"Missing data points: {', '.join(critical_missing)}")
        
        return validation
    
    def get_required_data_points(self) -> List[str]:
        """
        Get list of required data points for this pillar
        
        Returns:
            List of required data point names
        """
        data_points = []
        for sub_pillar in self.pillar_schema.sub_pillars:
            for factor in sub_pillar.factors:
                data_points.extend(factor.data_requirements)
        return list(set(data_points))
    
    def get_available_data_points(self, input_data: Any) -> List[str]:
        """
        Get list of available data points from input
        
        Args:
            input_data: Assessment input data
            
        Returns:
            List of available data point names
        """
        # This is a placeholder - actual implementation depends on input structure
        available = []
        
        if hasattr(input_data, 'content') and input_data.content:
            available.extend(input_data.content.keys())
        
        if hasattr(input_data, 'technical_data') and input_data.technical_data:
            available.extend(input_data.technical_data.keys())
        
        if hasattr(input_data, 'metadata') and input_data.metadata:
            available.extend(input_data.metadata.keys())
        
        return available
    
    def generate_recommendations(self, factor_scores: Dict[str, float]) -> List[str]:
        """
        Generate recommendations based on factor scores
        
        Args:
            factor_scores: Dictionary of factor scores
            
        Returns:
            List of prioritized recommendations
        """
        recommendations = []
        
        # Find low-scoring factors
        for factor_id, score in factor_scores.items():
            if score < 50:  # Critical threshold
                factor = self.get_factor_by_id(factor_id)
                if factor:
                    recommendations.append(
                        f"Critical: Improve {factor.name} (current score: {score:.1f}/100)"
                    )
            elif score < 70:  # Improvement needed
                factor = self.get_factor_by_id(factor_id)
                if factor:
                    recommendations.append(
                        f"Improve: {factor.name} (current score: {score:.1f}/100)"
                    )
        
        return recommendations[:5]  # Return top 5 recommendations
    
    def get_factor_by_id(self, factor_id: str) -> Optional[Factor]:
        """
        Get factor by its ID
        
        Args:
            factor_id: Factor identifier
            
        Returns:
            Factor object or None if not found
        """
        for sub_pillar in self.pillar_schema.sub_pillars:
            for factor in sub_pillar.factors:
                if factor.id == factor_id:
                    return factor
        return None
    
    def calculate_pillar_score(self, factor_scores: Dict[str, float]) -> float:
        """
        Calculate overall pillar score from factor scores
        
        Args:
            factor_scores: Dictionary of factor scores
            
        Returns:
            Weighted pillar score (0-100)
        """
        if not factor_scores:
            return 0.0
        
        # Get factor weights
        factor_weights = {}
        for sub_pillar in self.pillar_schema.sub_pillars:
            for factor in sub_pillar.factors:
                factor_weights[factor.id] = factor.weight
        
        # Calculate weighted average
        weighted_sum = 0.0
        total_weight = 0.0
        
        for factor_id, score in factor_scores.items():
            if factor_id in factor_weights:
                weight = factor_weights[factor_id]
                weighted_sum += score * weight
                total_weight += weight
        
        if total_weight > 0:
            return weighted_sum / total_weight
        
        return 0.0