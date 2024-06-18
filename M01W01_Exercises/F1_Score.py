def get_positive_integer():
    while True:
        try:
            value = int(input("Enter the positive integer: "))
            if value > 0:
                return value
            else:
                print("Entered value must be bigger than 0.")
        except ValueError:
            print("Enter value must be integer.")

# Test value tp = 2, fp = 3, fn = 3, recall = precision = f1_score = 0.4

def compute_f1_score(tp,fp,fn):
    
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*(precision*recall)/(precision+recall)
    print("Precision:", round(precision,2))
    print("Recall:", round(recall,2))
    print("F1 Score:", round(f1_score,2))
    return f1_score 

# Enter tp, fp, fn value
tp = get_positive_integer()
#print("tp:", tp)
fp = get_positive_integer()
#print("fp:", fp)
fn = get_positive_integer()
#print("fn:", fn)
compute_f1_score(tp,fp,fn)
