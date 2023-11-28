

# defining function that plots x against y through time
def plot_xy(x_coord, height):
    
    import matplotlib.pyplot as plt
    
    # this plots a line graph showing the trajectory of the mass
    plt.plot(x_coord, height) 
    plt.xlabel('x Coordinate (m)') 
    plt.ylabel('Height (m)') 
    plt.title('Height vs x Coordinate')
    # shows the figure
    plt.show()
