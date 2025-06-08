# Firewall Ansible Automation

## Introduction

This repository provides an automated solution for managing firewall configurations using Ansible. It allows administrators to deploy, manage, and maintain consistent firewall rules and settings across multiple Linux-based hosts, utilizing Ansible's powerful automation capabilities.

### Repository Structure

* `generate.sh`: Helper script for initiating configuration.
* `ansible-firewall/`: Directory containing Ansible playbooks and roles.

  * `bootstrap.yml`: Initializes the environment and installs necessary prerequisites.
  * `site.yml`: Main playbook to apply firewall configurations.
  * `diag_firewall.sh`: Script for diagnosing firewall settings and issues.
  * `group_vars/`: Contains group-specific variables.
  * `inventory/hosts`: Inventory file listing managed hosts.
  * `roles/firewall`: Role for firewall-specific tasks and configurations.

## Requirements

* Ansible (ensure it is installed and accessible on your system).
* SSH access to target firewall hosts.

## Usage

1. Clone the repository:

```bash
git clone <repository_url>
cd ansible-firewall
```

2. Install required Ansible roles and dependencies:

```bash
ansible-galaxy install -r requirements.yml
```

3. Edit inventory file (`inventory/hosts`) to match your environment.

4. Modify variables in `group_vars/` to fit your specific firewall requirements.

5. Run the main playbook to deploy configurations:

```bash
ansible-playbook -i inventory/hosts site.yml
```

## Diagnostics

To diagnose firewall settings, use the provided script:

```bash
./diag_firewall.sh
```

## nDPI Setup

nDPI is installed automatically by the Ansible playbook. Ensure the
`ndpi` role is listed in `site.yml` and run the playbook against your
hosts:

```bash
ansible-playbook -i inventory/hosts site.yml
```

The role also deploys a small helper service that feeds nDPI flow
information into nftables ipsets. These ipsets are then referenced in the
nftables configuration to apply DSCP marks based on the detected
application traffic.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
