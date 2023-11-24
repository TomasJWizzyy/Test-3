import matplotlib.pyplot as plt
from numpy import sign

def update_state(t, x, v, a, dt=0.1):
    ''' Update each parameter for the next time step. Args:
        t, x, v, a (float) :
            time (s), position (m) and velocity (m/s) and acceleration (m/s2) value for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float : Updated values for t, h, v after this time step
    ''' distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt
    x += distance_moved

    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    ''' Calculate the acceleration based on combined forces from gravity and air resistance. Args:
        v (float) :
            velocity (m/s) for this time step
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. Should be positive. Default = 0.0 i.e. no air 
            resistance
        mass (float) :
            Mass of the falling object. Needed if k > 0. Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2. Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass

    return a

def calculate_acceleration_x(v, k=0.0, mass=1.0):
    ''' Calculate the acceleration based on combined forces from gravity and air resistance. Args:
        v (float) :
            velocity (m/s) for this time step
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. Should be positive. Default = 0.0 i.e. no air 
            resistance
        mass (float) :
            Mass of the falling object. Needed if k > 0. Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2. Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    
    force_air = -sign(v)*k*v**2
    total_force = force_air
    a = total_force/mass
    return a

def falling_mass(initial_height, k=0.0, mass=1.0, dt=0.1):
    # Fixed input values
    start_velocity = 0.0 # m/s
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    distance_moved = 0
    h = initial_height
    v = start_velocity
    t = 0.0

    # Create empty lists which we will update
    height = []
    velocity = [] 
    time = []

    # Keep looping while the object is still falling
    while h > 0:
       
         # Evaluate the state of the system - start by calculating the total force on the object 
         a = calculate_acceleration(v, k=k, mass=mass, gravity=gravity)

         # Append values to list and then update 
         height.append(h)
         velocity.append(v)
         time.append(t)

         # Update the state for time, height and velocity

         t, h, v = update_state(t, h, v, a, dt=dt)
    
    return time, height, velocity
