from abc import ABCMeta, abstractmethod
from ..utils import SubclassesMixin
from ..logger import logger


class MetadataBackend(SubclassesMixin, metaclass=ABCMeta):

    @classmethod
    def get_backend(cls, metadata_backend="default"):
        subclasses_dict = cls._get_subclasses_dict("metadata_backend")
        if metadata_backend not in subclasses_dict:
            raise NotImplementedError(
                "API Metadata Backend not implemented"
            )
        logger.info("API metadata backend: {}".format(
            subclasses_dict[metadata_backend]
        ))

        return subclasses_dict[metadata_backend]()

    @staticmethod
    @abstractmethod
    def store_alternative_route():
        """Store alternative route.

        This should store the url and also the time when it was stored.
        """
        pass

    @staticmethod
    @abstractmethod
    def try_original_url():
        """Determine if next api call should use the original URL or not."""
        pass

    @staticmethod
    @abstractmethod
    def get_alternative_url():
        """Get stored URL."""
        pass