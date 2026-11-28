import imaplib, email, os, re, sys, datetime, urllib.request, urllib.parse
from email.header import decode_header
sys.path.insert(0, "/root/secondbrain")
from jarvis_brain import log_email

env_path = "/root/.hermes/.env"
if os.path.exists(env_path):
    for line in open(env_path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

USER = os.environ.get("GMAIL_USER", "")
PASS = os.environ.get("GMAIL_APP_PASSWORD", "").replace(" ", "")
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("TELEGRAM_ALLOWED_USERS", "").split(",")[0].strip()

KEYWORDS = re.compile(
    r"(recruiter|hiring|careers|interview|offer|assessment|shortlist|challenge|hackerrank|codility|nqt|apprenticeship|sde|software engineer)",
    re.I
)

def dec(val):
    if not val:
        return ""
    parts = decode_header(val)
    return "".join(
        t.decode(enc or "utf-8", errors="replace") if isinstance(t, bytes) else t
        for t, enc in parts
    )

def send_telegram(text):
    if not (BOT_TOKEN and CHAT_ID):
        print(text)
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}).encode()
    urllib.request.urlopen(url, data=data, timeout=15)

def main():
    if not (USER and PASS):
        print("Missing GMAIL_USER or GMAIL_APP_PASSWORD in /root/.hermes/.env")
        return
    since = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%b-%Y")
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(USER, PASS)
    mail.select("INBOX")
    _, data = mail.search(None, f'(SINCE "{since}")')
    hits = []
    for num in data[0].split():
        _, msg_data = mail.fetch(num, "(BODY.PEEK[HEADER.FIELDS (MESSAGE-ID FROM SUBJECT DATE)])")
        msg = email.message_from_bytes(msg_data[0][1])
        msg_id = (msg.get("Message-ID") or num.decode()).strip()
        sender = dec(msg.get("From"))
        subject = dec(msg.get("Subject"))
        date_str = dec(msg.get("Date"))
        if KEYWORDS.search(f"{sender} {subject}"):
            if log_email(msg_id, sender, subject, date_str, "career"):
                hits.append(f"• *{subject}*\n  From: `{sender}`")
    mail.logout()
    if hits:
        send_telegram("📬 *Important Mails (Last 24h)*\n\n" + "\n\n".join(hits))
    else:
        print("No new important mails in last 24h.")

if __name__ == "__main__":
    main()
