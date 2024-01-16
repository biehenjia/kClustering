from random import randint
import matplotlib.pyplot as plt

#Ignore this pls :3
version = [0]

class Point():
    """
    A class to represent a point

    Attributes:
        xPos: int
            the x position of the point
        yPos: int
            the y position of the point
    """
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def get_coords(self):
        '''
        Returns the coordinates of the point
        
            Parameters:
                None
            Returns:
                The x and y positions
        '''
        return [self.x_pos,self.y_pos]

class Cluster():
    """
    A class to represent a cluster

    Attributes:
        points: list
            the points that belong to this cluster
        y_pos: int
            the y position of the point
        x_pos: int
            the x position of the point
    """
    def __init__(self,points):
        self.points = points
        cluster_x,cluster_y = self.get_centroid()
        self.centroid = Point(cluster_x,cluster_y)

    def get_centroid(self):
        '''
        Returns the centroid

                Parameters:
                    None
                Returns:
                    cluster_x (int): the x position of the centroid
                    cluster_y (int): the y position of the centroid
        '''
        cluster_x = 0
        cluster_y = 0
        num_points = len(self.points)

        for point in self.points:
            point_x,point_y = point.getCoords()

            cluster_x += point_x
            cluster_y += point_y

        cluster_x /= num_points
        cluster_y /= num_points

        return cluster_x,cluster_y

    def shift_centroid(self,new_points):
        '''
        Updates the centroid to encompass a new set of points.
        Returns the distance that the centroid travelled.

                Parameters:
                    new_points (list): a list of new points 

                Returns:
                    delta (float): the distance between the old and new centroids
        '''
        centroid = self.centroid
        self.points = new_points

        x_pos,y_pos = self.get_centroid()
        self.centroid = Point(x_pos,y_pos)

        delta = get_dist(centroid,self.centroid)

        return delta

    def get_deviation(self):
        '''
        Returns the sum of two decimal numbers in binary digits.

            Parameters:
                None

            Returns:
                deviation (float): the sum of the distances between a cluster's centroid and its respective points
        '''
        deviation = 0
        for point in self.points:
            deviation += get_dist(self.centroid,point)
        return deviation

def get_dist(point1,point2):
    '''
    Returns the distance between the two points

        Parameters:
            point1 (Point): the first point
            point2 (Point): the second point

        Returns:
            dist (float): the distance between the two points
    '''
    x1,y1 = point1.getCoords()
    x2,y2 = point2.getCoords()

    dx = abs(x2-x1)
    dy = abs(y2-y1)

    dist = (dx**2+dy**2)**0.5

    return dist

def kmeans(points, k, threshold):
    '''
    Returns the clusters after the threshold is met

        Parameters:
            points (list): a list containing all the points
            k (int): the number of clusters 
            threshold (int): the threshold to stop the iterations

        Returns:
            clusters (list): a list of length k containing the clusters
    '''
    centroids = points[:k]
    clusters = [(Cluster([centroids[i]]),i) for i in range(len(centroids))]
    delta = 100

    while delta > threshold:
        for cluster in clusters:
            x,y = cluster[0].centroid.get_coords()
            x,y = int(x), int(y)

            plt.plot(x,y,'x')
            for point in cluster[0].points:

                px,py = point.getCoords()
                plt.plot(px,py,'bo')

                xval = [x,px]
                yval = [y,py]

                plt.plot(xval,yval,'r-')

        plt.savefig(f'newRun\{version[0]}.png')

        plt.close()
        version[0] +=1 

        #print('hi i iterated')

        home_clusters = [[] for cluster in clusters]
        for point in points:

            plt.plot()
            _, home = min(clusters,  key = lambda  x:  get_dist(x[0].centroid,point))
            home_clusters[home].append(point)
        delta = max([clusters[i][0].shift_centroid(home_clusters[i]) for i in range(len(clusters))])
    return clusters

def itkmeans(points, k, threshold, iterations):
    '''
    Returns the clusters after updating the points over some iterations
    Returns the best cluster, based on combined distance to the centroid

        Parameters:
            points (list): a list containing all the points
            k (int): the number of clusters 
            threshold (int): the threshold to stop the iterations
            iterations (int): the number of iterations to run kmeans over.

        Returns:
            history (list): a list of the previous best clusters 
            cluster (list): a list of the points within the current best cluster
    '''
    history = []
    for i in range(iterations):

        clusters = kmeans(points, k, threshold)
        error = get_total_deviation(clusters)

        history.append((clusters,error))

    return min(history, key = lambda x: x[1])[0],history

def get_total_deviation(clusters):
    '''
    Returns the total deviation of the clusters,
    total deviation is the average difference between all points and their respective clusters

        Parameters:
            clusters (list): a list containing all the clusters 

        Returns:
            total_deviation (float): the average deviation between all clusters and their points 
    '''
    total_deviation = sum([cluster[0].getDeviation() for cluster in clusters])/len(clusters)
    return total_deviation

def generate_points(num_points,low,high):
    '''
    Returns a list of randomly generated points

        Parameters:
            num_points (int): the number of points to generate
            low (int): the lower bound for random numbers to generate
            high (int): the upper bound for random numbers to generate
        Returns:
            points (list): a list of randomly generated points
    '''
    points = []
    for i in range(num_points):

        x_pos = randint(low,high)
        y_pos = randint(low,high)

        new_point = Point(x_pos,y_pos)
        points.append(new_point)

    return points

def simulate(num_points,low,high,iterations,k,threshold):
    '''
    Simulates the k-means clustering algorithm
        Parameters:
            num_points (int): the number of points to generate
            low (int): the lower bound for random numbers to generate
            high (int): the upper bound for random numbers to generate
            k (int): the number of clusters to generate
            threshold (int): the lower thresholod to stop at
            num_points (int): the number of points to generate
        Returns:
            None
    '''
    points = generate_points(num_points,low,high)
    itkmeans(points,k,threshold,iterations)

simulate(500,0,10000,2,10,15)