import psycopg2_pool

class GeventConnectionPool(psycopg2_pool.PostgresConnectionPool):
    """
    The real work is done by the psycopg2_pool module written by Denis Bilenko
    (https://github.com/SiteSupport/gevent/blob/master/examples/psycopg2_pool.py).

    This class expose the common interface used by dbpool.
    """
    def __init__(self, minconn, maxconn, **conn_params):
        super(GeventConnectionPool, self).__init__(maxsize=maxconn, **conn_params)

    def getconn(self):
        return self.get()

    def putconn(self, item):
        self.put(item)

