"""
Scoring Engine for MASTERY-AI Framework
Handles all scoring calculations with mathematical precision
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
from mastery_ai.core.schema import FrameworkSchema, PillarType


class ScoringEngine:
    """
    Handles all scoring calculations for the MASTERY-AI Framework
    Ensures mathematical precision and consistency
    """
    
    def __init__(self, schema: FrameworkSchema):
        """
        Initialize scoring engine with framework schema
        
        Args:
            schema: Framework schema defining weights and structure
        """
        self.schema = schema
        self._validate_weights()
    
    def _validate_weights(self):
        """Validate that pillar weights sum to exactly 100%"""
        validation = self.schema.validate_mathematical_precision()
        if not validation["valid"]:
            raise ValueError(f"Invalid framework weights: {validation['errors']}")
    
    def calculate_overall_score(self, pillar_scores: Dict[PillarType, float]) -> float:
        """
        Calculate weighted overall score from pillar scores
        
        Args:
            pillar_scores: Dictionary of pillar scores (0-100)
            
        Returns:
            Weighted overall score (0-100)
        """
        if not pillar_scores:
            return 0.0
        
        weighted_sum = 0.0
        total_weight = 0.0
        
        for pillar_type, score in pillar_scores.items():
            if pillar_type in self.schema.pillars:
                pillar = self.schema.pillars[pillar_type]
                weighted_sum += score * (pillar.weight / 100.0)
                total_weight += pillar.weight
        
        # Handle case where not all pillars are assessed
        if total_weight > 0:
            # Normalize to account for missing pillars
            return weighted_sum * (100.0 / total_weight)
        
        return 0.0
    
    def calculate_pillar_score(self, factor_scores: Dict[str, float], factor_weights: Dict[str, float]) -> float:
        """
        Calculate pillar score from individual factor scores
        
        Args:
            factor_scores: Dictionary of factor scores (0-100)
            factor_weights: Dictionary of factor weights within pillar
            
        Returns:
            Weighted pillar score (0-100)
        """
        if not factor_scores:
            return 0.0
        
        weighted_sum = 0.0
        total_weight = 0.0
        
        for factor_id, score in factor_scores.items():
            if factor_id in factor_weights:
                weight = factor_weights[factor_id]
                weighted_sum += score * (weight / 100.0)
                total_weight += weight
        
        # Normalize if not all factors are scored
        if total_weight > 0:
            return weighted_sum * (100.0 / total_weight)
        
        return 0.0
    
    def normalize_score(self, raw_score: float, min_val: float = 0, max_val: float = 100) -> float:
        """
        Normalize a score to 0-100 range
        
        Args:
            raw_score: Raw score value
            min_val: Minimum possible value
            max_val: Maximum possible value
            
        Returns:
            Normalized score (0-100)
        """
        if max_val <= min_val:
            return 0.0
        
        normalized = ((raw_score - min_val) / (max_val - min_val)) * 100.0
        return max(0.0, min(100.0, normalized))
    
    def calculate_improvement_potential(self, current_scores: Dict[PillarType, float]) -> Dict[PillarType, float]:
        """
        Calculate improvement potential for each pillar
        
        Args:
            current_scores: Current pillar scores
            
        Returns:
            Dictionary of improvement potential by pillar
        """
        improvement_potential = {}
        
        for pillar_type in PillarType:
            if pillar_type in self.schema.pillars:
                current_score = current_scores.get(pillar_type, 0.0)
                pillar = self.schema.pillars[pillar_type]
                
                # Calculate potential impact of improving this pillar to 100
                potential_gain = (100.0 - current_score) * (pillar.weight / 100.0)
                improvement_potential[pillar_type] = potential_gain
        
        return improvement_potential
    
    def get_score_interpretation(self, score: float) -> Tuple[str, str]:
        """
        Get interpretation of a score
        
        Args:
            score: Score to interpret (0-100)
            
        Returns:
            Tuple of (rating, description)
        """
        if score >= 90:
            return ("Excellent", "Outstanding optimization with minimal improvement needed")
        elif score >= 80:
            return ("Very Good", "Strong optimization with minor improvements possible")
        elif score >= 70:
            return ("Good", "Solid optimization with some improvement opportunities")
        elif score >= 60:
            return ("Fair", "Adequate optimization with significant improvement potential")
        elif score >= 50:
            return ("Poor", "Below average optimization requiring substantial improvements")
        else:
            return ("Critical", "Major optimization issues requiring immediate attention")
    
    def calculate_percentile_rank(self, score: float, benchmark_scores: List[float]) -> float:
        """
        Calculate percentile rank of a score against benchmarks
        
        Args:
            score: Score to rank
            benchmark_scores: List of benchmark scores
            
        Returns:
            Percentile rank (0-100)
        """
        if not benchmark_scores:
            return 50.0
        
        return float(np.percentile(benchmark_scores, score))
    
    def apply_custom_weights(self, pillar_scores: Dict[PillarType, float], 
                            custom_weights: Dict[str, float]) -> float:
        """
        Calculate overall score using custom weights
        
        Args:
            pillar_scores: Dictionary of pillar scores
            custom_weights: Custom weight distribution
            
        Returns:
            Weighted overall score
        """
        # Validate custom weights sum to 100
        total_weight = sum(custom_weights.values())
        if abs(total_weight - 100.0) > 0.01:
            raise ValueError(f"Custom weights must sum to 100%, got {total_weight}")
        
        weighted_sum = 0.0
        
        for pillar_type in PillarType:
            if pillar_type.value in custom_weights and pillar_type in pillar_scores:
                score = pillar_scores[pillar_type]
                weight = custom_weights[pillar_type.value]
                weighted_sum += score * (weight / 100.0)
        
        return weighted_sum
    
    def calculate_score_delta(self, before: Dict[PillarType, float], 
                             after: Dict[PillarType, float]) -> Dict[str, any]:
        """
        Calculate the difference between two assessments
        
        Args:
            before: Previous assessment scores
            after: Current assessment scores
            
        Returns:
            Dictionary with score changes and analysis
        """
        before_overall = self.calculate_overall_score(before)
        after_overall = self.calculate_overall_score(after)
        
        pillar_deltas = {}
        for pillar_type in PillarType:
            before_score = before.get(pillar_type, 0.0)
            after_score = after.get(pillar_type, 0.0)
            pillar_deltas[pillar_type] = {
                "before": before_score,
                "after": after_score,
                "change": after_score - before_score,
                "percent_change": ((after_score - before_score) / before_score * 100) if before_score > 0 else 0
            }
        
        return {
            "overall_before": before_overall,
            "overall_after": after_overall,
            "overall_change": after_overall - before_overall,
            "pillar_changes": pillar_deltas,
            "improved_pillars": [p for p, d in pillar_deltas.items() if d["change"] > 0],
            "declined_pillars": [p for p, d in pillar_deltas.items() if d["change"] < 0]
        }
    
    def get_critical_factors(self, factor_scores: Dict[str, float], threshold: float = 50.0) -> List[str]:
        """
        Identify factors scoring below a critical threshold
        
        Args:
            factor_scores: Dictionary of factor scores
            threshold: Score threshold for critical factors
            
        Returns:
            List of critical factor IDs
        """
        return [
            factor_id for factor_id, score in factor_scores.items()
            if score < threshold
        ]
    
    def calculate_confidence_interval(self, scores: List[float], confidence: float = 0.95) -> Tuple[float, float]:
        """
        Calculate confidence interval for scores
        
        Args:
            scores: List of scores
            confidence: Confidence level (default 95%)
            
        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        if not scores:
            return (0.0, 0.0)
        
        mean = np.mean(scores)
        std = np.std(scores)
        z_score = 1.96 if confidence == 0.95 else 2.58  # 95% or 99% confidence
        
        margin = z_score * (std / np.sqrt(len(scores)))
        return (max(0, mean - margin), min(100, mean + margin))