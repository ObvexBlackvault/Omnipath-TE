import abc
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

class ForkBaseAgent(abc.ABC):
    """
    Abstract base class for Omnipath agents.
    Provides a standard lifecycle: validation, initialization, execution, shutdown.
    """

    def __init__(self, agent_id: str, mission_payload: Dict[str, Any]):
        self.agent_id = agent_id
        self.mission_payload = mission_payload
        self.logger = logger.getChild(self.__class__.__name__)
        self.initialized = False
        self.terminated = False

    def run(self) -> Any:
        """
        Execute the agent lifecycle: validate, initialize, execute, then shutdown.
        Returns the result of execute_mission().
        """
        self.logger.info("Starting run sequence for agent '%s'.", self.agent_id)

        if not self.validate_mission():
            msg = f"Mission validation failed for agent '{self.agent_id}'."
            self.logger.error(msg)
            raise ValueError(msg)

        self.initialize()

        result = None
        try:
            result = self.execute_mission()
        except Exception:
            self.logger.exception(
                "Unhandled exception during execution for agent '%s'.", 
                self.agent_id
            )
            raise
        finally:
            self.shutdown()

        self.logger.info("Run sequence completed for agent '%s'.", self.agent_id)
        return result

    @abc.abstractmethod
    def validate_mission(self) -> bool:
        """
        Validate the mission_payload before execution.
        Should return True if payload is valid, False otherwise.
        """

    def initialize(self) -> None:
        """
        Prepare any resources, connections, or state needed.
        Called once before execute_mission().
        """
        self.initialized = True
        self.logger.debug("Initialization complete for agent '%s'.", self.agent_id)

    @abc.abstractmethod
    def execute_mission(self) -> Any:
        """
        Core mission logic.
        Subclasses must implement this method.
        """

    def shutdown(self) -> None:
        """
        Cleanup resources, close connections, and perform any teardown.
        Called once after execute_mission(), even if execution raises.
        """
        self.terminated = True
        self.logger.debug("Shutdown complete for agent '%s'.", self.agent_id)
