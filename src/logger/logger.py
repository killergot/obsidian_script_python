import logging


def init_log(level: int):
    logging.basicConfig(
            level=level,  #(DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
                   '%(lineno)d - %(name)s - %(message)s',
            handlers=[
                logging.FileHandler("app.log"),
                logging.StreamHandler()
            ]
        )
