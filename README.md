#A description of what has been implemented
#Installation instructions (if any besides cloning the repo)
#Python packages should be listed appropriately in requirements.txt
#Run instructions
#What do I need to type to get your program to do its thing

# Crawl-and-Cluster--Tools Project
### Our group name: Fantastic Four. 
### Group members: Zeqi Zhu(zz2568), Qi Li(ql2336), Jiani Lu(jl5240), Xiao Liang(xl2817)
### Enrolled in IEOR E4501 Section 001

#### Description
Our project was carried out in following steps.<br>

* First part, we wrote a web crawler that searches the house prices on www.streeteasy.com in Manhanttan Area, New York. 
The codes for this part are listed as [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py) and [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb). <br>
Because the website has the anti-crawl setting, which means we can only crawl nearly four pages' data with one cookie. If we want to get a large-scale data, we need to change the cookie each time we excute the code. <br>
Therefore, We came up with two ideas to firgure out this problem, which are listed as [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py) and [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb)

  * For the [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py), you have to change the cookie......(check out line 12 in the code) every time you excute the code, and you have to excute the code several times if you want to to get a large-scale data, and obviously you will get several csv files which contains the raw data. 

  * For the [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb),  , you can get all the raw data by excuting the code, and you will get one csv file which contains all the raw data. We suggest you to excute this code for your convenience.

* Second part, we carried out analysis on the data we collected, based on the “K-means Clustering Algorithm". <br>
  * The codes for this part are listed as [CSV merge and process.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/CSV%20merge%20and%20process.ipynb) and [K-means.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/kmeans.ipynb). <br>
  * The [CSV merge and process.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/CSV%20merge%20and%20process.ipynb) has two functions. Merging several csv.files into one single csv.file and cleaning the raw data we initially collected from the website.<br>
  * The raw data are listed in the [datafile.csv](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/datafile.csv), the data after being clearned are saved in the [processed_data.csv](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/processed_data.csv). <br>
  * The [K-means.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/kmeans.ipynb) is used to 

* Data analysis Result<br>
![](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/visualized%20data.png)
#### Packages need to install
* For the crawl code, we need to install following packages:<br>
  * `pandas`
  * `requests`
  * `time`
  * `lxml`
  * `bs4` 
* For the Data Analysis code, we need to install the following packages:<br>
  * `sklearn.cluster`
  * `matplotlib.pyplot`

#### Run instructions
* You have to refresh the website and add the new cookie into the code when you excute the code each time. 
