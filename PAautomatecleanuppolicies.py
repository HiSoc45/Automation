import requests
import xml.etree.ElementTree as ET

# Set Panorama details
panorama_ip = "YOUR_PANORAMA_IP"
api_key = "YOUR_API_KEY"


# Function to retrieve all security policies from Panorama
def get_security_policies():
    api_url = f"https://{panorama_ip}/api/?type=config&action=get&xpath=/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='your_device_group']/pre-rulebase/security/rules"
    headers = {
        "Content-Type": "application/xml"
    }
    params = {
        "key": api_key
    }
    response = requests.get(api_url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    return response.content


# Function to retrieve the list of used security policy names from Panorama logs
def get_used_policies():
    api_url = f"https://{panorama_ip}/api/?type=log&log-type=threat&query=(SELECT%20action%20FROM%20threat%20WHERE%20action%20contains%20%27allow%27)%20|%20table%20rule"
    headers = {
        "Content-Type": "application/xml"
    }
    params = {
        "key": api_key
    }
    response = requests.get(api_url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    used_policies = [entry.text for entry in root.findall(".//entry")]
    return used_policies


# Function to delete unused security policies from Panorama
def delete_unused_policies(unused_policies):
    for policy in unused_policies:
        api_url = f"https://{panorama_ip}/api/?type=config&action=delete&xpath=/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='your_device_group']/pre-rulebase/security/rules/entry[@name='{policy}']"
        headers = {
            "Content-Type": "application/xml"
        }
        params = {
            "key": api_key
        }
        response = requests.post(api_url, headers=headers, params=params, verify=False)
        response.raise_for_status()
        print(f"Deleted policy: {policy}")


# Main script execution
try:
    # Get all security policies from Panorama
    all_policies = get_security_policies()

    # Get the list of used security policy names from Panorama logs
    used_policies = get_used_policies()

    # Find unused security policies
    unused_policies = [policy for policy in all_policies if policy not in used_policies]

    # Delete unused security policies
    if len(unused_policies) > 0:
        delete_unused_policies(unused_policies)
    else:
        print("No unused security policies found.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
