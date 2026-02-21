import logging
from typing import Dict, Any
from .discovery_service import ComponentDiscoveryService
from .integration_manager import IntegrationManager

logger = logging.getLogger(__name__)

class DynamicComponentLoader:
    """Manages dynamic loading and integration of AI components."""
    
    def __init__(self):
        self.discovery = ComponentDiscoveryService()
        self.integration = IntegrationManager()
        
    def load_component(self, component_config: Dict[str, Any]) -> None:
        """Load and integrate a component based on its configuration."""
        try:
            # Discover the component
            if not self.discovery.register_component(
                component_config["name"], component_config["description"]
            ):
                raise ValueError("Component registration failed")
                
            # Integrate the component
            criteria = {
                "type": component_config["type"],
                "version": component_config["version"]
            }
            best_component = self.integration.get_best_component(criteria)
            self.integration.integrate_component(best_component)
            
        except Exception as e:
            logger.error(f"Component loading failed: {str(e)}")
            raise ComponentLoadingError("Failed to load and integrate component")