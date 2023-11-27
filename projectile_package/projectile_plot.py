


def plot_xy(x_coord, height):
    
    import matplotlib.pyplot as plt
    
    plt.plot(x_coord, height) 
    plt.xlabel('x Coordinate (m)') 
    plt.ylabel('Height (m)') 
    plt.title('Height vs x Coordinate')
    plt.show()
