import pandas
train_df=pandas.read_csv('train/west-to-north-routes-with-cells.csv')
#train_df=pandas.read_csv('train/north-to-west-routes-with-cells.csv')
train_route_ids = train_df['route_number'].unique()
train_route_cells_m=train_df['cell'].unique()
#train_df=pandas.read_csv('long_routes_t2a.csv')
#train_route_ids = train_df['route_number'].unique()
#train_route_cells_m=train_df['cell'].unique()
print(len(train_route_cells_m))
print(train_route_cells_m)
print(train_route_ids)
temp=[]
i=0
for number in train_route_ids:

         route_df = train_df[train_df['route_number'] == number]
         route_df=route_df['cell'].unique()
         temp.append(route_df)


similarity=[[0 for i in range (len(temp))]for j in range (len(temp))]
for i in range (len(temp)):
    for j in range (len(temp)):

        t=len(set(temp[i]).intersection(temp[j]))
        if len(temp[j])>len(temp[i]):
            similarity[i][j]=t/len(temp[i])*100
        else:
            similarity[i][j] = t / len(temp[j]) * 100

print(similarity)
r=[0 for i in range (len(temp))]
std=0
std_n=0
for i in range (len(temp)):
    for j in range (len(temp)):
        r[i]+=similarity[i][j]
    if r[i]>r[i-1]:
        std=r[i]
        std_n=i
count=0
print("common route",std_n,std)
for j in range (len(temp)):
    if similarity[std_n][j]<70:
        count+=1
        print("anomaly",j,train_route_ids[j])
print(count)