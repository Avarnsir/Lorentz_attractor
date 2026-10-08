<div align="center">
  <h1>🌀 Interactive 3D Lorenz Attractor</h1>
  <p><em>A numerical simulation of chaotic dynamics and the Lorenz system.</em></p>
</div>

<hr>

<h2>📖 Overview</h2>
<p>
  This repository contains a computational physics simulation of the <strong>Lorenz Attractor</strong>. Built entirely within a terminal-based Vim environment, the script utilizes numerical integration to map the chaotic trajectories of the Lorenz system in a 3D phase space. It features a fully interactive Matplotlib GUI, allowing real-time adjustment of system parameters to visualize the emergence of deterministic chaos.
</p>

<h2>✨ Features</h2>
<ul>
  <li><strong>Numerical Integration:</strong> Uses SciPy's <code>solve_ivp</code> (Runge-Kutta) for highly accurate differential equation solving.</li>
  <li><strong>Interactive 3D Visualization:</strong> Built-in UI sliders to dynamically adjust system parameters: <strong>&sigma;</strong> (Prandtl number), <strong>&rho;</strong> (Rayleigh number), and <strong>&beta;</strong>.</li>
  <li><strong>Optimized Environment:</strong> Designed to run purely from a self-contained Python virtual environment.</li>
</ul>

<h2>🚀 Quick Start</h2>
<h3>Prerequisites</h3>
<p>Ensure you have Python 3 installed on your system.</p>

<h3>Installation & Setup</h3>
<pre><code># Clone the repository
git clone https://github.com/yourusername/lorenz-attractor.git
cd lorenz-attractor

# Create and activate a virtual environment
python3 -m venv hdd_env
source hdd_env/bin/activate

# Install the required scientific libraries
pip install numpy scipy matplotlib
</code></pre>

<h3>Usage</h3>
<p>Run the simulation script from your terminal:</p>
<pre><code>python3 lorenz.py</code></pre>
<p>A window will open displaying the 3D phase-space plot. Use the sliders at the bottom of the window to recalculate the trajectories in real-time.</p>

<hr>

<h2>👨‍💻 Author</h2>
<p>
  <strong>Avarn Sharma</strong><br>
  <em>Computational Physics</em>
</p>
