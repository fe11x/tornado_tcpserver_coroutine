from puller import logger
from puller.core import Puller
from tornado import ioloop


def main():
    puller = Puller()
    puller.listen(8777)
    logger.info('Starting Puller instance......')
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

