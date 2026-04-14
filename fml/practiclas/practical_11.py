import numpy as np

# Training and test data provided explicitly
train_data = np.array([[1, 2], [2, 1], [1, 1], [8, 8], [9, 8], [9, 9]])
test_data = np.array([[2, 2], [8, 9]])

def my_kmeans(data):
    # Take first point and fourth point as our starting centers
    c1 = data[0]
    c2 = data[3]
    
    for i in range(10): # loop 10 times
        group1 = []
        group2 = []
        
        for p in data:
            # calculate euclidean distance to c1 and c2
            dist1 = np.sqrt(np.sum((p - c1)**2))
            dist2 = np.sqrt(np.sum((p - c2)**2))
            
            # assign to closest group
            if dist1 < dist2:
                group1.append(p)
            else:
                group2.append(p)
                
        # find the new average center for each group
        c1 = np.mean(group1, axis=0)
        c2 = np.mean(group2, axis=0)
        
    return c1, c2

# 1. Train the model manually
center1, center2 = my_kmeans(train_data)
print("Center 1:", center1)
print("Center 2:", center2)

# 2. Predict on test data
predictions = []
for p in test_data:
    d1 = np.sqrt(np.sum((p - center1)**2))
    d2 = np.sqrt(np.sum((p - center2)**2))
    
    if d1 < d2:
        predictions.append(1) # belongs to group 1
    else:
        predictions.append(2) # belongs to group 2

print("Test point predictions:", predictions)
