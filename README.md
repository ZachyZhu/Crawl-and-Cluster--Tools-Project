#A description of what has been implemented
#Installation instructions (if any besides cloning the repo)
#Python packages should be listed appropriately in requirements.txt
#Run instructions
#What do I need to type to get your program to do its thing

# Crawl-and-Cluster--Tools Project
Our group name: Fantastic Four. Group members: Zeqi Zhu(zz2568), Qi Li(ql2336), Jiani Lu(jl5240), Xiao Liang(xl2817)
---
Enrolled in IEOR E4501 Section 001
---
Description: Our project was carried out in following steps.

* First part, we wrote a web crawler that searches the house prices on www.streeteasy.com in Manhanttan Area, New York. 
The codes for this part are listed as `crawl.py` and `spider.ipynb`. <br>
Because the website has the anti-crawl setting, which means we can only crawl nearly four pages' data with one cookie. If we want to get a large-scale data, we need to change the cookie each time we excute the code. <br>
Therefore, We came up with two ideas to firgure out this problem, which are listed as `crawl.py` and `spider.ipynb`

  * For the 'crawl.py', you have to change the cookie......(check out line 12 in the code) every time you excute the code, and you have to excute the code several times if you want to to get a large-scale data, and obviously you will get several csv files which contains the raw data. 

  * For the 'spider.ipynb',  , you can get all the raw data by excuting the code, and you will get one csv file which contains all the raw data. We suggest you to excute this code for your convenience.

* Second step, we carried out analysis on the data we collected, based on the “K-means Clustering Algorithm". <br>
The codes for this part are listed as `CSV merge and process.ipynb` and `K-means.ipynb`. <br>
The `CSV merge and process.ipynb` is used to clean the raw data we initially collected from the website, the raw data are listed in the `datafile.csv`, the data after being clearned are saved in the `processed_data.csv`. <br>
Then the `K-means.ipynb` is used to 

