import numpy as np
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time

# Create the x domain
x_a = np.linspace(-1*np.pi, np.pi, 1000)

# Original square wave function
def create_square_wave(x):
    x1 = np.sign(np.sin(x))
    x1[:len(x)//2] = 0
    return x1

# Corrected Fourier series function
def fourier_series_sqr(x, n):
    f = 0.5
    for k in range(n):
        f += (2 / ((2*k + 1)* np.pi)) * np.sin((2*k + 1) * x)
    return f

# Original sawtooth wave function (f(x) = x/π normalized to [-1,1] over period)
def create_sawtooth_wave(x):
    return x/np.pi

# Fourier series approximation for sawtooth wave
def fourier_series_sawtooth(x, n_terms):
    """
    Computes the Fourier series approximation for a sawtooth wave.
    
    For a sawtooth wave f(x) = x/π over [-π,π], the Fourier series is:
    f(x) = 2/π * sum_{k=1}^{n} (-1)^(k+1)/k * sin(kx)
    """
    result = np.zeros_like(x)
    
    for k in range(1, n_terms + 1):
        # Calculate the coefficient: (-1)^(k+1)/k
        coefficient = ((-1)**(k+1)) / k
        
        # Add the term: coefficient * sin(kx)
        result += coefficient * np.sin(k * x)
    
    # Multiply by the scaling factor 2/π
    result *= 2/np.pi
    
    return result

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Original function
#original = create_square_wave(x_a)
original = create_sawtooth_wave(x_a)
original_line, = ax.plot(x_a, original, 'b-', label='Original sawtooth wave')

# Initial Fourier approximation
initial_n = 1
fourier_line, = ax.plot(x_a, fourier_series_sqr(x_a, initial_n), 'r-', 
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
    fourier_data = fourier_series_sawtooth(x_a, n)
    fourier_line.set_ydata(fourier_data)
    
    # Update the title and label
    ax.set_title(f'Square wave and its Fourier approximation with {n} term(s)')
    fourier_line.set_label(f'Fourier approximation (n={n})')
    
    # Update legend
    ax.legend(loc='upper right')
    
    return fourier_line,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=max_terms, blit=False, interval=1000, repeat=False)
ani.save('fs_sawtooth.gif', writer='pillow', fps=5)

plt.tight_layout()
plt.show()
