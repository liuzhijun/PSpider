# _*_ coding: utf-8 _*_

"""
threads_inst_proxies.py by xianhu
"""

import time
import logging
from .threads_inst_base import TPEnum, BaseThread


class ProxiesThread(BaseThread):
    """
    class of ProxiesThread, as the subclass of BaseThread
    """

    def working(self):
        """
        procedure of proxies, auto running, and return False if you need stop thread
        """
        # ----2----
        proxies_result, proxies_list = self._worker.working()

        # ----3----
        if proxies_result > 0:
            for proxies in proxies_list:
                self._pool.add_a_task(TPEnum.PROXIES, proxies)

        # ----5----
        while (self._pool.get_number_dict(TPEnum.PROXIES_LEFT) > 100) and (not self._pool.is_all_tasks_done()):
            logging.debug("%s[%s] sleep 5 seconds because of too many 'PROXIES_LEFT' ...", self.__class__.__name__, self.getName())
            time.sleep(5)
        return True if not self._pool.is_all_tasks_done() else False
