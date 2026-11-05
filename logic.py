"""Enrollment and search logic for the Student Center prototype.

This file runs in the browser through Pyodide (Python compiled to
WebAssembly), so the prototype still needs no server and works on
GitHub Pages. index.html calls these functions for:

  * time-conflict detection in the shopping cart
  * the "Check my cart" readiness check
  * ranking results in the header search box

If Python can't load (no internet, or a viewer that blocks it), the page
falls back to matching JavaScript versions, so the demo never breaks.

The page talks to Python through api(), which takes and returns JSON
strings, so the JavaScript side never handles Python objects directly.

A class section looks like:
  {"code": "CECS 450", "title": "Data Visualization",
   "days": ["Tu", "Th"], "s": "9:30", "e": "10:45", "consent": False}
"""

import json


# ---------- time conflicts ----------

def to_minutes(hhmm):
    """'15:30' -> 930 minutes after midnight."""
    hours, minutes = hhmm.split(":")
    return int(hours) * 60 + int(minutes)


def shared_days(a, b):
    """Days both sections meet, e.g. ['Tu', 'Th']."""
    return [day for day in a["days"] if day in b["days"]]


def overlaps(a, b):
    """True when two sections meet on a shared day at overlapping times.

    Back-to-back classes (one ends at 10:45, the next starts at 10:45)
    do not count as a conflict.
    """
    if not shared_days(a, b):
        return False
    return (to_minutes(a["s"]) < to_minutes(b["e"])
            and to_minutes(b["s"]) < to_minutes(a["e"]))


def find_conflicts(cart):
    """Every pair of classes in the cart that overlap, as [code, code] pairs."""
    pairs = []
    for i, a in enumerate(cart):
        for b in cart[i + 1:]:
            if overlaps(a, b):
                pairs.append([a["code"], b["code"]])
    return pairs


def catalog_clashes(cart, catalog):
    """For each class not yet in the cart, the cart class it would overlap.

    Used to flag "Overlaps CECS 428" in the class list *before* the
    student adds the class (error prevention).
    """
    in_cart = {course["code"] for course in cart}
    clashes = {}
    for course in catalog:
        if course["code"] in in_cart:
            continue
        for held in cart:
            if overlaps(course, held):
                clashes[course["code"]] = held["code"]
                break
    return clashes


def check_cart(cart, holds):
    """Decide whether the cart is ready to enroll.

    Order matters:
      1. A time conflict blocks enrollment.
      2. A hold on the account blocks enrollment.
      3. A class that needs a permission number only blocks that class.
    """
    conflicts = find_conflicts(cart)
    needs_permission = [course["code"] for course in cart if course.get("consent")]
    if conflicts or holds:
        status = "bad"
    elif needs_permission:
        status = "warn"
    else:
        status = "ok"
    return {
        "status": status,
        "conflicts": conflicts,
        "holds": holds,
        "needs_permission": needs_permission,
    }


# ---------- search ----------

def score(query, code, title, keywords=""):
    """How well one item matches the search; 0 means no match.

    100  exact course number or code      "450", "cecs 450"
     90  start of the number or code      "45", "cecs 4"
     70  start of a word in the title     "graph" -> Computer Graphics
     50  appears anywhere                 "visual" -> Data Visualization
     40  every word appears somewhere     "mobile app" -> Mobile Application...
    """
    q = " ".join(query.lower().split())
    if not q:
        return 0
    code_l = code.lower()
    number = code_l.split()[-1] if code_l else ""
    haystack = f"{code_l} {title.lower()} {keywords.lower()}"
    if q in (number, code_l):
        return 100
    if (number and number.startswith(q)) or (code_l and code_l.startswith(q)):
        return 90
    if any(word.startswith(q) for word in title.lower().split()):
        return 70
    if q in haystack:
        return 50
    if all(word in haystack for word in q.split()):
        return 40
    return 0


def rank(query, items, key, title, keywords=None):
    """Matching items, best match first; ties keep their original order."""
    scored = []
    for position, item in enumerate(items):
        s = score(query, item.get(key, "") if key == "code" else "",
                  item.get(title, ""),
                  item.get(keywords, "") if keywords else "")
        if s:
            scored.append((-s, position, item))
    scored.sort()
    return [item for _, _, item in scored]


def search(query, mine, catalog, pages):
    """Grouped results for the header search box."""
    return {
        "mine": [c["code"] for c in rank(query, mine, "code", "title")],
        "catalog": [c["code"] for c in rank(query, catalog, "code", "title")],
        "pages": [p["name"] for p in rank(query, pages, "name", "name", "k")],
    }


# ---------- bridge to the page ----------

API = {
    "find_conflicts": find_conflicts,
    "catalog_clashes": catalog_clashes,
    "check_cart": check_cart,
    "search": search,
}


def api(name, payload_json):
    """Called from JavaScript: api('check_cart', '{"cart": [...], "holds": []}')."""
    return json.dumps(API[name](**json.loads(payload_json)))


if __name__ == "__main__":
    # Quick self-check: python3 logic.py
    cs428 = {"code": "CECS 428", "title": "Analysis of Algorithms", "days": ["Tu", "Th"], "s": "9:30", "e": "10:45"}
    cs450 = {"code": "CECS 450", "title": "Data Visualization", "days": ["Tu", "Th"], "s": "9:30", "e": "10:45"}
    cs491b = {"code": "CECS 491B", "title": "Computer Science Senior Project II", "days": ["Mo", "We"], "s": "14:00", "e": "15:15", "consent": True}
    late = {"code": "LATE 1", "title": "Back to back", "days": ["Tu"], "s": "10:45", "e": "11:30"}
    assert find_conflicts([cs428, cs450, cs491b]) == [["CECS 428", "CECS 450"]]
    assert not overlaps(cs428, late), "back-to-back classes are not a conflict"
    assert check_cart([cs428, cs450], [])["status"] == "bad"
    assert check_cart([cs428, cs491b], [])["status"] == "warn"
    assert check_cart([cs428], [])["status"] == "ok"
    assert check_cart([cs428], ["Advising hold"])["status"] == "bad"
    assert catalog_clashes([cs428], [cs428, cs450, cs491b]) == {"CECS 450": "CECS 428"}
    assert search("450", [], [cs428, cs450], [])["catalog"] == ["CECS 450"]
    assert search("graph", [], [cs450], [])["catalog"] == []
    assert search("visual", [], [cs450], [])["catalog"] == ["CECS 450"]
    assert search("textbooks", [], [], [{"name": "My Textbooks", "k": "books"}])["pages"] == ["My Textbooks"]
    print("logic.py: all checks passed")
