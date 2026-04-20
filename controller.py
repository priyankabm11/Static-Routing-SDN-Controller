from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected")

    msg1 = of.ofp_flow_mod()
    msg1.match.in_port = 1
    msg1.actions.append(of.ofp_action_output(port=2))
    event.connection.send(msg1)

    msg2 = of.ofp_flow_mod()
    msg2.match.in_port = 2
    msg2.actions.append(of.ofp_action_output(port=1))
    event.connection.send(msg2)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    log.info("Static Routing Controller Running")
