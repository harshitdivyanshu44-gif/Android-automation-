from utils.logging import setup_logging
from utils.device import device_config
from agent import NLAgent

def bootstrap():
    logger = setup_logging()
    cfg = device_config()
    agent = NLAgent(cfg)
    return agent

if __name__ == "__main__":
    agent = bootstrap()
    agent.run("Open YouTube, search 'lofi hip hop', play the first result for 30 seconds, then pause.")
    agent.run("Open Gmail app draft the mail to someone regarding some subject and send it.")
