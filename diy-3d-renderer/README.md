# DIY-3D-Renderer

A toy 3D renderer built without any 3D graphics libraries. Every pixel is drawn from scratch!

I originally wanted to learn how to use OpenGL to create 3D graphics, but I had a very hard time understanding the fundamental 3D concepts like normals, projections, and lighting. Making my own simple 3D renderer taught me so much about these tricky topics, so hopefully learning OpenGL will be easier now. Plus, this project was super fun to work on!

**Features I've implemented:** custom matrix and vector classes, object transformations, projection+perspective matrices, camera movement, triangle rasterization, normal creation, backface+frustum culling, STL importing, ambient+diffuse lighting, z-buffering, hacky vertex coloring

**Features I want to implement:** object texturing, specular lighting (Phong), support for multiple lights, multithreading, background images from a file, text rendering, general optimizations

**Current problems:** overall very slow and unoptimized, shaders should belong to objects, renderer class is too big, no clear file standard for individually coloring vertices

<br />
To show what the engine can do, I made a simple infinite runner game. Try to stay alive as long as you can by jumping and moving to avoid the spikes.

<video width="450" autoplay loop muted>
  <source src="https://github.com/ehanover/diy-3d-renderer/blob/main/screenshots/infinite-runner-game.mp4?raw=true" type="video/mp4" />
</video>
