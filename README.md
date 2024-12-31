# Gradient-Styler v1.0 For Katana
This Tool create gradient colors for nodes in The Foundry Katana


![UI](https://github.com/user-attachments/assets/5cc576c9-e719-4d48-80b5-cc043f7d47e8)

Developed in Python for Katana, specifically designed to style and customize nodes in the Node Graph by applying color gradients.
## Features
* Custom Color Selection: allows you to choose two colors to generate a gradient that will be applied to the selected nodes.

* Automatic Position Detection: Detects the position of the nodes on the Y axis of the Node Graph to calculate the gradient accurately.
### Special Scenarios:
* If only one node is selected, the first color chosen is applied.
* If no nodes are selected, it displays a message indicating that at least one node is needed to apply the gradient.

# How to install

1. Copy the Python script and the `gradientStyler.png` file.
2. Navigate to your Katana configuration folder. On Windows, the default location is: C:\Users<YourUsername>\.katana\Shelves\Python

# How it works

The gradient at intermediate nodes is applied by interpolating the color values between the initial color and the final color using a mathematical formula based on the proportion of each node within the sequence.

The basic formula for calculating a color value in the gradient is:

![formula](https://github.com/user-attachments/assets/e5dd8ca5-b74a-43d1-85e5-cf2ca4c3eda5)

### Ci = Node color at position i
### Cstart = Initial color of the first node
### Cend = Final color of the last node
### i = Current node position (starting from 0)
### n = Total number of nodes in the sequence
