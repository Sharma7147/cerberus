import argparse
import sys
from .core import generate_passwords
from .banners import banner

DEFAULT_SEPARATORS = ["", "@", "_", "-", ".", "$"]

def interactive_mode():
    try:
        banner()
        usernames = input("Enter usernames (comma separated, optional): ").split(",")
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        emails = input("Emails (comma separated, optional): ").split(",")
        dob = input("DOB (YYYY-MM-DD, optional): ").strip()
        pets = input("Pet names (comma separated, optional): ").split(",")
        numbers = input("Numbers (comma separated, optional): ").split(",")

        print("\nSelect preset size:")
        print("1) Small (~1k)  2) Medium (~5k)  3) Large (~20k)  4) Custom")
        choice = input("Choice: ").strip()
        if choice == "1":
            limit = 1000
        elif choice == "2":
            limit = 5000
        elif choice == "3":
            limit = 20000
        else:
            try:
                limit = int(input("Enter custom limit (500–50000): "))
                if not (500 <= limit <= 50000):
                    raise ValueError("Limit must be between 500 and 50000.")
            except ValueError as e:
                print(f"[!] Invalid limit: {e}")
                return

        # Options
        breached = input("Include top breached passwords? [y/N]: ").strip().lower().startswith("y")
        try:
            min_len = int(input("Minimum password length (default 6): ") or 6)
            max_len = int(input("Maximum password length (default 24): ") or 24)
            if min_len < 1 or max_len < 1 or min_len > max_len:
                raise ValueError("Invalid min/max length values.")
        except ValueError as e:
            print(f"[!] Error: {e}")
            return

        use_leet = input("Enable leetspeak? [y/N]: ").strip().lower().startswith("y")
        reversals = input("Include reversals? [y/N]: ").strip().lower().startswith("y")
        need_digit = input("Require digit? [y/N]: ").strip().lower().startswith("y")
        need_symbol = input("Require symbol? [y/N]: ").strip().lower().startswith("y")
        need_upper = input("Require uppercase? [y/N]: ").strip().lower().startswith("y")
        need_lower = input("Require lowercase? [y/N]: ").strip().lower().startswith("y")

        pwds = generate_passwords(
            first, last, usernames, emails, pets, numbers, dob,
            limit=limit,
            min_len=min_len,
            max_len=max_len,
            breached=breached,
            use_leet=use_leet,
            reversals=reversals,
            need_digit=need_digit,
            need_symbol=need_symbol,
            need_upper=need_upper,
            need_lower=need_lower,
            separators=DEFAULT_SEPARATORS
        )

        out_file = f"{first.lower() or 'wordlist'}.txt"
        try:
            with open(out_file, "w") as f:
                f.write("\n".join(pwds))
            print(f"[+] Generated {len(pwds)} entries → {out_file}")
        except OSError as e:
            print(f"[!] Failed to write file: {e}")

    except KeyboardInterrupt:
        print("\n[!] Aborted by user.")


def cli():
    parser = argparse.ArgumentParser(description="CERBERUS – Advanced Password Profiler")
    parser.add_argument("--first", default="", help="First name")
    parser.add_argument("--last", default="", help="Last name")
    parser.add_argument("--usernames", nargs="*", default=[])
    parser.add_argument("--emails", nargs="*", default=[])
    parser.add_argument("--pets", nargs="*", default=[])
    parser.add_argument("--numbers", nargs="*", default=[])
    parser.add_argument("--dob", default="", help="DOB YYYY-MM-DD")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--min-len", type=int, default=6, help="Minimum password length")
    parser.add_argument("--max-len", type=int, default=24, help="Maximum password length")
    parser.add_argument("--breached", action="store_true", help="Include top breached passwords")
    parser.add_argument("--use-leet", action="store_true", help="Enable leetspeak variants")
    parser.add_argument("--reversals", action="store_true", help="Include reversed tokens")
    parser.add_argument("--need-digit", action="store_true", help="Require digit in password")
    parser.add_argument("--need-symbol", action="store_true", help="Require symbol in password")
    parser.add_argument("--need-upper", action="store_true", help="Require uppercase letter")
    parser.add_argument("--need-lower", action="store_true", help="Require lowercase letter")
    parser.add_argument("--output", help="Output filename (defaults to firstname.txt)")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    args = parser.parse_args()

    try:
        if args.min_len <= 0 or args.max_len <= 0 or args.min_len > args.max_len:
            raise ValueError("Invalid min/max length values.")
        if args.limit < 500 or args.limit > 50000:
            raise ValueError("Limit must be between 500 and 50000.")

        if args.interactive:
            interactive_mode()
        else:
            pwds = generate_passwords(
                args.first, args.last, args.usernames, args.emails, args.pets, args.numbers, args.dob,
                limit=args.limit,
                min_len=args.min_len,
                max_len=args.max_len,
                breached=args.breached,
                use_leet=args.use_leet,
                reversals=args.reversals,
                need_digit=args.need_digit,
                need_symbol=args.need_symbol,
                need_upper=args.need_upper,
                need_lower=args.need_lower,
                separators=DEFAULT_SEPARATORS
            )
            out_file = args.output or f"{args.first.lower() or 'wordlist'}.txt"
            try:
                with open(out_file, "w") as f:
                    f.write("\n".join(pwds))
                print(f"[+] Generated {len(pwds)} entries → {out_file}")
            except OSError as e:
                print(f"[!] Failed to write file: {e}")

    except ValueError as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Aborted by user.")
        sys.exit(1)
