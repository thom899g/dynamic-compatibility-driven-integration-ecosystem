import logging
from abc import ABC, abstractmethod
from typing import Dict, Any

logger = logging.getLogger(__name__)

class CompatibilityEvaluator(ABC):
    """Abstract base class for AI component compatibility evaluators.

    This class defines the interface for evaluating compatibility between AI components.
    Subclasses must implement the `evaluate` method to provide specific evaluation logic.
    """
    
    @abstractmethod
    def evaluate(self, component1: Dict[str, Any], component2: Dict[str, Any]) -> float:
        """Evaluate compatibility between two components.

        Args:
            component1: Dictionary describing component 1's properties.
            component2: Dictionary describing component 2's properties.

        Returns:
            A score between 0 and 1 representing the compatibility level.
        """
        pass

    def _log_evaluation(self, component1: str, component2: str, score: float) -> None:
        """Log evaluation results for debugging purposes."""
        logger.info(f"Compatibility evaluated between {component1} and {component2}: {score}")