import shutil
from typing import Tuple

UNIT_KiB = 1_024
UNIT_MiB = 1_048_576
UNIT_GiB = 1_073_741_824
UNIT_TiB = 1_099_511_627_776


def get_fs_metrics(sample_path: str = __file__,
                   unit: int = UNIT_GiB
                   ) -> Tuple[float, float, float]:
    ''' Get disk usage metrics.

    Args:
        sample_path(str): Path or file contained on file system.
        unit(int): Unit bytes should be converted to.

    Returns:
        The total, used, and free disk space.
    '''
    total, used, free = shutil.disk_usage(sample_path)
    total /= unit
    used /= unit
    free /= unit
    return total, used, free


def get_fs_percent_used(unit: int = UNIT_GiB) -> float:
    ''' Get percentage of disk that has been used.

    Args:
        unit(int): Unit bytes should be converted to.

    Returns:
        The percentage of disk space currently used.
    '''
    total, used, _ = get_fs_metrics(unit=unit)
    return used / total


if __name__ == "__main__":
    print(get_fs_metrics())
