from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

hosts = {}
TIMEOUT = 60

def print_hosts():
    log.info("----- Current Host Table -----")
    for mac in hosts:
        h = hosts[mac]
        log.info("MAC: %s | Switch: %s | Port: %s", mac, h["dpid"], h["port"])

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    mac = str(packet.src)
    dpid = event.connection.dpid
    port = event.port
    now = time.time()

    if mac not in hosts:
        hosts[mac] = {
            "dpid": dpid,
            "port": port,
            "last_seen": now
        }
        log.info("Host JOIN → MAC: %s | Switch: %s | Port: %s", mac, dpid, port)
        print_hosts()
    else:
        hosts[mac]["last_seen"] = now

def cleanup():
    now = time.time()
    for mac in list(hosts.keys()):
        if now - hosts[mac]["last_seen"] > TIMEOUT:
            log.info("Host LEFT: %s", mac)
            del hosts[mac]

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

    import threading
    def timer():
        while True:
            cleanup()
            time.sleep(10)

    threading.Thread(target=timer).start()
    log.info("Host Discovery Module Loaded")