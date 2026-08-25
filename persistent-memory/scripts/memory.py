#!/usr/bin/env python3
"""Plain-text CLI for persistent-memory/SKILL.md.

One memory file per topic, under MEMORY_DIR (default .claude/memory/),
plain markdown, one dated line per entry. No database, nothing binary -
the file is meant to be read and hand-edited as easily as the script
writes it.

    memory.py show <topic>            # print the file, or say there isn't one
    memory.py append <topic> "<note>" # add one dated line
    memory.py list                    # list every topic with a memory file

This script only reads and appends. Pruning or editing a stale entry
(see SKILL.md's "Keeping it honest") is a manual edit to the file,
deliberately not something this script does on its own.
"""
import datetime
import os
import re
import sys


def memory_dir():
    return os.environ.get("MEMORY_DIR") or os.path.join(".claude", "memory")


def topic_path(topic):
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", topic)
    if not safe:
        raise ValueError("topic must contain at least one alphanumeric character")
    return os.path.join(memory_dir(), f"{safe}.md")


def cmd_show(topic):
    path = topic_path(topic)
    if not os.path.exists(path):
        print(f"No memory file for '{topic}' yet ({path}).")
        return
    with open(path) as f:
        sys.stdout.write(f.read())


def cmd_append(topic, note):
    note = note.strip()
    if not note:
        print("Nothing to append - note was empty.", file=sys.stderr)
        sys.exit(1)
    path = topic_path(topic)
    os.makedirs(memory_dir(), exist_ok=True)
    is_new = not os.path.exists(path)
    date = datetime.date.today().isoformat()
    with open(path, "a") as f:
        if is_new:
            f.write(f"# Memory: {topic}\n\n")
        f.write(f"- {date}: {note}\n")
    print(f"Appended to {path}")


def cmd_list():
    d = memory_dir()
    if not os.path.isdir(d):
        print("No memory files yet.")
        return
    topics = sorted(name[:-3] for name in os.listdir(d) if name.endswith(".md"))
    if not topics:
        print("No memory files yet.")
        return
    for t in topics:
        print(t)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    cmd = args[0]
    if cmd == "show" and len(args) == 2:
        cmd_show(args[1])
    elif cmd == "append" and len(args) == 3:
        cmd_append(args[1], args[2])
    elif cmd == "list" and len(args) == 1:
        cmd_list()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
