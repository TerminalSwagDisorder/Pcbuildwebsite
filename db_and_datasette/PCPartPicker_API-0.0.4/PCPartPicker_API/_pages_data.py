"""
Each row contains multiple columns and
the only way to know what the columns
text is, is by numbering them (as they
are always in the same order)
"""

lookup = {
    "cpu": {
        1: "cpu",
        2: "speed",
        3: "cores",
        4: "tdp",
        5: "rating",
        6: "price"
    },
    "cpu-cooler": {
        1: "cpu-cooler",
        4: "rating",
        5: "price"
    },
    "motherboard": {
        1: "motherboard",
        2: "socket",
        4: "ram-slots",
        6: "rating",
        7: "price"
    },
    "memory": {
        1: "ram"
        2: "speed",
        4: "cas",
        5: "modules",
        6: "size",
        8: "rating",
        9: "price"
    },
    "internal-hard-drive": {
        1: "storage",
        3: "form",
        4: "type",
        5: "capacity",
        8: "rating",
        9: "price"
    },
    "video-card": {
        1: "video-card",
        3: "chipset",
        4: "memory",
        6: "rating",
        7: "price"
    },
    "power-supply": {
        1: "power-supply",
        4: "efficiency",
        5: "watts",
        6: "modular",
        7: "rating",
        8: "price"
    },
    "case": {
        1: "case",
        2: "type",
        3: "ext525b",  # EXTERNAL 5.25" BAYS
        4: "int35b",   # INTERNAL 3.5" BAYS
        6: "rating",
        7: "price"
    },
    "case-fan": {
        1: "case-fan",
        3: "size",
        4: "rpm",
        7: "rating",
        8: "price"
    },
#    "thermal-paste": {
#        1: "thermal-compound",
#        2: "amount",
#        3: "rating",
#        4: "price"
#    },
    "wired-network-card": {
        3: "network-interface-card",
        2: "interface",
        3: "ports",
        4: "rating",
        5: "price"
    },
    "wireless-network-card": {
        6: "wireless-network-card",
        2: "interface",
        3: "protocols",
        4: "rating",
        5: "price"
    },
}
