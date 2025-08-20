"""
Configuration Management for MASTERY-AI Framework
Handles framework configuration, customization, and environment settings
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, validator


class AssessmentConfig(BaseModel):
    """Configuration for assessment behavior"""
    enable_all_pillars: bool = Field(default=True, description="Enable all pillars in assessment")
    enabled_pillars: List[str] = Field(default_factory=lambda: ["AI", "A", "M", "S", "E", "T", "R", "Y"])
    min_data_completeness: float = Field(default=0.6, ge=0.0, le=1.0, description="Minimum data completeness for assessment")
    strict_validation: bool = Field(default=False, description="Enable strict input validation")
    parallel_processing: bool = Field(default=True, description="Enable parallel pillar processing")
    timeout_seconds: int = Field(default=300, description="Maximum assessment time in seconds")


class ScoringConfig(BaseModel):
    """Configuration for scoring behavior"""
    use_weighted_scoring: bool = Field(default=True, description="Use weighted scoring")
    custom_weights: Optional[Dict[str, float]] = Field(default=None, description="Custom pillar weights")
    normalization_method: str = Field(default="standard", description="Score normalization method")
    decimal_places: int = Field(default=1, description="Decimal places in scores")
    
    @validator('custom_weights')
    def validate_custom_weights(cls, v):
        """Ensure custom weights sum to 100%"""
        if v is not None:
            total = sum(v.values())
            if abs(total - 100.0) > 0.01:
                raise ValueError(f"Custom weights must sum to 100%, got {total}")
        return v


class ReportingConfig(BaseModel):
    """Configuration for reporting and output"""
    default_format: str = Field(default="json", description="Default report format")
    include_factor_scores: bool = Field(default=True, description="Include individual factor scores")
    include_metadata: bool = Field(default=True, description="Include assessment metadata")
    max_recommendations: int = Field(default=10, description="Maximum recommendations to include")
    verbose_output: bool = Field(default=False, description="Enable verbose output")
    save_results: bool = Field(default=False, description="Automatically save results")
    results_directory: str = Field(default="./results", description="Directory for saved results")


class APIConfig(BaseModel):
    """Configuration for API settings"""
    host: str = Field(default="0.0.0.0", description="API host")
    port: int = Field(default=8000, description="API port")
    reload: bool = Field(default=False, description="Enable auto-reload")
    cors_enabled: bool = Field(default=True, description="Enable CORS")
    cors_origins: List[str] = Field(default_factory=lambda: ["*"], description="CORS allowed origins")
    rate_limit: int = Field(default=100, description="Requests per minute limit")
    api_key_required: bool = Field(default=False, description="Require API key")


class Config:
    """
    Main configuration class for MASTERY-AI Framework
    Manages all configuration aspects of the framework
    """
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize configuration
        
        Args:
            config_path: Optional path to configuration file
        """
        self.config_path = config_path
        self.assessment = AssessmentConfig()
        self.scoring = ScoringConfig()
        self.reporting = ReportingConfig()
        self.api = APIConfig()
        
        # Load configuration from file if provided
        if config_path:
            self.load_from_file(config_path)
        
        # Override with environment variables
        self.load_from_env()
    
    def load_from_file(self, filepath: Path):
        """
        Load configuration from JSON file
        
        Args:
            filepath: Path to configuration file
        """
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"Configuration file not found: {filepath}")
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Update configuration sections
        if 'assessment' in data:
            self.assessment = AssessmentConfig(**data['assessment'])
        if 'scoring' in data:
            self.scoring = ScoringConfig(**data['scoring'])
        if 'reporting' in data:
            self.reporting = ReportingConfig(**data['reporting'])
        if 'api' in data:
            self.api = APIConfig(**data['api'])
    
    def load_from_env(self):
        """Load configuration from environment variables"""
        # Assessment configuration
        if os.getenv('MASTERY_ENABLE_ALL_PILLARS'):
            self.assessment.enable_all_pillars = os.getenv('MASTERY_ENABLE_ALL_PILLARS').lower() == 'true'
        if os.getenv('MASTERY_MIN_DATA_COMPLETENESS'):
            self.assessment.min_data_completeness = float(os.getenv('MASTERY_MIN_DATA_COMPLETENESS'))
        
        # Scoring configuration
        if os.getenv('MASTERY_USE_WEIGHTED_SCORING'):
            self.scoring.use_weighted_scoring = os.getenv('MASTERY_USE_WEIGHTED_SCORING').lower() == 'true'
        if os.getenv('MASTERY_DECIMAL_PLACES'):
            self.scoring.decimal_places = int(os.getenv('MASTERY_DECIMAL_PLACES'))
        
        # Reporting configuration
        if os.getenv('MASTERY_DEFAULT_FORMAT'):
            self.reporting.default_format = os.getenv('MASTERY_DEFAULT_FORMAT')
        if os.getenv('MASTERY_MAX_RECOMMENDATIONS'):
            self.reporting.max_recommendations = int(os.getenv('MASTERY_MAX_RECOMMENDATIONS'))
        
        # API configuration
        if os.getenv('MASTERY_API_HOST'):
            self.api.host = os.getenv('MASTERY_API_HOST')
        if os.getenv('MASTERY_API_PORT'):
            self.api.port = int(os.getenv('MASTERY_API_PORT'))
        if os.getenv('MASTERY_API_KEY_REQUIRED'):
            self.api.api_key_required = os.getenv('MASTERY_API_KEY_REQUIRED').lower() == 'true'
    
    def save_to_file(self, filepath: Path):
        """
        Save current configuration to JSON file
        
        Args:
            filepath: Path to save configuration
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        config_dict = self.to_dict()
        
        with open(filepath, 'w') as f:
            json.dump(config_dict, f, indent=2)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to dictionary
        
        Returns:
            Dictionary representation of configuration
        """
        return {
            'assessment': self.assessment.dict(),
            'scoring': self.scoring.dict(),
            'reporting': self.reporting.dict(),
            'api': self.api.dict()
        }
    
    def validate(self) -> Dict[str, Any]:
        """
        Validate configuration settings
        
        Returns:
            Validation results
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Validate enabled pillars
        valid_pillars = ["AI", "A", "M", "S", "E", "T", "R", "Y"]
        for pillar in self.assessment.enabled_pillars:
            if pillar not in valid_pillars:
                results['valid'] = False
                results['errors'].append(f"Invalid pillar: {pillar}")
        
        # Validate custom weights if provided
        if self.scoring.custom_weights:
            for pillar in self.scoring.custom_weights:
                if pillar not in valid_pillars:
                    results['valid'] = False
                    results['errors'].append(f"Invalid pillar in custom weights: {pillar}")
        
        # Validate report format
        valid_formats = ["json", "markdown", "html"]
        if self.reporting.default_format not in valid_formats:
            results['valid'] = False
            results['errors'].append(f"Invalid report format: {self.reporting.default_format}")
        
        # Check for potential issues
        if self.assessment.min_data_completeness < 0.3:
            results['warnings'].append("Very low min_data_completeness may produce unreliable results")
        
        if self.assessment.timeout_seconds < 30:
            results['warnings'].append("Very short timeout may prevent complete assessments")
        
        return results
    
    @classmethod
    def get_default_config(cls) -> "Config":
        """
        Get default configuration instance
        
        Returns:
            Default configuration
        """
        return cls()
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Config":
        """
        Create configuration from dictionary
        
        Args:
            data: Configuration dictionary
            
        Returns:
            Configuration instance
        """
        config = cls()
        
        if 'assessment' in data:
            config.assessment = AssessmentConfig(**data['assessment'])
        if 'scoring' in data:
            config.scoring = ScoringConfig(**data['scoring'])
        if 'reporting' in data:
            config.reporting = ReportingConfig(**data['reporting'])
        if 'api' in data:
            config.api = APIConfig(**data['api'])
        
        return config