"""
This module is just testing the :class:`ConfigureBuild` class from locked_module.
"""

from logging import getLogger, basicConfig, INFO

from locked_module import ConfigureBuild

logger = getLogger()
basicConfig(format='%(levelname)s: %(message)s', level=INFO)

configs = ConfigureBuild("configs.txt")
logger.info(configs.state)
logger.info(f"First check: the object is {'locked' if configs.locked else 'unlocked'}")
logger.info(f"First check: {configs.dummy_attribute}")

configs.dummy_attribute = "The dummy attribute does not have the default value anymore."

logger.info(f"Second check: the object is {'locked' if configs.locked else 'unlocked'}")
logger.info(f"Second check: {configs.dummy_attribute}")

configs.locked = False
configs.dummy_attribute = "The dummy attribute does not have the default value anymore."

logger.info(f"Third check: the object is {'locked' if configs.locked else 'unlocked'}")
logger.info(f"Third check: {configs.dummy_attribute}")

configs.locked = True

logger.info(f"Fourth check: the object is {'locked' if configs.locked else 'unlocked'}")
logger.info(f"Fourth check: {configs.dummy_attribute}")

configs.dummy_attribute = "Trying to change the dummy attribute again."

configs.added_dummy_attribute = "This attribute is added to the instance."

try:
    logger.info(configs.added_dummy_attribute)
except AttributeError as e:
    logger.error(e)

configs.locked = False
configs.added_dummy_attribute = "This attribute is added to the instance."

logger.info(configs.added_dummy_attribute)

configs.locked = True
