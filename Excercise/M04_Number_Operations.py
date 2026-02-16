#Accumulator (sum of all)
prices=[1,2,3,5,6,7,8,9,10]

def calculate_total(prices):
    total=0 
    for price in prices:
           
        total+=price
    return total

print(calculate_total(prices))

#counter
def counter_number(count):

    total=0
    for c in count:
        total+=1
    return total

print(counter_number([1,2,3,4,5,6,7,8,9,0,10]))

#running balance 
def track_transactions(initial_balance, transactions):
    balance = initial_balance
    history=[]

    for t in transactions:
        balance+=int(t)
    
        history.append(balance)

    return history

print(track_transactions(10000, [1000]))

# Example 4: Delta (Change Measurement)
def calculate_change(before, after):
    delta = after - before
    percent_change = (delta / before) * 100 if before != 0 else 0 
    return {"delta": delta,"percent": percent_change}

print(calculate_change(100,150))

# Example 5: Test Result Analysis
def analyze_test_results(results):
    counts = {"pass": 0, "fail": 0, "skip": 0}
    
    for result in results:
        counts[result["status"]] += 1
            
    total = sum(counts.values())
    pass_rate = (counts["pass"] / total * 100) if total > 0 else 0
    
    return {**counts, "pass_rate": f"{pass_rate:.2f}%"}

test_data = [{"status": "pass"}, {"status": "fail"}, {"status": "pass"}, {"status": "skip"}]
print(analyze_test_results(test_data))
