import pandas

air_df=pandas.read_csv('long_routes_a2t.csv')

air_route_ids = air_df['route_number'].unique()

air_route_cells_m=air_df['cell'].unique()
print(len(air_route_cells_m))
print(air_route_cells_m)
print(air_route_ids)

temp=[]
i=0
for number in air_route_ids:
    #if air_df['route_number'].values.any()!=375971 or air_df['route_number'].values.any()!=324340 or air_df['route_number'].values.any()!=164729:

        route_df = air_df[air_df['route_number'] == number]
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

print("common route",std_n,std)
for j in range (len(temp)):
     if similarity[std_n][j]<70:
         if air_route_ids[j]!=375971 and air_route_ids[j]!=324340 and air_route_ids[j]!=164729:
            print("anomaly",j,air_route_ids[j])