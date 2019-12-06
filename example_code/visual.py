import os
import numpy as np
import glob
#import matplotlib.image as mpimg
#import matplotlib.pyplot as plt
import shutil
import sys
from operator import itemgetter

#%matplotlib inline

def main(image_path,number_of_pictures):

    image_path,image_name = os.path.split(image_path)
    subfolder_path,label = os.path.split(image_path)
    #image_name,extension = os.path.splitext(image_name)
    feature_extension = '.txt'
    image_dir = os.path.dirname(image_path)
    features_dir = os.path.join(os.path.dirname(image_dir),'bottlenecks_new')
    target_feature_text = os.path.join(features_dir,label,image_name) + feature_extension
    print(target_feature_text)

    
    s = []
    count=0
    dist = []
    #PATH = os.path.join('/','Users','dhruvag')
    # path where your WLS folder is stored.

    # #Store the feature vectors of the target image in s_arr.

    with open(target_feature_text, "r") as filestream:
        for i in filestream:
            s.append(i.split(","))
    s_arr = np.asarray([float(i) for i in s[0]])
    #print(s_arr[0:10])
    print('calculating distances...')
    for file in glob.glob(features_dir+'/**/*.txt', recursive=True):
        #print('Calculating Distances')
        s1 = []
        #print('processing for :'+ str(file))
        with open(file, "r") as filestream:
            for i in filestream: 
                s1.append(i.split(","))
        s1_arr = np.asarray([float(i) for i in s1[0]])
        dist.append([np.linalg.norm(s_arr-s1_arr),file])
    sorted_dist = sorted(dist, key=itemgetter(0))
    # print(os.path.dirname(image_dir))
    print('************************')
    print(sorted_dist[0])
    for i in sorted_dist[0:int(number_of_pictures)]:
        class_recommended= os.path.split(os.path.dirname(i[1]))[1]
        recommended_file_name = os.path.splitext(os.path.split(i[1])[1])[0]
        print('************************')
        print(recommended_file_name)
        image_path_recommended = os.path.join(image_dir,class_recommended,recommended_file_name)
        if i[0]==0:
            shutil.copyfile(image_path_recommended, os.path.join(os.path.dirname(image_dir),'predicted','original.jpg'))
            print('original file copied at :'+ os.path.join(os.path.dirname(image_dir),'predicted'))
        else:
            count+=1
            shutil.copyfile(image_path_recommended, os.path.join(os.path.dirname(image_dir),'predicted',str(class_recommended)+str(count)+'.jpg'))
        #image = mpimg.imread(path)
        #plt.imshow(image)
        #plt.show()
    



if __name__ == "__main__":
   main(sys.argv[1],sys.argv[2])


