import pandas
#train_df=pandas.read_csv('train/west-to-north-routes-with-cells.csv')
train_df=pandas.read_csv('train/north-to-west-routes-with-cells.csv')

# top=pandas.read_csv('topGoogleMapRoute.csv')
# middle=pandas.read_csv('middleGoogleMapRoute.csv')
# bottom=pandas.read_csv('bottomGoogleMapRoute.csv')
# middle2=pandas.read_csv('middleGoogleMapRoute2.csv')

left=pandas.read_csv('train/North-Train-To-West-Left-Google-Maps-Route-Cells.csv')
middle=pandas.read_csv('train/North-Train-To-West-Middle-Google-Maps-Route-Cells.csv')
#########################################################################################
top=pandas.read_csv('train/West-Train-To-North-Top-Google-Maps-Route-Cells.csv')
middle2=pandas.read_csv('train/West-Train-To-North-Middle-Google-Maps-Route-Cells.csv')
bottom=pandas.read_csv('train/West-Train-To-North-Bottom-Google-Maps-Route-Cells.csv')
#middle2=pandas.read_csv('middleGoogleMapRoute2.csv')


top_cells=top['cell'].unique()
middle_cells=middle['cell'].unique()
bottom_cells=bottom['cell'].unique()
left_cells=left['cell'].unique()
middle_cells2=middle['cell'].unique()
#middle_cells2=middle2['cell'].unique()

#train_df=pandas.read_csv('long_routes_t2a.csv')
train_route_ids = train_df['route_number'].unique()
train_route_cells_m=train_df['cell'].unique()

temp=[]
i=0
for number in train_route_ids:
     route_df = train_df[train_df['route_number'] == number]
     route_df=route_df['cell'].unique()
     temp.append(route_df)


similarity_top=[0 for i in range (len(temp))]
similarity_mid2=[0 for i in range (len(temp))]
similarity_bottom=[0 for i in range (len(temp))]
similarity_left=[0 for i in range (len(temp))]
similarity_mid=[0 for i in range (len(temp))]
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
        t=len(set(temp[i]).intersection(middle_cells2))
        if len(middle_cells2)>len(temp[i]):
            similarity_mid2[i]=t/len(temp[i])*100
        else:
            similarity_mid2[i] = t / len(middle_cells2) * 100
            ###################################################################
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(bottom_cells))
        if len(bottom_cells)>len(temp[i]):
            similarity_bottom[i]=t/len(temp[i])*100
        else:
            similarity_bottom[i] = t / len(bottom_cells) * 100
            ###################################################################
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(left_cells))
        if len(left_cells)>len(temp[i]):
            similarity_left[i]=t/len(temp[i])*100
        else:
            similarity_left[i] = t / len(left_cells) * 100
            ###################################################################
for i in range (len(temp)):
        t=len(set(temp[i]).intersection(middle_cells))
        if len(middle_cells)>len(temp[i]):
            similarity_mid[i]=t/len(temp[i])*100
        else:
            similarity_mid[i] = t / len(middle_cells) * 100

#print(similarity_top)
#print("train to air")
count=0
for i in range (len(temp)):
    #if similarity_mid[i]<80 and similarity_left[i]<80:
    if similarity_top[i]<80 and similarity_mid2[i]<80 and similarity_bottom[i]<80 and similarity_mid[i]<80 and similarity_left[i]<80:
         count+=1
         print("anomaly",train_route_ids[i])
print(count)