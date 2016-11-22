from scoring_engine.engine.basic_check import BasicCheck
import random


class DNSCheck(BasicCheck):
    name = 'DNS IPv4 Check'
    protocol = 'dns'
    version = 'ipv4'
    PROP_QTYPE = 'qtype'
    PROP_DOMAIN = 'domain'
    CMD = 'dig @{0} -t {1} -q {2}'

    def command(self):
        ip = self.get_ip_address()
        dns_environments = self.environments()
        if len(dns_environments) == 0:
            raise LookupError('DNS Environments are length 0')
        dns_environment = random.choice(dns_environments)
        dig_args = self.get_property_tuple(dns_environment)
        cmd = self.CMD.format(*dig_args)
        return cmd

    def get_property_tuple(self, dns_environment):
        """
        Given a dns_environment, extract the qtype and domain property
        Returns a tuple of ip,qtype,domain for dig command
        """
        ip = self.get_ip_address()
        if len(dns_environment.properties) != 2:
            raise LookupError('Not enough DNS Environment Properties to issue query')
        qtype = [prop.value for prop in dns_environment.properties if prop.name == self.PROP_QTYPE][0]
        domain = [prop.value for prop in dns_environment.properties if prop.name == self.PROP_DOMAIN][0]
        return (ip, qtype, domain)