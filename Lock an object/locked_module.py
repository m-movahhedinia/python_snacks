"""
It happens sometimes that you have an object which must not change after it is created. I remember having a config
module which had to be kept constant all over the code after it was instantiated. However, since multiple people were
developing the code, it was not possible to tell everyone not to add any more attributes or change the current
attributes of the object. Therefore, I cam up with the idea to lock the object, but also give the developers the chance
to unlock it in extreme cases. The source of this idea come from a post on Stack Overflow and person who had posted it
referenced a page on Github. I have modified the code pretty much to have it fit my needs but I wanted to reference the
person who came up with the idea as well. Unfortunately, I don't have the link of those two anymore. Nevertheless,
kudos to the first person who came up with this.

Check the test_locked_module.py file for usage.
"""

from logging import getLogger
from typing import NoReturn, Any

logger = getLogger()


class ConfigureBuild:
    """
    Lets say this is the class that when instantiated, has to remain constant all over the code. What we want to do is
    to intercept any incoming changes and block them. However, also want to let changes to be applied in specific
    situations. For this purpose, we override the __setattr__ method and block all changes unless the locked attribute
    is set to False. By default, an instance of this class will be locked unless explicitly unlocked.
    """

    def __setattr__(self, attr: str, value: Any):
        """
        Should set the attributes of an instance of the :class:`ConfigureBuild` class. But it is overridden to avoid
        doing so if the locked attribute is set to True. By default, locked is set to True.

        :param str attr: Attribute name.
        :param Any value: The value of the attribute.
        """
        if self.__dict__.get("locked", False) and attr != "locked":
            logger.critical("This object is locked. The values of the attributes cannot be modified and "
                            "new attributes cannot be added. You can unlock it by setting its \"locked\" attribute to "
                            "False.")
        elif self.__dict__.get("locked", False) and value is False:
            logger.warning("Object unlocked. The values of the attributes of this object are not secure anymore.")
            self.__dict__[attr] = value
        else:
            self.__dict__[attr] = value

    def __init__(self, config_file: str):
        """
        Performs all the operations needed in one go and before locking the instance.

        :param str config_file: The path to the file containing the configurations for the build.
        """
        self.config_file = config_file
        self.state: str = None
        self.dummy_attribute = "The dummy attribute has the default value."

        # If there are any operations that need to be done must be done before locking the instance. If they are done
        # after and they need to assign any values to the attributes, they will fail.
        self._read_configs()

        # The locked attribute must be the last attribute. If it is not it will lock the instance in the middle of
        # instantiating it.
        self.locked: bool = True

    # If you want to add
    def _read_configs(self) -> NoReturn:
        """
        Reads the config file and sets the state attribute.

        :return: None
        """
        with open(self.config_file, encoding="utf-8") as file:
            # Read the file and do whatever you want to do with it.
            self.state = "We read the config file and pretended that we did whatever we wanted to do with it."
