import asyncio
import logging
from backend.core.ForkBaseAgent import ForkBaseAgent
from backend.core.mission_validator import validate_mission_payload

logger = logging.getLogger(__name__)


class ForkAlpha(ForkBaseAgent):
    def __init__(self):
        super().__init__(agent_name="ForkAlpha")

    async def run_mission(self, mission_payload: dict) -> dict:
        """
        Validate and execute the given mission payload.
        """
        try:
            logger.info(f"[{self.agent_name}] Received mission payload: {mission_payload}")
            mission = validate_mission_payload(mission_payload)
            command = mission["command"]
            handler = getattr(self, f"handle_{command}", None)

            if handler and asyncio.iscoroutinefunction(handler):
                logger.info(f"[{self.agent_name}] Executing command: {command}")
                result = await handler(mission)
                logger.info(f"[{self.agent_name}] Command '{command}' completed")
                return {"status": "success", "result": result}
            else:
                logger.warning(f"[{self.agent_name}] Unknown command: {command}")
                return {"status": "error", "message": f"Unknown command: {command}"}

        except Exception as e:
            logger.exception(f"[{self.agent_name}] Mission execution failed")
            return {"status": "error", "message": str(e)}

    # --- Example command handlers below ---

    async def handle_echo(self, mission: dict) -> dict:
        """
        Simple test command: echo input.
        """
        message = mission.get("message", "No message provided.")
        return {"echo": message}

    async def handle_scan_memory(self, mission: dict) -> dict:
        """
        Stub: Pretend to scan memory pool.
        """
        await asyncio.sleep(1)
        return {"memory_scan": "completed", "items_found": 0}

    async def handle_simulate_trace(self, mission: dict) -> dict:
        """
        Stub: Simulate trace logic.
        """
        await asyncio.sleep(2)
        return {"trace_simulation": "ok", "path": [0, 1, 2]}
