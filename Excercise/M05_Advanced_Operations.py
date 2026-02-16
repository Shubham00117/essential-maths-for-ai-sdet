# Example 1: Pagination Logic
# Think: "How many complete pages? Any leftover items?"

# Define a function named 'paginate' that takes two arguments:
# total_items: The total number of items to be displayed.
# page_size: The number of items allowed per page.
def paginate(total_items, page_size):
    """Calculate pagination info"""
    
    # Use integer division (//) to find how many full pages we have.
    # Example: 47 // 10 = 4 full pages.
    full_pages = total_items // page_size  # Complete pages
    
    # Use the modulo operator (%) to find the remainder (items left over).
    # Example: 47 % 10 = 7 items remaining.
    remaining = total_items % page_size    # Items on last page

    # Calculate total pages.
    # If there are remaining items (remaining > 0), we need an extra page to hold them.
    # Logic: 4 full pages + 1 extra page for the 7 remaining items = 5 total pages.
    total_pages = full_pages + (1 if remaining > 0 else 0)

    # Return a dictionary containing all the calculated pagination details.
    return {
        "total_items": total_items,
        "page_size": page_size,
        "full_pages": full_pages,
        # If remaining is 0, it means the last page is full (equal to page_size).
        # Otherwise, the last page has 'remaining' items.
        "last_page_items": remaining if remaining > 0 else page_size,
        "total_pages": total_pages
    }

# Usage Example:
# We have 47 items in total, and we want to display 10 items per page.
result = paginate(47, 10)

# Print the total number of pages calculated.
print(f"Total pages: {result['total_pages']}")  # Output: 5

# Print the number of items on the last page.
print(f"Last page has: {result['last_page_items']} items")  # Output: 7

# 🔑 Key insight: // gives pages, % gives remainder

# Example 2: Time Conversion
# Think: "Convert seconds to hours:minutes:seconds"

def seconds_to_time(total_seconds):
    """Convert seconds to H:M:S format"""
    
    # Calculate hours: There are 3600 seconds in an hour (60 * 60).
    # Integer division (//) gives the whole number of hours.
    hours = total_seconds // 3600
    
    # Calculate remaining seconds after extracting hours using modulo (%).
    remaining = total_seconds % 3600

    
    # Calculate minutes: There are 60 seconds in a minute.
    # Integer division on the remaining seconds gives the minutes.
    minutes = remaining // 60
    
    # Calculate final seconds: The remainder after extracting minutes.
    seconds = remaining % 60
    
    # Return formatted string. :02d ensures 2 digits with leading zero if needed.
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(seconds_to_time(3725))  # Output: 01:02:05
print(seconds_to_time(7200))  # Output: 02:00:00
print(seconds_to_time(90))    # Output: 00:01:30

# 🔑 Key insight: Chain // and % to break down units

# Example 3: Cyclic/Wrap-Around Pattern
# Think: "Like a clock that wraps from 12 back to 1"

def get_next_in_cycle(current_index, cycle_length):
    """
    Get the next position in a list, wrapping back to 0 if we hit the end.
    Logic: (Current Position + 1) divided by Total Length -> Keep the Remainder (%)
    """
    return (current_index + 1) % cycle_length

# CASE STUDY: Round-robin through 3 servers
# In SDET work, we use this to balance the test load across multiple environments.

servers = ["Server A", "Server B", "Server C"] # Length is 3 (Indices: 0, 1, 2)
current = 0 # Start at the first server (index 0)

print("\n--- Starting Round Robin Server Rotation (7 Requests) ---")

for request in range(7):
    # Step A: Use the current server index to pick from the list
    print(f"Request {request + 1} → {servers[current]}")
    
    # Step B: Calculate the next index for the next loop
    # If current is 0 -> 1
    # If current is 1 -> 2
    # If current is 2 -> (2+1)%3 = 0 (The WRAP AROUND happens here!)
    current = get_next_in_cycle(current, len(servers))

# Output logic visualization:
# Request 1 → Server A (index 0)
# Request 2 → Server B (index 1)
# Request 3 → Server C (index 2)
# Request 4 → Server A (index 0 - wraps back because 3 % 3 = 0)
# Request 5 → Server B (index 1 - 4 % 3 = 1)
# Request 6 → Server C (index 2 - 5 % 3 = 2)
# Request 7 → Server A (index 0 - 6 % 3 = 0)

# 🔑 Key insight: The modulo operator (%) effectively creates a 'trapdoor' 
# that catches the number before it goes out of bounds and drops it back to the start.

# Example 4: Divisibility Checks
# Think: "Does it divide evenly?"
def analyze_divisibility(number):
    """Check divisibility by common numbers using Modulo (%)"""
    # Logic: If (number % divisor) is 0, then the number is perfectly divisible.
    results = {}
    for divisor in [2, 3, 5, 10]:
        # '== 0' check is the core of divisibility logic
        results[divisor] = number % divisor == 0
    return results

print("\n--- Divisibility Analysis ---")
print(f"30 analysis: {analyze_divisibility(30)}")
# Expected: {2: True, 3: True, 5: True, 10: True}

print(f"25 analysis: {analyze_divisibility(25)}")
# Expected: {2: False, 3: False, 5: True, 10: False}

# 🔑 Key insight: x % y == 0 is the universal way to check 'Is x a multiple of y?'
# Example 5: Distribute Items into Groups
# Think: "Split evenly, handle leftovers"

def distribute_evenly(total, num_groups):
    """
    Distribute items as evenly as possible across groups.
    Logic: 
    1. Find the base amount (floor division //)
    2. Find the remainder (modulo %)
    3. Add 1 extra to the first 'remainder' groups
    """
    
    # Calculate the minimum items every group must have
    base_amount = total // num_groups 
    
    # Calculate how many items are 'left over' after even division
    extra = total % num_groups 
    
    distribution = []
    
    # Loop through each group to assign their items
    for i in range(num_groups):
        # WORKFLOW: If we still have 'extra' items left, 
        # give this group (base + 1) items.
        if i < extra:
            distribution.append(base_amount + 1)
        else:
            # Otherwise, give them the standard base amount.
            distribution.append(base_amount)
            
    return distribution

print("\n--- Items Distribution ---")
# Example: Distribute 17 items among 5 groups
# Math: 17 // 5 = 3 (base), 17 % 5 = 2 (extra)
# Result: 2 groups get 4, 3 groups get 3 -> [4, 4, 3, 3, 3]
result = distribute_evenly(17, 5)
print(f"17 items in 5 groups: {result}") 
print(f"Total check: {sum(result)} items") # Should equal 17

# 🔑 Key insight: // gives the baseline, % tells you how many units need an extra +1.

