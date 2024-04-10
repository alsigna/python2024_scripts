from textwrap import dedent

# fmt: off
s1 = 'hello'
# fmt: on

s2 = "some text"

s3 = """
interface Tunnel2
  description {{ interfaces.tunnel.1.description }}
  ip address {{ interfaces.tunnel.1.ip }} {{ interfaces.tunnel.1.mask }}
  ip nhrp network-id {{ interfaces.tunnel.1.network_id }}
  ip nhrp nhs {{ dmvpn.hub.main.ip  }} nbma {{ dmvpn.hub.main.nbma }}
  ip nhrp registration no-unique
"""


def get_config1():
    config = """
      interface Tunnel2
        description {{ interfaces.tunnel.1.description }}
        ip address {{ interfaces.tunnel.1.ip }} {{ interfaces.tunnel.1.mask }}
        ip nhrp network-id {{ interfaces.tunnel.1.network_id }}
        ip nhrp nhs {{ dmvpn.hub.main.ip  }} nbma {{ dmvpn.hub.main.nbma }}
        ip nhrp registration no-unique
    """
    return config


def get_config2():
    config = (
        "interface Tunnel2\n"
        "  description {{ interfaces.tunnel.1.description }}\n"
        "  ip address {{ interfaces.tunnel.1.ip }} {{ interfaces.tunnel.1.mask }}\n"
        "  ip nhrp network-id {{ interfaces.tunnel.1.network_id }}\n"
    )
    return config


def get_config3():
    config = dedent(
        """
        interface Tunnel2
          description {{ interfaces.tunnel.1.description }}
          ip address {{ interfaces.tunnel.1.ip }} {{ interfaces.tunnel.1.mask }}
          ip nhrp network-id {{ interfaces.tunnel.1.network_id }}
        """
    )
    return config


s4 = get_config2()

from textwrap import dedent

s5 = dedent(
    """
    interface Tunnel2
        description {{ interfaces.tunnel.1.description }}
        ip address {{ interfaces.tunnel.1.ip }} {{ interfaces.tunnel.1.mask }}
        ip nhrp network-id {{ interfaces.tunnel.1.network_id }}
    """
)
