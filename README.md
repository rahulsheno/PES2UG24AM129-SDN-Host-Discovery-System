# Host Discovery in SDN using POX

## 📌 Overview

This project implements a host discovery service in an SDN environment using the POX controller. It detects hosts dynamically and maintains their information in real time.

---

## 🎯 Objective

* Detect host join events
* Maintain host database
* Display host details
* Update dynamically

---

## 🛠️ Requirements

* Ubuntu
* Python 2.7
* POX Controller
* Mininet
* Open vSwitch

---

## ⚙️ Installation

### Install dependencies

```
sudo apt update
sudo apt install git mininet openvswitch-switch build-essential wget -y
```

### Install Python 2

```
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
tar -xvf Python-2.7.18.tgz
cd Python-2.7.18
./configure
make -j4
sudo make install
```

### Install POX

```
cd ~
git clone https://github.com/noxrepo/pox.git
cd pox
git checkout dart
```

## 🚀 Run the Project

### Start POX

```
cd ~/pox
python2 pox.py openflow.of_01 misc.host_discovery log.level --DEBUG
```

### Start Mininet

```
sudo mn -c
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633
```

### Test

```
pingall
```

---

## 🔍 How It Works

* Host sends packet
* Switch sends PacketIn to controller
* Controller extracts MAC, switch ID, and port
* New host is added to database
* Existing host is updated
* Inactive hosts are removed

---

## 📊 Host Data Structure

```
hosts = {
    MAC: {
        "dpid": switch_id,
        "port": port_number,
        "last_seen": timestamp
    }
}
```

---

## 🏁 Result

* Hosts are detected automatically
* Host information is stored and updated dynamically
* Network state is maintained in real time
