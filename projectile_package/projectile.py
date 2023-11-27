import matplotlib.pyplot as plt
from numpy import sign

def update_state(t, x, v, a, dt=0.1):
  
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt
    x += distance_moved

    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):


    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass

    return a

def calculate_acceleration_x(v, k=0.0, mass=1.0):

    
    force_air = -sign(v)*k*v**2
    total_force = force_air
    a = total_force/mass
    return a

def flying_mass(start_velocity_x, start_velocity_y, k=0.0, mass=1.0, dt=0.1):
    
    
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    x = 0
    h = 0
    v_x = start_velocity_x
    v_y = start_velocity_y
    
    t = 0.0

    # Create empty lists which we will update
    height = []
    x_coord = []
    velocity_x = []
    velocity_y = []
    time = []

    # Keep looping while the object is still falling
    while h >= 0:
        
        a_y = calculate_acceleration_y(v_y, k=k, mass=mass, gravity=gravity)
        a_x = calculate_acceleration_x(v_x, k=k, mass=mass)

        # Append values to list and then update 
        x_coord.append(x)
        height.append(h)
        velocity_y.append(v_y)
        velocity_x.append(v_x)
        time.append(t)

        # Update the state for time, height and velocity

        t, h, v_y = update_state(t, h, v_y, a_y, dt=dt)
        t, x, v_x = update_state(t, x, v_x, a_x, dt=dt)
    
    return time, x_coord, height, velocity_x, velocity_y
