#A description of what has been implemented
#Installation instructions (if any besides cloning the repo)
#Python packages should be listed appropriately in requirements.txt
#Run instructions
#What do I need to type to get your program to do its thing

# Crawl-and-Cluster--Tools Project
Our group name: Fantastic Four. Group members: Zeqi Zhu(zz2568), Qi Li(ql2336), Jiani Lu(jl5240), Xiao Liang(xl2817)
Enrolled in IEOR E4501 Section 001

Description: Our project was carried out in following steps.

First part, we wrote a web crawler that searches the house prices on www.streeteasy.com in Manhanttan Area, New York. The codes for this part are listed as "crawl.py" and "crawl.ipynb". There are some differences between these two code. 

For the "crawl.py", you have to change the cookie......(check out line 12 in the code), because the website has anti-crawl setting, and you have to excute the code several times if you want to to get a large-scale data, and obviously you will get several csv files which contains the raw data. 

For the "crawl.ipynb", we wrote a "for loop" to figure out the anti-crawl problem, you can get all the raw data by excuting the code once, and you will get one csv file which contains all the raw data. We suggest you to excute this code for your convenience.

Second step, we carried out analysis on the data we collected, based on the “K-means Clustering Algorithm". The codes for this part are listed as "CSV merge and process.ipynb" and "K-means.ipynb". The "CSV merge and process.ipynb" is used to clean the raw data we initially collected from the website, the raw data are listed in the "datafile.csv", the data after being clearned are saved in the "processed_data.csv". Then the "K-means.ipynb" is used to 

