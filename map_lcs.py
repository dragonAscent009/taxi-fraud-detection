import pandas
top=pandas.read_csv('topGoogleMapRoute.csv')
middle=pandas.read_csv('middleGoogleMapRoute.csv')
bottom=pandas.read_csv('bottomGoogleMapRoute.csv')
#middle2=pandas.read_csv('bottomGoogleMapRoute2.csv')


top_cells=top['cell'].unique()
middle_cells=middle['cell'].unique()
bottom_cells=bottom['cell'].unique()
#middle_cells2=middle2['cell'].unique()

air_df=pandas.read_csv('long_routes_a2t.csv')
air_route_ids = air_df['route_number'].unique()
air_route_cells_m=air_df['cell'].unique()

temp=[]
i=0
for number in air_route_ids:
     route_df = air_df[air_df['route_number'] == number]
     route_df=route_df['cell'].unique()
     temp.append(route_df)


similarity_top=[0 for i in range (len(temp))]
similarity_mid=[0 for i in range (len(temp))]
similarity_bottom=[0 for i in range (len(temp))]
#similarity=[]
#similarity=[[0 for i in range (len(temp))]for j in range (len(temp))]
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(top_cells))
        if len(top_cells)>len(temp[i]):
            similarity_top[i]=t/len(temp[i])*100
        else:
            similarity_top[i] = t / len(top_cells) * 100
            ##################################################################
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(middle_cells))
        if len(middle_cells)>len(temp[i]):
            similarity_mid[i]=t/len(temp[i])*100
        else:
            similarity_mid[i] = t / len(middle_cells) * 100
            ###################################################################
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(bottom_cells))
        if len(bottom_cells)>len(temp[i]):
            similarity_bottom[i]=t/len(temp[i])*100
        else:
            similarity_bottom[i] = t / len(top_cells) * 100

#print(similarity_top)#
#print("air to train")
for i in range (len(temp)):
     if similarity_top[i]<90 and similarity_bottom[i]<90 and similarity_mid[i]<90:
         if air_route_ids[i] != 375971 and air_route_ids[i] != 324340 and air_route_ids[i] != 164729:
            print("anomaly",air_route_ids[i])