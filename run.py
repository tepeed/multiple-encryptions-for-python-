import sys
import os
import subprocess
import base64
import marshal
import zlib
import lzma
import bz2
import binascii
import gzip
import pickle
import codecs
import aiofiles
import asyncio
import pyfiglet
from typing import Union
import tempfile
import shutil
from shutil import which
from colorama import init, Fore, Style
from tqdm import tqdm
from datetime import datetime
import time
import requests
import pytz
import glob

init(autoreset=True)
OUTPUT_DIR = "encode"


def get_local_time_from_ip():
    try:
        res = requests.get("https://ipapi.co/json/", timeout=5)
        data = res.json()
        tz_name = data.get("timezone", "UTC")
        timezone = pytz.timezone(tz_name)
        now = datetime.now(timezone)
        offset = now.strftime("%z")
        formatted_offset = f"UTC{offset[:3]}:{offset[3:]}"
        formatted_time = now.strftime("%d-%m-%y %H:%M") + " " + formatted_offset
        return tz_name, formatted_time
    except Exception:
        now = datetime.utcnow()
        return "UTC", now.strftime("%d-%m-%y %H:%M UTC+00:00")


def print_banner_with_timezone():
    tz_name, time_str = get_local_time_from_ip()
    print(Fore.WHITE + "------------------------------------------------------------")
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}({Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTWHITE_EX}) Author: " + Fore.LIGHTWHITE_EX + "tepeed")
    print(Fore.LIGHTMAGENTA_EX + f"{Fore.LIGHTWHITE_EX}({Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTWHITE_EX}) Timezone: " + Fore.LIGHTWHITE_EX + time_str)
    print(Fore.WHITE + "------------------------------------------------------------" + "\n")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """Display T ENCODER banner - compact version for all screens."""
    # Compact ASCII art for "T ENCODER" (fits mobile screens)
    banner_lines = [
        "████████╗███████╗███╗   ██╗ ██████╗ ██████╗ ███████╗██████╗ ",
        "╚══██╔══╝██╔════╝████╗  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗",
        "   ██║   █████╗  ██╔██╗ ██║██║   ██║██║  ██║█████╗  ██████╔╝",
        "   ██║   ██╔══╝  ██║╚██╗██║██║   ██║██║  ██║██╔══╝  ██╔══██╗",
        "   ██║   ███████╗██║ ╚████║╚██████╔╝██████╔╝███████╗██║  ██║",
        "   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝",
    ]

    # Simple purple color (works on all terminals)
    PURPLE = "[38;5;129m"  # Medium purple
    BRIGHT_PURPLE = "[38;5;141m"  # Light purple
    WHITE = "[38;5;255m"
    CYAN = "[38;5;51m"
    GREEN = "[38;5;82m"
    GRAY = "[38;5;245m"
    RESET = "[0m"

    # Print banner with simple purple gradient
    for i, line in enumerate(banner_lines):
        # Alternate between purple shades for subtle effect
        color = PURPLE if i % 2 == 0 else BRIGHT_PURPLE
        print(f"{color}{line}{RESET}")

    # Credits line - compact for small screens
    print()
    print(f"{CYAN}Developer: {WHITE}tepeed{CYAN} | Telegram: {WHITE}@wlzbi{CYAN} | GitHub: {WHITE}tepeed{CYAN} | {GREEN}ACTIVE{RESET}")
    print(f"{GRAY}{'-' * 55}{RESET}")


