# Static-Routing-SDN-Controller
POX-based Static Routing using SDN Controller in Mininet with OpenFlow flow rules.

## Project Overview
Static-Routing-SDN-Controller is a Software Defined Networking (SDN) project developed using the POX controller, Mininet emulator, and OpenFlow switches. The objective of this project is to implement static routing paths between hosts by manually installing flow rules through the SDN controller.

Unlike traditional networks where routing decisions are taken by routers individually, SDN separates the control plane from the data plane. The controller centrally manages the network and decides how packets should travel through switches.

In this project, the controller predefines fixed paths (static routes) and installs corresponding flow entries in Open vSwitch switches to ensure packet forwarding between hosts.

---

## Objective
- Design a simple SDN network topology in Mininet.
- Implement static routing using controller-installed flow rules.
- Verify connectivity between hosts.
- Observe flow entries in switches.
- Demonstrate centralized network control using SDN.

---

## Technologies Used
- Ubuntu Linux
- Python
- POX Controller
- Mininet
- Open vSwitch
- OpenFlow Protocol

---

## Network Topology
A linear topology with:

- 2 Hosts (`h1`, `h2`)
- 2 Switches (`s1`, `s2`)

Connection Path:

h1 ↔ s1 ↔ s2 ↔ h2

---

## Working Principle
1. Mininet creates the virtual network topology.
2. POX controller connects to switches.
3. When switches join the controller, flow rules are installed manually.
4. Packets from `h1` to `h2` and `h2` to `h1` follow predefined static paths.
5. Connectivity is tested using `pingall`.

---

## Commands Used

```bash
sudo mn --topo linear,2 --controller remote
pingall
sh ovs-vsctl show
sh ovs-ofctl dump-flows s1
sh ovs-ofctl dump-flows s2
