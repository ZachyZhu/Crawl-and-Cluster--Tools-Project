# Crawl-and-Cluster--Tools Project
### Our group name: Fantastic Four
### Group members: Zeqi Zhu (zz2568), Qi Li (ql2336), Jiani Lu (jl5240), Xiao Liang (xl2817)
### Enrolled in IEOR E4501 Section 001

#### Brief Description
Our project was carried out in following parts.<br>

* First part, we wrote a web crawler that searches the house prices on https://streeteasy.com/for-sale/manhattan in Manhanttan Area.<br> 
  * `Attention:` As the website has the `anti-crawl setting`, which means each cookie can only allow us to crawl nearly four pages' data (nearly 40 data sets). Thus we set the length of pages we want to crawl into `4` in the code. In order to obtain a large-scale datasets (nearly one thousand datasets in our project), we have to refresh the website and update the cookie each time when we execute the code. <br>
  
  * In order to figure out how to overcome the `anti-crawl setting`, We make an assumption that the `anti-crawl setting` is based on the time interval when we crawl the data from different pages. We built another `try` branch to store the files. It is optional for you to review this branch. Our main work are on the `master` branch.

  * The codes for this part are listed as [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py) and [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb). <br>

  * These two codes almost work with the same effect, except the datafile.csv you would acquire after you executing them.

    * For the [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py), you have to update the cookie each time, and also remember to rename the datafile.csv (line 119) before you execute the code for another time.<br> Otherwise, the new data would cover the data crawled from last execution. With this code, you are supposed to generate several csv files which contains the raw data. 

    * For the [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb), you also have to update the cookie each time, and excute the code several times. However, you do not need to rename the datafile.csv. It would be updated when you executing the code with a new cookie and you are supposed to obtain a single datafile.csv which contains all the data you crawled through all former excutations.<br>
  
  * We would suggest you to execute [spider.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/spider.ipynb) for your convenience.

* Second part, we carried out analysis on the data we collected, based on the “K-means Clustering Algorithm". <br>
  * The codes for this part are listed as [CSV merge and process.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/CSV%20merge%20and%20process.ipynb) and [K-means.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/kmeans.ipynb). <br>
  * The [CSV merge and process.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/CSV%20merge%20and%20process.ipynb) has two functions. Merging several csv.files into one single csv.file if you choose to use [crawl.py](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/crawl.py) to crawl the data, and cleaning the raw data we initially collected from the website. Data cleaning includes following work:<br>
    * Convert the price of the house into unit price, and only keep four categories of the data, which are "unit price", "address", "type", "area". 
    * Find the house with the highest unit price, set this data to be our standard point - with the highest price and the excellent location. 
    * Calculate the distance from other houses to the original point, based on the address. We googled out the following information to help us estimate the distance with two different addresses in Manhanttan: ["North-south is easy: about 20 blocks to a mile. The annual Fifth Avenue Mile, for example, is a race from 80th to 60th Street. The distance between avenues is more complicated. In general, one long block between the avenues equals three short blocks, but the distance varies, with some avenues as far apart as 920 feet."](https://www.nytimes.com/2006/09/17/nyregion/thecity/17fyi.html)
  * The raw data are listed in the [datafile.csv](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/datafile.csv), the data after being clearned are saved in the [processed_data.csv](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/processed_data.csv). <br>  
  * The [K-means.ipynb](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/kmeans.ipynb) is used to divide these datasets into three kinds. See the following cluster result.

* Data analysis Result<br>
![](https://github.com/ZachyZhu/Crawl-and-Cluster--Tools-Project/blob/master/visualized%20data.png)

* Result Explanation <br>
All the datas are differentiated into three types，and the datas marked in `Blue` represent the center points of these three different types.
  * The first type are maked in `Red 0`. These datasets represents those houses which are very close to the standard point, but the price are much higher.
  * The second type are marked in `Green 1`. These datasets represents those houses which prices are very close to the standard point, but the distance to our standard point are much too far.
  * The third type are marked in `Brown 2`. These datasets represents those houses which prices are very close to the standard point, as well as the location.
  * If you are considering about purchasing your own house in Manhanttan, it would be a better strategy to start your research among those houses in the `Brown 2` type. If you do not care about the money, the `Red 0` type has a higher possibility containing your future potential home. And if you are working to your best to earn money, type `Green 1` would be a better fit for you.


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
* You have to refresh the website https://streeteasy.com/for-sale/manhattan and add the new cookie into the code when you excute the code each time. 
