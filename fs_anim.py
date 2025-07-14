import numpy as np
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time

# Create the x domain
num_points = 1000
x_a = np.linspace(-1*np.pi, np.pi, num_points)

#This is the general function for FS Synthisis
def fs_synthesis(a0, an, bn, L, n, x):
    f = np.zeros(num_points) + a0 * 0.5 
    for k in range(1, n):
        f += (an(k) * np.cos(2 * np.pi * k * x/L) + bn(k) * np.sin(2 * np.pi * k * x/L))
    return f

### Square wave
# Original square wave function
def create_square_wave(x):
    x1 = np.sign(np.sin(x))
    x1[:len(x)//2] = 0
    return x1
    
def an_sqr(n):
    return 0
def an_sqr(n):
    return 0

def bn_sqr(n):
    if n%2 == 0:
        return 0
    return 2/(n*np.pi)

### Sawtooth
# Original sawtooth wave function (f(x) = x/π normalized to [-1,1] over period)
def create_sawtooth_wave(x):
    return x/np.pi

def an_st(n):
    return 0

def bn_st(n):
    return (2/np.pi) * ((-1)**(n+1)) / n

# Original triangle wave function
def create_triangle_wave(x):
    x1 = np.abs(x)
    return x1

def an_triangle(n):
    if n % 2 == 0:
        return 0
    return (-4/np.pi) * (1/n**2)

def bn_triangle(n):
    return 0

###Rectified sine wave 

def create_rectified_sine_wave(x):
    return np.abs(np.sin(x))

def an_rectified_sine(n):
    if n % 2 == 0:
        return (-4 / (np.pi * (n**2 - 1))) 
    return 0

def bn_rectified_sine(n):
    return 0

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Original function
#original = create_square_wave(x_a)
#original = create_sawtooth_wave(x_a)
#original = create_triangle_wave(x_a)
original = create_rectified_sine_wave(x_a)
original_line, = ax.plot(x_a, original, 'b-', label='Original Rectified sine wave')

# Initial Fourier approximation
initial_n = 1
fourier_line, = ax.plot(x_a, create_rectified_sine_wave(x_a), 'r-', 
                       label=f'Fourier approximation (n={initial_n})')


# Set up the plot
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.grid(True)
ax.legend(loc='upper right')

# Define max number of terms for animation
max_terms = 60

# Animation function
def animate(frame):
    #time.sleep(0.5)
    n = frame + 1  # Start from n=1
    
    # Update the Fourier approximation line
    #fourier_data = fourier_series_sqr(x_a, n)
    #fourier_data = fourier_series_sawtooth(x_a, n)
    #fourier_data = fs_synthesis(1, an_sqr, bn_sqr, np.pi, n, x_a )
    #fourier_data = fs_synthesis(0, an_st, bn_st, 2*np.pi, n, x_a )
    #fourier_data = fs_synthesis(np.pi, an_triangle, bn_triangle, 2*np.pi, n, x_a )
    fourier_data = fs_synthesis(4/np.pi, an_rectified_sine, bn_rectified_sine, 2*np.pi, n, x_a )
    fourier_line.set_ydata(fourier_data)
    
    # Update the title and label
    ax.set_title(f'Rectified sine wave and its Fourier approximation with {n} term(s)')
    fourier_line.set_label(f'Fourier approximation (n={n})')
    
    # Update legend
    ax.legend(loc='upper right')
    
    return fourier_line,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=max_terms, blit=False, interval=500, repeat=False)
ani.save('fs_rectified_sine.gif', writer='pillow', fps=5)

plt.tight_layout()
plt.show()
