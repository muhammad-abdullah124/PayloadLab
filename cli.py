import argparse
from modules import xss, sqli, cmdi
from modules.encoder import encode_payload
from modules.mutator import mutate_payload
from modules.burp import send_to_burp


def main():
    parser = argparse.ArgumentParser(
        prog="PayloadForge",
        description="🔧 PayloadForge — Advanced Web Exploitation Payload Generator",
        epilog="""Example:\n  python3 main.py --xss --mode waf --encode url --count 5""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--xss", action="store_true", help="🔹 Include XSS payloads")
    parser.add_argument("--sqli", action="store_true", help="🔹 Include SQLi payloads")
    parser.add_argument("--cmdi", action="store_true", help="🔹 Include Command Injection payloads")

    parser.add_argument("--count", type=int, default=5, help="🔢 Number of payloads to generate (default: 5)")
    parser.add_argument("--filter", nargs='+', help="🔍 Filter payloads containing keywords (e.g., alert admin)")

    parser.add_argument("--mode", choices=["default", "stealth", "brute", "waf"], default="default",
                        help="🛡️ Payload mutation mode for WAF evasion:\n  default = no mutation\n  stealth = space escaping\n  brute   = append junk to bypass\n  waf     = insert inline comments")

    parser.add_argument("--encode", choices=["url", "base64", "unicode", "hex"],
                        help="🔐 Apply encoding to payloads")

    parser.add_argument("--burp", metavar="URL",
                        help="🌐 Send payloads to endpoint via GET for testing (e.g., http://localhost:8080/test)")

    args = parser.parse_args()
    payloads = []

    if args.xss:
        payloads.extend(xss.get_random_xss(args.count, args.filter))
    if args.sqli:
        payloads.extend(sqli.get_random_sqli(args.count, args.filter))
    if args.cmdi:
        payloads.extend(cmdi.get_random_cmdi(args.count, args.filter))

    if not payloads:
        print("[!] No payloads found.")
        return

    print(f"\n[+] Generated {len(payloads)} Payloads:\n")

    for idx, p in enumerate(payloads, 1):
        original = p["payload"]
        mutated = mutate_payload(original, mode=args.mode)
        encoded = encode_payload(mutated, args.encode) if args.encode else mutated

        print(f"[{idx}] Type: {p.get('category')} | Source: {p.get('source_file')}")
        print(f"Original: {original}")
        print(f"Mutated : {mutated}")
        print(f"Encoded : {encoded}")

        if args.burp:
            result = send_to_burp(encoded, args.burp)
            if 'error' in result:
                print(f"[BURP] Error: {result['error']}")
            else:
                print(f"[BURP] URL: {result['url']} | Status: {result['status_code']} | Size: {result['length']}")
        print("-" * 50)

