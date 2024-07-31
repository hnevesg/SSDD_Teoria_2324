import sys
import Ice
Ice.loadSlice('cristian.ice')
import ssdd
import time

class Client(Ice.Application):
    def run(self, argv):
        proxy1 = self.communicator().stringToProxy("Cristian -t -e 1.1:tcp -h 93.189.90.58 -p 4000 -t 60000")
        proxy2 = self.communicator().stringToProxy("SyncReport -t -e 1.1:tcp -h 93.189.90.58 -p 4000 -t 60000")

        time1 = ssdd.CristianPrx.checkedCast(proxy1)
        time2 = ssdd.SyncReportPrx.checkedCast(proxy2)

        if not time1 or not time2:
            sys.exit(1)

        t1 = time.time()
        server_time = time1.getServerTime("12345678Z", t1)

        t2 = time.time() 
        new_time = server_time + (t2-t1)/2
        error = (t2-t1)/2
        time2.notifyTime("12345678Z", "Nombre Apellido", t2, new_time, error)

        return 0

sys.exit(Client().main(sys.argv))