def check_pyarmor_version():
    try:
        result = subprocess.run(["pyarmor", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        return None
    except Exception:
        return None


def check_pyinstaller_installed():
    return which("pyinstaller") is not None


HEX_EMOJI_MAP = {
    "0": "😀", "1": "😁", "2": "😂", "3": "🤣",
    "4": "😃", "5": "😄", "6": "😅", "7": "😆",
    "8": "😉", "9": "😊", "a": "😋", "b": "😎",
    "c": "😍", "d": "😘", "e": "😗", "f": "😙",
}


def hex_to_emoji(hex_str):
    return "".join(HEX_EMOJI_MAP[ch] for ch in hex_str.lower())


def _progress():
    for _ in tqdm(range(50), desc="Processing", ncols=70,
                   bar_format="{l_bar}{bar}| {n_fmt}%"):
        time.sleep(0.01)


def encode_choice(choice, data):
    try:
        if choice == 1:
            for _ in tqdm(range(50), desc="Processing", ncols=70,
                           bar_format="{l_bar}{bar}| {n_fmt}%"):
                time.sleep(0.01)
            return codecs.encode(data, "rot_13"), "rot13"

        if choice == 2:
            for _ in tqdm(range(50), desc="Processing", ncols=70,
                           bar_format="{l_bar}{bar}| {n_fmt}%"):
                time.sleep(0.01)
            return zlib.compress(data.encode()).hex(), "zlib"

        if choice == 3:
            for _ in tqdm(range(50), desc="Processing", ncols=70,
                           bar_format="{l_bar}{bar}| {n_fmt}%"):
                time.sleep(0.01)
            return gzip.compress(data.encode()).hex(), "gzip"

        if choice == 4:
            for _ in tqdm(range(50), desc="Processing", ncols=70,
                           bar_format="{l_bar}{bar}| {n_fmt}%"):
                time.sleep(0.01)
            code_obj = compile(data, "<string>", "exec")
            pyc_bytes = marshal.dumps(code_obj)
            return hex_to_emoji(pyc_bytes.hex()), "pyc_emoji"

        if choice == 5:
            _progress()
            return base64.a85encode(data.encode()).decode(), "base85"

        if choice == 6:
            _progress()
            return base64.b16encode(data.encode()).decode(), "base16"

        if choice == 7:
            _progress()
            return base64.b64encode(data.encode()).decode(), "base64"

        if choice == 8:
            _progress()
            return base64.b32encode(data.encode()).decode(), "base32"

        if choice == 9:
            for _ in tqdm(range(50), desc="Processing", ncols=70,
                           bar_format="{l_bar}{bar}| {n_fmt}%"):
                time.sleep(0.01)
            key = 23
            b = bytes([b ^ key for b in data.encode()])
            xored = b
            return base64.b64encode(xored).decode(), "xor_base64"

        if choice == 10:
            _progress()
            return gzip.compress(marshal.dumps(data.encode())).hex(), "marshal_gzip"

        if choice == 11:
            _progress()
            return zlib.compress(marshal.dumps(data.encode())).hex(), "marshal_zlib"

        if choice == 12:
            _progress()
            return base64.b16encode(marshal.dumps(data.encode())).decode(), "marshal_base16"

        if choice == 13:
            _progress()
            return base64.b64encode(marshal.dumps(data.encode())).decode(), "marshal_base64"

        if choice == 14:
            _progress()
            return base64.a85encode(marshal.dumps(data.encode())).decode(), "marshal_base85"

        if choice == 15:
            _progress()
            return base64.b64encode(pickle.dumps(data.encode())).decode(), "pickle_base64"

        if choice == 16:
            _progress()
            return binascii.b2a_hex(base64.b32encode(data.encode())).decode(), "base32_binascii"

        if choice == 17:
            _progress()
            return base64.b64encode(lzma.compress(marshal.dumps(data.encode()))).decode(), "marshal_lzma_base64"

        if choice == 18:
            _progress()
            return base64.b16encode(zlib.compress(marshal.dumps(data.encode()))).decode(), "marshal_zlib_base16"

        if choice == 19:
            _progress()
            return base64.b64encode(zlib.compress(marshal.dumps(data.encode()))).decode(), "marshal_zlib_base64"

        if choice == 20:
            _progress()
            return base64.b32encode(zlib.compress(marshal.dumps(data.encode()))).decode(), "marshal_zlib_base32"

        if choice == 21:
            _progress()
            return base64.b64encode(bz2.compress(marshal.dumps(data.encode()))).decode(), "marshal_bz2_base64"

        if choice == 22:
            _progress()
            return base64.b64encode(lzma.compress(zlib.compress(data.encode()))).decode(), "base64_marshal_lzma_zlib"

        if choice == 23:
            _progress()
            return base64.b85encode(lzma.compress(bz2.compress(marshal.dumps(data.encode())))).decode(), "marshal_bz2_lzma_base85"

        if choice == 24:
            _progress()
            with tempfile.TemporaryDirectory() as tmpdir:
                src_path = os.path.join(tmpdir, "temp_script.py")
                out_path = os.path.join(tmpdir, "dist", "temp_script.py")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(data)
                os.makedirs(os.path.join(tmpdir, "dist"), exist_ok=True)
                result = subprocess.run(
                    ["pyarmor", "obfuscate", "-O", os.path.join(tmpdir, "dist"), src_path],
                    capture_output=True, text=True
                )
                if result.returncode != 0:
                    print(Fore.RED + f"Pyarmor failed: {result.stderr.strip()}")
                    return None, None
                if not os.path.exists(out_path):
                    print(Fore.RED + "Pyarmor output file not found.")
                    return None, None
                with open(out_path, "r", encoding="utf-8") as f:
                    return f.read(), "pyarmor_obfuscate"

        return None, None
    except Exception as e:
        print(Fore.RED + f"Error encoding data: {e}")
        return None, None


async def save_result(filename: str, data: Union[str, bytes]) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    try:
        if isinstance(data, bytes):
            await asyncio.to_thread(write_binary_file, path, data)
        else:
            async with aiofiles.open(path, "w", encoding="utf-8") as f:
                await f.write(str(data))
        print(Fore.GREEN + f"Result saved to {path}")
    except Exception as e:
        print(Fore.RED + f"Failed to save file: {e}")


def write_binary_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)


def generate_runner(encoded_str, method):
    try:
        header_comment = (
            "# Encrypted : tepeed\n"
            f"# Time Encrypted: {datetime.now().strftime('%d-%m-%y %H:%M %p')}"
            "\n# Telegram : @tepeed\n"
            "# Github : https://github.com/tepeed\n"
        )
        e = encoded_str.strip()
        runners = {
            "base16": f'''{header_comment}\nimport base64\ndata = """{e}"""\nexec(base64.b16decode(data.encode()))\n''',
            "base64": f'''{header_comment}\nimport base64\ndata = """{e}"""\nexec(base64.b64decode(data.encode()))\n''',
            "base32": f'''{header_comment}\nimport base64\ndata = """{e}"""\nexec(base64.b32decode(data.encode()))\n''',
            "marshal": f'''{header_comment}\nimport marshal, binascii\nexec(marshal.loads(binascii.unhexlify("""{e}""")))\n''',
            "zlib": f'''{header_comment}\nimport zlib, binascii\nexec(zlib.decompress(binascii.unhexlify("""{e}""")))\n''',
            "marshal_zlib": f'''{header_comment}\nimport marshal, zlib, binascii\nexec(marshal.loads(zlib.decompress(binascii.unhexlify("""{e}"""))))\n''',
            "marshal_base16": f'''{header_comment}\nimport marshal, base64\nexec(marshal.loads(base64.b16decode("""{e}""")))\n''',
            "marshal_base64": f'''{header_comment}\nimport marshal, base64\nexec(marshal.loads(base64.b64decode("""{e}""")))\n''',
            "marshal_zlib_base16": f'''{header_comment}\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b16decode("""{e}"""))))\n''',
            "marshal_zlib_base64": f'''{header_comment}\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode("""{e}"""))))\n''',
            "marshal_zlib_base32": f'''{header_comment}\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b32decode("""{e}"""))))\n''',
            "base64_marshal_lzma_zlib": f'''{header_comment}\nimport marshal, base64, lzma, zlib\nexec(zlib.decompress(lzma.decompress(base64.b64decode("""{e}"""))))\n''',
            "marshal_bz2_lzma_base85": f'''{header_comment}\nimport marshal, base64, lzma, bz2\ntemp = base64.b85decode("""{e}""")\nexec(marshal.loads(bz2.decompress(lzma.decompress(temp))))\n''',
            "base32_binascii": f'''{header_comment}\nimport base64, binascii\nhex_data = """{e}"""\nraw_base32 = binascii.unhexlify(hex_data)\ndecoded = base64.b32decode(raw_base32)\nexec(decoded)\n''',
            "gzip": f'''{header_comment}\nimport gzip, binascii\nexec(gzip.decompress(binascii.unhexlify("""{e}""")))\n''',
            "marshal_gzip": f'''{header_comment}\nimport marshal, gzip, binascii\nexec(marshal.loads(gzip.decompress(binascii.unhexlify("""{e}"""))))\n''',
            "marshal_gzip_base64": f'''{header_comment}\nimport marshal, gzip, base64\nexec(marshal.loads(gzip.decompress(base64.b64decode("""{e}"""))))\n''',
            "base85": f'''{header_comment}\nimport base64\nencoded_str = r"""{e}"""\nexec(base64.a85decode(encoded_str))\n''',
            "marshal_base85": f'''{header_comment}\nimport marshal, base64\nexec(marshal.loads(base64.a85decode("""{e}""")))\n''',
            "marshal_bz2_base64": f'''{header_comment}\nimport marshal, base64, bz2\nexec(marshal.loads(bz2.decompress(base64.b64decode("""{e}"""))))\n''',
            "marshal_lzma_base64": f'''{header_comment}\nimport marshal, base64, lzma\nexec(marshal.loads(lzma.decompress(base64.b64decode("""{e}"""))))\n''',
            "xor_base64": f'''{header_comment}\nimport base64\nkey = 23\ndata = base64.b64decode("""{e}""")\nexec(bytes([b ^ key for b in data]))\n''',
            "rot13": f'''{header_comment}\nimport codecs\nexec(codecs.decode("""{e}""", "rot_13"))\n''',
            "pyc_emoji": f'''{header_comment}\nHEX_EMOJI_MAP = {{\n    '0': '😀', '1': '😁', '2': '😂', '3': '🤣',\n    '4': '😃', '5': '😄', '6': '😅', '7': '😆',\n    '8': '😉', '9': '😊', 'a': '😋', 'b': '😎',\n    'c': '😍', 'd': '😘', 'e': '😗', 'f': '😙',\n}}\nEMOJI_HEX_MAP = {{v: k for k, v in HEX_EMOJI_MAP.items()}}\ndef emoji_to_hex(emoji_str):\n    return ''.join(EMOJI_HEX_MAP[ch] for ch in emoji_str)\nimport marshal, binascii\nencoded_emoji = """{e}"""\nhex_str = emoji_to_hex(encoded_emoji)\npyc_bytes = binascii.unhexlify(hex_str)\ncode_obj = marshal.loads(pyc_bytes)\nexec(code_obj)\n''',
            "pickle_base64": f'''{header_comment}\nimport pickle, base64\nexec(pickle.loads(base64.b64decode("""{e}""")))\n''',
        }
        return runners.get(method)
    except Exception as e:
        print(f"Error generating runner: {e}")
        return None


async def save_runner_file(method_name: str, runner_code: Union[str, bytes]) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"runner-{method_name}.py"
    path = os.path.join(OUTPUT_DIR, filename)
    try:
        if isinstance(runner_code, bytes):
            await asyncio.to_thread(write_binary_file, path, runner_code)
        else:
            async with aiofiles.open(path, "w", encoding="utf-8") as f:
                await f.write(str(runner_code))
        print(Fore.GREEN + f"Runner saved to {path}")
    except Exception as e:
        print(Fore.RED + f"Failed to save runner file: {e}")


async def process_encoding_choice(choice):
    clear_screen()
    print_banner()
    file_path = await asyncio.to_thread(input, Fore.YELLOW + "Enter path to .py file: " + Fore.LIGHTBLUE_EX)
    if not os.path.isfile(file_path) or not file_path.endswith(".py"):
        print(Fore.RED + "Invalid Python file path.")
        input(Fore.CYAN + "Press Enter to return to menu...")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        user_input = f.read()
    encoded, method = encode_choice(choice, user_input)
    if encoded and method:
        filename = f"encoded-{method}.txt"
        await save_result(filename, encoded)
        runner_code = generate_runner(encoded, method)
        if runner_code:
            await save_runner_file(method, runner_code)
        else:
            print(Fore.RED + "Failed to generate runner script.")
    else:
        print(Fore.RED + "Encoding failed or unsupported method.")
    input(Fore.CYAN + "Press Enter to return to menu...")


def pyarmor_obfuscate():
    try:
        version = check_pyarmor_version()
        if version is None:
            print(Fore.RED + "PyArmor not found or not installed.")
            return
        if not version.startswith("9.1.8"):
            print(Fore.YELLOW + f"Warning: Recommended PyArmor version is 9.1.8 but found {version}")
        filepath = input(Fore.CYAN + "Enter path to Python (.py) file to obfuscate: ").strip()
        if not os.path.isfile(filepath) or not filepath.endswith(".py"):
            print(Fore.RED + "Invalid Python file path.")
            return
        output_folder = os.path.join(OUTPUT_DIR, "pyarmor_output")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        print(Fore.YELLOW + "Running PyArmor obfuscation...")
        result = subprocess.run(
            ["pyarmor", "obfuscate", "--output", output_folder, filepath],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(Fore.GREEN + f"PyArmor obfuscation successful, output in {output_folder}")
            print(Fore.CYAN + result.stdout)
            return
        print(Fore.RED + "PyArmor obfuscation failed:")
        print(Fore.RED + result.stderr)
    except Exception as e:
        print(Fore.RED + f"PyArmor error: {e}")


def pyinstaller_build():
    if not check_pyinstaller_installed():
        print(Fore.RED + "PyInstaller not installed.")
        return
    filepath = input(Fore.CYAN + "Enter path to Python (.py) file to build EXE: ").strip()
    if not os.path.isfile(filepath) or not filepath.endswith(".py"):
        print(Fore.RED + "Invalid Python file path.")
        return
    output_folder = os.path.join(OUTPUT_DIR, "pyinstaller_output")
    os.makedirs(output_folder, exist_ok=True)
    if os.path.exists("build"):
        shutil.rmtree("build")
    print(Fore.YELLOW + "Running PyInstaller...")
    result = subprocess.run(
        ["pyinstaller", "--onefile", "--distpath", output_folder, filepath],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(Fore.GREEN + f"PyInstaller build successful, output in {output_folder}")
        return
    print(Fore.RED + "PyInstaller build failed:")
    print(Fore.RED + result.stderr)
    print(Fore.RED + result.stdout)


def pyarmor_plus_pyinstaller():
    version = check_pyarmor_version()
    if not version:
        print(Fore.RED + "❌ PyArmor not found or not installed.")
        return
    if not version.startswith("9.1.8"):
        print(Fore.YELLOW + f"⚠️  Recommended PyArmor version is 9.1.8, but found {version}")
    if not check_pyinstaller_installed():
        print(Fore.RED + "❌ PyInstaller not installed.")
        return
    filepath = input(Fore.CYAN + "📄 Enter path to Python (.py) file: ").strip()
    if not os.path.isfile(filepath) or not filepath.endswith(".py"):
        print(Fore.RED + "❌ Invalid Python file path.")
        return
    filename = os.path.basename(filepath).replace(".py", "")
    with tempfile.TemporaryDirectory() as tmpdir:
        dist_dir = os.path.join(tmpdir, "dist")
        os.makedirs(dist_dir, exist_ok=True)
        print(Fore.YELLOW + "🔐 Obfuscating with PyArmor...")
        for _ in tqdm(range(30), desc="Running PyArmor", ncols=70,
                       bar_format="{l_bar}{bar}| {remaining}s"):
            time.sleep(0.02)
        obf = subprocess.run(
            ["pyarmor", "obfuscate", "-O", dist_dir, filepath],
            capture_output=True, text=True
        )
        if obf.returncode != 0:
            print(Fore.RED + "❌ PyArmor obfuscation failed:")
            print(Fore.RED + obf.stderr.strip())
            return
        print(Fore.GREEN + "✅ PyArmor obfuscation completed.\n")
        obf_files = glob.glob(os.path.join(dist_dir, "**", "*.py"), recursive=True)
        obf_script = obf_files[0] if obf_files else None
        if not obf_script:
            print(Fore.RED + "❌ Obfuscated .py file not found.")
            print(Fore.YELLOW + f"🔍 Check contents of: {dist_dir}")
            return
        output_folder = os.path.join("output", "pyarmor_pyinstaller_output")
        os.makedirs(output_folder, exist_ok=True)
        print(Fore.YELLOW + "⚙️  Building EXE with PyInstaller...")
        for _ in tqdm(range(50), desc="Packaging EXE", ncols=70,
                       bar_format="{l_bar}{bar}| {remaining}s"):
            time.sleep(0.015)
        exe = subprocess.run(
            ["pyinstaller", "--onefile", "--distpath", output_folder, obf_script],
            capture_output=True, text=True
        )
        if exe.returncode != 0:
            print(Fore.RED + "❌ PyInstaller build failed:")
            print(Fore.RED + exe.stderr.strip())
        else:
            output_exe = os.path.join(
                output_folder, os.path.basename(obf_script).replace(".py", ".exe")
            )
            print(Fore.GREEN + "✅ EXE build complete:")
            print(Fore.CYAN + f"📦 Output: {output_exe}\n")


def install_packages():
    clear_screen()
    print_banner()
    print(Fore.CYAN + "Installing required packages...\n")
    packages = ["colorama", "pyfiglet", "pyarmor==9.1.8", "pyinstaller", "tqdm", "pytz", "requests"]
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        for pkg in tqdm(packages, desc="Installing packages", ncols=70):
            print(Fore.YELLOW + f"Installing {pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            time.sleep(0.2)
        print(Fore.GREEN + "\nAll packages installed successfully!")
    except Exception as e:
        print(Fore.RED + f"Package installation error: {e}")


def print_helper():
    clear_screen()
    print_banner()
    print(Fore.CYAN + "\nHelper - Usage & Info:\n\n- Choose encoding method from menu.\n- Input text to encode; encoded result saved in 'encode/' folder.\n- Runner script for each encoding method saved in 'encode/' folder.\n- PyArmor obfuscation requires PyArmor 9.1.8 (recommended).\n- PyInstaller builds EXE in 'encode/pyinstaller_output'.\n- PyArmor + EXE obfuscates then builds EXE.\n- Option 25 installs required packages automatically.\n- Press Ctrl+C anytime to exit.\n")


def print_menu():
    print_banner_with_timezone()
    labels = (
        "Exit", "ROT13", "Zlib", "Gzip", "Pyc (Emoji)", "Base85", "Base16", "Base64", "Base32",
        "XOR + Base64", "Marshal + Gzip", "Marshal + Zlib", "Marshal + Base16", "Marshal + Base64",
        "Marshal + Base85", "Pickle + Base64", "Base32 + BinAscii", "Marshal + Lzma + Base64",
        "Marshal + Zlib + Base16", "Marshal + Zlib + Base64", "Marshal + Zlib + Base32",
        "Marshal + Bz2 + Base64", "Base64 + Marshal + Lzma + Zlib", "Marshal + Bz2 + Lzma + Base85",
        "PyArmor Obfuscate", "Install all required packages", "Helper - Usage & Info",
        "Python script to EXE (PyInstaller)", "PyArmor + EXE (Obfuscate + PyInstaller)"
    )
    col_width = 55
    total = len(labels)
    half = (total + 1) // 2

    def colored_option(idx, label):
        if idx == 0:
            return f"{Fore.WHITE}({Fore.RED}00{Fore.WHITE}) {Fore.RED}Exit{Fore.RESET}"
        return f"{Fore.YELLOW}({Fore.MAGENTA}{str(idx).zfill(2)}{Fore.YELLOW}){Fore.LIGHTWHITE_EX} {label}{Fore.RESET}"

    for i in range(half):
        left_idx = i
        right_idx = i + half
        left = colored_option(left_idx, labels[left_idx]).ljust(col_width)
        right = colored_option(right_idx, labels[right_idx]) if right_idx < total else ""
        print(left + right)


async def main():
    try:
        while True:
            clear_screen()
            print_banner()
            print_menu()
            choice = await asyncio.to_thread(
                input,
                f"\n{Fore.YELLOW}({Fore.MAGENTA}+{Fore.YELLOW}){Fore.LIGHTWHITE_EX} ( {Fore.LIGHTYELLOW_EX}Choose option {Fore.LIGHTYELLOW_EX}0{Fore.LIGHTWHITE_EX}-{Fore.LIGHTYELLOW_EX}28{Fore.LIGHTWHITE_EX} )--{Fore.LIGHTMAGENTA_EX}> "
            )
            if choice == "0":
                print(Fore.MAGENTA + "Goodbye!")
                return
            if choice == "25":
                install_packages()
                input(Fore.CYAN + "Press Enter to return to menu...")
            elif choice == "26":
                print_helper()
                input(Fore.CYAN + "Press Enter to return to menu...")
            elif choice == "27":
                clear_screen()
                pyinstaller_build()
                input(Fore.CYAN + "Press Enter to return to menu...")
            elif choice == "28":
                clear_screen()
                pyarmor_plus_pyinstaller()
                input(Fore.CYAN + "Press Enter to return to menu...")
            elif choice.isdigit() and 1 <= int(choice) <= 23:
                await process_encoding_choice(int(choice))
            elif choice == "24":
                clear_screen()
                pyarmor_obfuscate()
                input(Fore.CYAN + "Press Enter to return to menu...")
            else:
                print(Fore.RED + "Invalid choice.")
                input(Fore.CYAN + "Press Enter to continue...")
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nInterrupted by user. Exiting...")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
        input(Fore.CYAN + "Press Enter to continue...")


if __name__ == "__main__":
    asyncio.run(main())
