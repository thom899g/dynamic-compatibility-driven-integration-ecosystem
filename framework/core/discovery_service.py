import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class ComponentDiscoveryService:
    """Manages discovery and registration of AI components in the ecosystem."""
    
    def __init__(self):
        self.components_registry: Dict[str, Dict[str, Any]] = {}
        
    def register_component(self, name: str, component_desc: Dict[str, Any]) -> bool:
        """Register a new component with the system."""
        if not self._is_valid_component(component_desc):
            logger.error("Invalid component description")
            return False
        self.components_registry[name] = component_desc
        logger.info(f"Component registered: {name}")
        return True
        
    def _is_valid_component(self, component_desc: Dict[str, Any]) -> bool:
        """Validate the component description schema."""
        required_fields = ["type", "version", "interfaces"]
        try:
            for field in required_fields:
                if field not in component_desc:
                    raise ValueError(f"Missing required field: {field}")
            return True
        except Exception as e:
            logger.error(f"Validation failed: {str(e)}")
            return False
            
    def discover_components(self) -> Dict[str, Dict[str, Any]]:
        """Discover and return all registered components."""
        logger.info("Discovering available components")
        return self.components_registry.copy()