# Static Routing using SDN Controller using POX and Mininet

## 1. Introduction

Software Defined Networking (SDN) is a modern networking architecture where the control plane is separated from the data plane. Instead of configuring each network device manually, a centralized controller manages traffic flow intelligently.

In this project, a POX controller is used with Mininet to implement static routing. The controller installs fixed OpenFlow rules in switches so that packets always follow a predefined path.

---

## 2. Problem Statement

Implement static routing paths using controller-installed OpenFlow flow rules in a Software Defined Network using Mininet topology and POX controller.

The routing path should remain fixed and communication between hosts must be verified successfully.

---

## 3. Objective

The objectives of this project are:

- To understand the concept of SDN.
- To create a virtual network using Mininet.
- To use POX controller for managing switches.
- To install static flow rules manually.
- To verify communication between hosts.
- To display switch flow tables.

---

## 4. Technologies Used

| Tool | Purpose |
|------|---------|
| Ubuntu | Operating System |
| Mininet | Network emulator |
| POX Controller | SDN Controller |
| OpenFlow | Communication protocol |
| Open vSwitch | Virtual switch |

---

## 5. Network Topology Used

A linear topology with 2 hosts and 2 switches was used.

```text id="h9wxoa"
h1 ---- s1 ---- s2 ---- h2
