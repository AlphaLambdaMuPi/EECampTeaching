#! /usr/bin/env python3

import asyncio
import logging
# import matplotlib.pyplot as plt
import numpy as np

from .num_model import Drone

from controller import Controller

logger = logging.getLogger()

np.set_printoptions(precision=10, suppress=True)

class Simulator(object):
    def __init__(self):
        self._drone = Drone()
        self._controller = Controller(self._drone, log=True)
        self._loop = asyncio.get_event_loop()
        self._drone.set_init([0., 0., 0.], [0., 0., 1.])
        self.started = asyncio.Future()
        # self._AOO = []
        # self._drone.dt = 5e-4
        # self._drone.noise_z = 1e-10

    @asyncio.coroutine
    def run(self):
        logger.info('starting simulation...')
        yield from self._controller.arm()
        self._loop.call_soon_threadsafe(
            self._loop.create_task,
            self._controller.run()
        )
        self.started.set_result(True)
        logger.info('started.')

    @asyncio.coroutine
    def get_data(self):
        pos = self._drone.get_position()
        ori = self._drone.rot
        # oori = ori[:, 2]
        # self._AOO.append(self._drone.acc_sensor[2])
        # self._AOO.append(oori)
        return pos, ori

    @asyncio.coroutine
    def stop(self):
        yield from self._controller.stop()
        yield from self._drone.stop()
        # logger.debug('plotting...')
        # plt.plot(self._AOO)
        # plt.show()
