# ActivitySim
# See full license in LICENSE.txt.

import logging

import numpy as np
import pandas as pd

from activitysim.core.util import reindex
from activitysim.core import inject

logger = logging.getLogger(__name__)


@inject.table()
def tours_merged(tours, persons_merged):
    return inject.merge_tables(tours.name, tables=[
        tours, persons_merged])


inject.broadcast('persons_merged', 'tours', cast_index=True, onto_on='person_id')
