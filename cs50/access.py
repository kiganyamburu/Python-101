# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
#
# 2. Create two empty lists: "approved" and "denied".
#
# 3. Start a loop to collect visitor info:
#
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.
#
#
# Example commented implementation (everything below is intentionally a comment):
#
revoked = {24601, 31415, 27182}  # example revoked badge numbers
approved = []
denied = []

while True:
    # prompt for name; 'done' (case-insensitive) exits
    name = input("Visitor name (or 'done' to finish): ").strip()
    if name.lower() == 'done':
        break

    # prompt for badge number; keep as string to allow leading zeros if needed
    badge_str = input("Badge number: ").strip()

    # basic validation: ensure some value was entered
    if not badge_str:
        print("No badge entered — ACCESS DENIED")
        denied.append(name)
        continue

    # attempt to parse badge as integer for comparison with revoked set
    try:
        badge = int(badge_str)
    except ValueError:
        # non-numeric badges are treated as denied in this policy
        print("Invalid badge format — ACCESS DENIED")
        denied.append(name)
        continue

    # check revocation
    if badge in revoked:
        denied.append(name)
        print("ACCESS DENIED")
    else:
        approved.append(name)
        print("ACCESS GRANTED")

# After loop: sort and print a summary
approved.sort()
denied.sort()

print("\nAccess Summary")
print("✅ Approved Visitors ({}):".format(len(approved)))
for person in approved:
    print(" -", person)

print("\n⛔️ Denied Visitors ({}):".format(len(denied)))
for person in denied:
    print(" -", person)
