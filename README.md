# taxi-fraud-detection

Taxi drivers fleecing customers is a concern for most taxi companies and drivers especially in a world where they are increasingly losing business to ride sharing services like Uber and Lyft. Detecting taxi drivers engaging in fraud would be monumental in increasing customer satisfaction and saving business. We used GPS data of taxi trajectories and tried to find anomalies by mutual comparison of routes for a source-destination pair. This analysis was done using just 2 days of data as opposed to months of data used by other similar studies but still was able to detect anomalous trajectories to a reasonable degree. This makes use of pandas for dealing with huge amounts of data.

The following code detects fradulant taxi trajectories by analysis of GPS data for the Chinease city of Shenzen
Only filterd data used in analysis is included with code. Complete original data in not included as its size is around 2TB 


