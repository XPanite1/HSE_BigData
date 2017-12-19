# HSE_BigData
Homeworks by course Big Data in HSE - 2017 (autumn)



## Docker: 
sudo docker run -i -t sequenceiq/hadoop-ubuntu:2.6.0 /etc/bootstrap.sh -bash

sudo docker ps
sudo docker cp ./for_hadoop/map2.py backstabbing_ardinghelli:map2.py
sudo docker cp ./for_hadoop/reduce2.py backstabbing_ardinghelli:reduce2.py
sudo docker cp ./for_hadoop/map_mean.py backstabbing_ardinghelli:map_mean.py
sudo docker cp ./for_hadoop/reduce_mean.py backstabbing_ardinghelli:reduce_mean.py
sudo docker cp ./for_hadoop/star2002-sample.csv backstabbing_ardinghelli:test.csv

bin/hdfs dfs -mkdir small_sample1
bin/hdfs dfs -put /test.csv ./small_sample1/ 



bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input small_sample1/ -output small_output1/advert -mapper map_mean.py  -reducer reduce_mean.py -file /map_mean.py -file /reduce_mean.py

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input small_output1/advert/ -output small_output2/advert -mapper map2.py  -reducer reduce2.py -file /map2.py -file /reduce2.py

