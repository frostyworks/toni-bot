"""This module acts as our constants, but we
   will call it components.py"""

user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
darksky_line = "https://api.darksky.net/forecast/abe6a84811a8ab8f1f39cd9b8b8f40e1/{},{}"
welcome_line = "Hype Roleplay არის ერთ ერთი ახალი საუკეთესო ქართული სერვერი რომელიც მიმდინარეობს ვირტუალურ ქართულ სამყაროში, ქალაქ თბილიშში. ჩვენი სერვერი ხმარობს GTA V კლიენტს რომელსაც ქვია RAGE MULTIPLAYER."


def check_digits(s):
    """Check if a string contains digit and return true"""
    return any(i.isdigit() for i in s)
