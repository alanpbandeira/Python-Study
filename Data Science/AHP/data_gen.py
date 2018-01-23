import numpy as np


n_criteria = 3
criteria_comb = int((n_criteria * (n_criteria - 1)) / 2)
criteria_relations = np.transpose(np.indices((n_criteria, n_criteria)))
criteria_relations = sorted([tuple(y) for x in criteria_relations for y in x])

selected = []

with open("data.csv", 'w') as fhand:
    for comb in range(criteria_comb):
        selected_idx = np.random.randint(0, (len(criteria_relations)-1))
        x, y = criteria_relations.pop(selected_idx)

        if x == y:
            grade = 1
        else:
            grade = np.random.randint(1, 9)
        
        selected.append((str(x), str(y), str(grade)))
    
    # print(selected)
    
    for relation in selected:
        print(relation)
        fhand.write(",".join(relation) + "\n")