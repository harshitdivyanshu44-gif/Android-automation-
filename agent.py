from loguru import logger
from actions.flows import Flows
from actions.ui import UI

class NLAgent:
    def __init__(self, cfg):
        self.cfg = cfg
        self.driver = self._connect_device(cfg)
        self.ui = UI(self.driver)
        self.flows = Flows(self.ui)

    def _connect_device(self, cfg):
        logger.info(f"Connecting to device: {cfg['adb_serial'] or cfg['mrc_device_id']}")
        return MockDriver()  # Replace with DroidRun/MRC driver

    def run(self, instruction: str):
        logger.info(f"Instruction: {instruction}")
        if "youtube" in instruction.lower():
            self.flows.youtube_search_and_play("lofi hip hop", 30)
        elif "wifi" in instruction.lower():
            self.flows.enable_wifi_and_connect("Home_5G")
        else:
            logger.warning("Unknown instruction")

class MockDriver:
    def launch_app(self, package): pass
    def wait_idle(self): pass
    def find(self, **kwargs): return MockNode()
    def press_enter(self): pass
    def sleep(self, seconds): pass

class MockNode:
    def click(self): pass
    def clear(self): pass
    def send_text(self, t): pass
    def is_checked(self): return False
    def find_child(self, **kwargs): return MockNode()
