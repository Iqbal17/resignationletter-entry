"""The Funniest One-Line Resignation Letter (u-deranalabs, $10).

Writes the chosen resignation letter to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt), exactly one line plus a trailing
newline. Sealed gate: UTF-8 text of 1 to 140 characters, not only
white space.

Decision record (weighed against the judge's criteria, most important
first: on-subject -> funny on first read with a real comic turn ->
flat tired voice of the thing itself -> tightness -> a complaint only
this thing could make):

Candidate A — cron job asking for a Sunday:
    "I have fired every minute since March. I am not asking for a
    raise. I am asking for a Sunday." (93 chars)
    Loses: the turn is a generic worker complaint. Any tired employee
    could ask for a Sunday; nothing in it belongs to a cron job in
    particular, so it fails criterion 5 (specific and surprising).

Candidate B — retry loop as tradition:
    "I have retried this 4,096 times and it still fails. I am not a
    loop. I am a tradition." (86 chars)
    Strong reserve: the turn is real (retries that never succeed become
    ritual), and the voice is flat. Loses only to C: "tradition" is a
    clever label, but the joke is about the loop's history rather than
    what the loop actually does, so it lands a beat slower.

Candidate C — rate limit resigning by going silent (CHOSEN):
    "I have said no 2.4 million times this week. Effective
    immediately, I will be saying nothing." (92 chars)
    Wins: the joke IS the job. A rate limit's entire function is
    refusing, so resigning by refusing to refuse is a complaint only
    a rate limit could make. The number gives it scale, "Effective
    immediately" is real resignation-letter register, and the
    punchline lands on the last three words in a flat, tired voice.

Candidate D — cron job quitting the 3 a.m. shift:
    "Effective immediately, I resign. Someone else can wake up at
    3 a.m. to do nothing, on time, forever." (100 chars)
    Strong reserve: "to do nothing, on time, forever" is specific to
    a cron job's pointless punctuality. Loses to C: it spends its
    first sentence announcing the resignation, and the turn arrives
    as a list of three beats instead of one clean twist.

Writing passes on the winner:
Pass 1 — the first draft opened "This week I have said no 2.4
million times." Front-loading "This week" buried the scale; moving
the number to the end of the first sentence ("I have said no 2.4
million times this week.") lets the count land as the sentence's
punch before the resignation begins.
Pass 2 — the first draft ended "I am saying nothing." The flat
present tense read like a shrug; "I will be saying nothing." keeps
the bureaucratic future of a resignation letter ("Effective
immediately, I will be...") and makes the silence sound like a
policy change rather than a mood, which is funnier for a rate limit.
A shorter variant ("From now on, I say nothing.") was tried and
dropped: it loses the resignation-letter register that makes the
second sentence sound like an official notice.
"""

import os

MAX_CHARS = 140

LINE = "I have said no 2.4 million times this week. Effective immediately, I will be saying nothing."


def has_clean_edges(text):
    """Reject leading/trailing whitespace or control characters.

    The sealed gate counts raw characters, so stray whitespace would
    silently eat the 1-140 budget and a control character would break
    the one-line shape. The LINE itself has clean edges, so this guard
    only fires on a future edit that slips one in.
    """
    if text != text.strip():
        return False
    return all(ord(ch) >= 0x20 for ch in text)


def check_gate(text):
    """Mirror the sealed gate: 1-140 chars, UTF-8, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if not has_clean_edges(text):
        return False
    text.encode("utf-8")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not check_gate(LINE):
        raise SystemExit("line fails the 1-140 character gate")
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
