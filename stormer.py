from colorama import Fore
from others import *
import requests
import argparse

def parser():  # argparser setup
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q", "--quiet",
        action="store_false",
        required=False,
        help="does not display all on going tests"
    )
    parser.add_argument(
        "-s", "--save",
        action="store_true",
        required=False,
        help="when activated, flags code to save vulnerable urls in a .txt file"
    )
    parser.add_argument(
        "-l", "--level",
        type=int,
        required=False,
        help="amount of payloads that are going to be tested"
    )

    return parser.parse_args()

args = parser()
# end of argparser setup

targetfile = input("path for target file: ")
targets = open(f"{targetfile}", "r+")
vulnerabilities_found = 0

if args.level == 1:  # argparser payload setup
    payloads = payloads
elif args.level == 2:
    payloads = payloads2
elif args.level == 3:
    payloads = payloads3
else:
    print("[/]level not flagged or invalid level, stormer only supports level 1-3, using default(1) instead.")
    payloads = payloads

# tests for sqli
for target in targets:
    target = target.strip()
    skip_not_found = False
    vulnerability_found = False

    for payload in payloads:
        try:
            response = requests.post(f"{target}{payload}")
            for sqli_error in sqli_errors:
                if sqli_error in response.text.lower():
                    print(Fore.GREEN + f"[+]vulnerability found in {target} with payload: {payload}" + Fore.RESET)
                    vulnerabilities_found += 1
                    vulnerability_found = True
                    if args.save:
                        with open(f"{targetfile}.txt", "a") as file_create:
                            file_create.writelines(f"{target}\n")
                    break

            if vulnerability_found:
                break

            for error in errors:
                if error.lower() in response.text.lower():
                    if args.quiet:
                        print(Fore.YELLOW + f"error {error} while handling connection to url: {target}" + Fore.RESET)
                        skip_not_found = True
                    break

            if skip_not_found:
                break

        except ConnectionResetError:
            print(f"[-] connection error in url: {target}, skipping")
            continue
        except KeyboardInterrupt:
            print("program stopped manually")
            print(f"[!]{vulnerabilities_found} vulnerabilities found")
            exit()
        except requests.exceptions.InvalidSchema:
            if args.quiet:
                print(Fore.YELLOW + f"[/]invalid url: {target}, skipping" + Fore.RESET)
            break

    if not vulnerability_found and not skip_not_found and args.quiet:
        print(Fore.RED + f"vulnerability not found in url: {target}" + Fore.RESET)

print(f"[!]{vulnerabilities_found} vulnerabilities found")
if vulnerability_found and args.save:
    print(f"vulnerable urls can be found in {targetfile}.txt")
targets.close()