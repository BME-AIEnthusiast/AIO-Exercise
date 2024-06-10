# Exercise 1 
# Write function to evaluate the classification model by F1 score

# Function to evaluate model
def evaluate_model(tp, fp, fn): 
    # Calculate precision
    precision = tp / (tp + fp) 
    print("precision is", precision) 
    # Calculate recall
    recall = tp / (tp + fn) 
    print("recall is", recall)
    # Calculate F1 score
    f1_score = 2 * (precision * recall) / (precision + recall)
    print("f1_score is", f1_score)

    return precision, recall, f1_score

# Input 
tp_input = input("tp = ")
if not tp_input.isdigit(): # Check if input is a valid integer 
    print("tp must be int")
    exit()

tp = int(tp_input)

fp_input = input("fp = ")
if not fp_input.isdigit(): # Check if input is a valid integer 
    print("fp must be int")
    exit()

fp = int(fp_input)

fn_input = input("fn = ")
if not fn_input.isdigit(): # Check if input is a valid integer 
    print("fn must be int")
    exit()

fn = int(fn_input)

# Check if tp, fp, and fn are greater than zero
if tp <= 0 or fp <= 0 or fn <= 0:
    print("tp, fp, and fn must be greater than zero")
    exit()    

# Calculate
print(f"evaluate_model({tp}, {fp}, {fn})")
precision, recall, f1_score = evaluate_model(tp, fp, fn)
